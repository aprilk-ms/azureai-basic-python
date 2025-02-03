import contextlib
import logging
import os
import pathlib
from typing import Union, Any

import fastapi
from azure.ai.projects.aio import AIProjectClient
from azure.ai.inference.prompts import PromptTemplate
from azure.identity import AzureDeveloperCliCredential, ManagedIdentityCredential
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

from .shared import globals

from azure.ai.inference.tracing import AIInferenceInstrumentor 
from azure.monitor.opentelemetry import configure_azure_monitor

from azure.identity import DefaultAzureCredential
from azure.appconfiguration.provider import load
from featuremanagement import FeatureManager
from featuremanagement.azuremonitor import publish_telemetry

from opentelemetry.baggage import get_baggage
from opentelemetry.sdk.trace import Span, SpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.baggage import set_baggage
from opentelemetry.context import attach
from opentelemetry.sdk.trace import Span

import uuid

logger = logging.getLogger("azureaiapp")
logger.setLevel(logging.INFO)

@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    azure_credential: Union[AzureDeveloperCliCredential, ManagedIdentityCredential]
    if not os.getenv("RUNNING_IN_PRODUCTION"):
        if tenant_id := os.getenv("AZURE_TENANT_ID"):
            logger.info("Using AzureDeveloperCliCredential with tenant_id %s", tenant_id)
            azure_credential = AzureDeveloperCliCredential(tenant_id=tenant_id)
        else:
            logger.info("Using AzureDeveloperCliCredential")
            azure_credential = AzureDeveloperCliCredential()
    else:
        # User-assigned identity was created and set in api.bicep
        user_identity_client_id = os.getenv("AZURE_CLIENT_ID")
        logger.info("Using ManagedIdentityCredential with client_id %s", user_identity_client_id)
        azure_credential = ManagedIdentityCredential(client_id=user_identity_client_id)

    project = AIProjectClient.from_connection_string(
        credential=azure_credential,
        conn_str=os.environ["AZURE_AIPROJECT_CONNECTION_STRING"],
    )

    chat = await project.inference.get_chat_completions_client()
    prompt = PromptTemplate.from_prompty(pathlib.Path(__file__).parent.resolve() / "prompt.prompty")

    # Enable tracing
    application_insights_connection_string = await project.telemetry.get_connection_string()
    configure_azure_monitor(connection_string=application_insights_connection_string, span_processors=[TargetingSpanProcessor()])
    AIInferenceInstrumentor().instrument() 

    # Inititalize the feature manager
    app_config_conn_str = os.getenv("APP_CONFIGURATION_ENDPOINT") # this will become: project.experiments.get_connection_string()
    app_config = load(
        endpoint=app_config_conn_str,
        credential=DefaultAzureCredential(),
        feature_flag_enabled=True,
        feature_flag_refresh_enabled=True,
        refresh_interval=30,  # 30 seconds
    )
    feature_manager = FeatureManager(app_config, on_feature_evaluated=publish_telemetry)

    globals["project"] = project
    globals["chat"] = chat
    globals["prompt"] = prompt
    globals["chat_model"] = os.environ["AZURE_AI_CHAT_DEPLOYMENT_NAME"]
    globals["feature_manager"] = feature_manager

    yield

    await project.close()

    await chat.close()

# Below will be replaced by a helper function from App Config SD

class TargetingSpanProcessor(SpanProcessor):
    def on_start(
        self,
        span: "Span",
        parent_context = None,
    ):
        if (get_baggage("Microsoft.TargetingId", parent_context) != None):
            span.set_attribute("TargetingId", get_baggage("Microsoft.TargetingId", parent_context))

def server_request_hook(span: Span, scope: dict[str, Any]):
     if span and span.is_recording():
        targeting_id = str(uuid.uuid4())
        attach(set_baggage("Microsoft.TargetingId", targeting_id))
        span.set_attribute("TargetingId", targeting_id)

# End Targeting Id code

def create_app():
    if not os.getenv("RUNNING_IN_PRODUCTION"):
        logger.info("Loading .env file")
        load_dotenv(override=True)

    app = fastapi.FastAPI(lifespan=lifespan)

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    if os.path.isdir(static_dir):
        app.mount("/static", StaticFiles(directory=static_dir), name="static")

    from . import routes  # noqa

    app.include_router(routes.router)

    FastAPIInstrumentor.instrument_app(app, server_request_hook=server_request_hook)

    return app
