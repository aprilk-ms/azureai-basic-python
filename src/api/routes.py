# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for full license information.
import json
import logging
import os

import fastapi
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from featuremanagement.azuremonitor import track_event

import uuid
import pathlib
from azure.ai.inference.prompts import PromptTemplate
from azure.ai.inference.prompts import PromptTemplate
from azure.ai.inference import ChatCompletionsClient

from .util import get_logger, ChatRequest
from .search_index_manager import SearchIndexManager
from azure.core.exceptions import HttpResponseError


logger = get_logger(
    name="azureaiapp_routes",
    log_level=logging.INFO,
    log_file_name=os.getenv("APP_LOG_FILE"),
    log_to_console=True
)

from opentelemetry.baggage import get_baggage
from azure.ai.evaluation import CoherenceEvaluator, FluencyEvaluator, RelevanceEvaluator, ViolenceEvaluator, SexualEvaluator, HateUnfairnessEvaluator, ProtectedMaterialEvaluator, ContentSafetyEvaluator
import asyncio
from opentelemetry.baggage import set_baggage, get_baggage
from opentelemetry.context import attach
from featuremanagement import TargetingContext, FeatureManager
from azure.identity import DefaultAzureCredential

router = fastapi.APIRouter()
templates = Jinja2Templates(directory="api/templates")


# Accessors to get app state
def get_chat_client(request: Request) -> ChatCompletionsClient:
    return request.app.state.chat

def get_chat_model(request: Request) -> str:
    return request.app.state.chat_model

def get_search_index_namager(request: Request) -> SearchIndexManager:
    return request.app.state.search_index_manager

def get_feature_manager(request: Request) -> str:
    return request.app.state.feature_manager

class Message(pydantic.BaseModel):
    content: str
    role: str = "user"


class ChatRequest(pydantic.BaseModel):
    messages: list[Message]
    prompt_override: str = None
    sessionState: dict = {}

@router.get("/test/hello")
async def test():
    return "helloworld"

@router.get("/", response_class=HTMLResponse)
async def index_name(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/chat/stream")
async def chat_stream_handler(
    chat_request: ChatRequest,
    chat_client: ChatCompletionsClient = Depends(get_chat_client),
    model_deployment_name: str = Depends(get_chat_model),
    search_index_manager: SearchIndexManager = Depends(get_search_index_namager),
    feature_manager: FeatureManager = Depends
) -> fastapi.responses.StreamingResponse:
    if chat_client is None:
        raise Exception("Chat client not initialized")

    async def response_stream():
        messages = [{"role": message.role, "content": message.content} for message in chat_request.messages]
        model_deployment_name = globals["chat_model"]
        feature_manager = globals["feature_manager"] 
        
        targeting_id = chat_request.sessionState.get('sessionId', str(uuid.uuid4()))
        attach(set_baggage("Microsoft.TargetingId", targeting_id))
        
        # figure out which prompty template to use
        prompt_template = "prompt.v1.prompty"
        if chat_request.prompt_override:
            prompt_template = chat_request.prompt_override
        elif feature_manager is not None:                       
            prompt_variant = feature_manager.get_variant("prompty_file") # replace this with prompt_asset
            if prompt_variant and prompt_variant.configuration: # TODO: check file exists
                prompt_template = prompt_variant.configuration
 
        prompt = PromptTemplate.from_prompty(pathlib.Path(__file__).parent.resolve() / prompt_template)
        prompt_messages = prompt.create_messages()

        chat_coroutine = await chat_client.complete(
            model=model_deployment_name, messages=prompt_messages + messages, stream=True
        )
        async for event in chat_coroutine:
            if event.choices:
                first_choice = event.choices[0]
                yield (
                    json.dumps(
                        {
                            "delta": {
                                "content": first_choice.delta.content,
                                "role": first_choice.delta.role,
                            }
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )

        prompt_messages = PromptTemplate.from_string('You are a helpful assistant').create_messages()
        # Use RAG model, only if we were provided index and we have found a context there.
        if search_index_manager is not None:
            context = await search_index_manager.search(chat_request)
            if context:
                prompt_messages = PromptTemplate.from_string(
                    'You are a helpful assistant that answers some questions '
                    'with the help of some context data.\n\nHere is '
                    'the context data:\n\n{{context}}').create_messages(data=dict(context=context))
                logger.info(f"{prompt_messages=}")
            else:
                logger.info("Unable to find the relevant information in the index for the request.")
        try:
            chat_coroutine = await chat_client.complete(
                model=model_deployment_name, messages=prompt_messages + messages, stream=True
            )
            async for event in chat_coroutine:
                if event.choices:
                    first_choice = event.choices[0]
                    yield (
                        json.dumps(
                            {
                                "delta": {
                                    "content": first_choice.delta.content,
                                    "role": first_choice.delta.role,
                                }
                            },
                            ensure_ascii=False,
                        )
                        + "\n"
                    )
        except BaseException as e:
            error_processed = False
            response = "<div class=\"error\">Error: {}</div>"
            try:
                if '(content_filter)' in e.args[0]:
                    rai_dict = e.response.json()['error']['innererror']['content_filter_result']
                    errors = []
                    for k, v in rai_dict.items():
                        if v['filtered']:
                            if 'severity' in v:
                                errors.append(f"{k}, severity: {v['severity']}")
                            else:
                                errors.append(k)
                    error_text = f"We have found the next safety issues in the response: {', '.join(errors)}"
                    logger.error(error_text)
                    response = response.format(error_text)
                    error_processed = True
            except BaseException:
                pass
            if not error_processed:
                error_text = str(e)
                logger.error(error_text)
                response = response.format(error_text)
            yield (
                json.dumps(
                    {
                        "delta": {
                            "content": response,
                            "role": "agent",
                        }
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    return fastapi.responses.StreamingResponse(response_stream())


def get_targeting_context() -> TargetingContext:
    return TargetingContext(user_id=get_baggage("Microsoft.TargetingId"))

# @router.post("/chat")
# async def chat_nostream_handler(
#     chat_request: ChatRequest,
#     request: Request
# ):
#     chat_client = globals["chat"]
#     if chat_client is None:
#         raise Exception("Chat client not initialized")
   
#     messages = [{"role": message.role, "content": message.content} for message in chat_request.messages]
#     model_deployment_name = globals["chat_model"]
#     feature_manager = globals["feature_manager"] 

#     targeting_id = chat_request.sessionState.get('sessionId', str(uuid.uuid4()))
#     attach(set_baggage("Microsoft.TargetingId", targeting_id))
    
#     # figure out which prompty template to use (replace file to API)
#     variant = "none"
#     if chat_request.prompt_override:
#         prompt = PromptTemplate.from_prompty(pathlib.Path(__file__).parent.resolve() / chat_request.prompt_override)
#         variant = chat_request.prompt_override
#     else:                       
#         prompt_variant = feature_manager.get_variant("prompty_file") # replace this with prompt_asset
#         if prompt_variant and prompt_variant.configuration:
#             prompt = PromptTemplate.from_prompty(pathlib.Path(__file__).parent.resolve() / prompt_variant.configuration)
#             variant = prompt_variant.name
#         else:
#             prompt = globals["prompt"]

#     prompt_messages = prompt.create_messages()

#     try:
#         response = await chat_client.complete(
#             model=model_deployment_name, messages=prompt_messages + messages, stream=False
#         )
#         track_event("RequestMade", targeting_id)
#         answer = response.choices[0].message.content
#     except Exception as e:
#         error = {"Error": str(e)}
#         track_event("ErrorLLM", targeting_id, error)       
#         return { "answer": str(e), "variant": variant }    


    # conversation = {}

    # # initialize the evaluation client
    # # optional parameter to configure sampling
    # eval_client = await project.evaluation.get_evaluation_client(sampling_config=0.1)

    # eval_config = {
    #     # Required: built-in or custom evaluators
    #     "evaluators" : ["fluency", "content-safety"],
    #     # Optional: properties to log with the evaluation results
    #     "additional_metadata": {
    #         "prompt-variant": variant,
    #         "targeting-id": targeting_id
    #     }
    # }
    
    # # submit remote evaluation request, results will be sent to app insights
    # eval_request = await eval_client.submit_request(conversation, eval_config)
    
    # eval_sampling = feature_manager.get_variant("eval_sampling", targeting_id)
    # if eval_sampling and eval_sampling.configuration == True:
    #     eval_input = { "conversation": { "messages": messages } }
    # project = globals["project"]
   
    # asyncio.create_task(run_evals(eval_input, targeting_id, project.scope, DefaultAzureCredential()))
    
    return { "answer": answer, "variant": variant }
    

async def run_evals(eval_input, targeting_id, ai_project_scope, credential):
    run_eval(FluencyEvaluator, eval_input, targeting_id)
    run_eval(RelevanceEvaluator, eval_input, targeting_id)
    run_eval(CoherenceEvaluator, eval_input, targeting_id)

    run_safety_eval(ViolenceEvaluator, eval_input, targeting_id, ai_project_scope, credential)
    run_safety_eval(SexualEvaluator, eval_input, targeting_id, ai_project_scope, credential)
    run_safety_eval(HateUnfairnessEvaluator, eval_input, targeting_id, ai_project_scope, credential)
    run_safety_eval(ProtectedMaterialEvaluator, eval_input, targeting_id, ai_project_scope, credential)
    run_safety_eval(ContentSafetyEvaluator, eval_input, targeting_id, ai_project_scope, credential)

def run_safety_eval(evaluator, eval_input, targeting_id, ai_project_scope, credential):
    eval = evaluator(credential=credential, azure_ai_project=ai_project_scope)
    score = eval(**eval_input)
    score.update({"evaluator_id": eval.id})
    track_event("gen.ai." + type(eval).__name__, targeting_id, score)

def run_eval(evaluator, eval_input, targeting_id):
    eval = evaluator(globals["model_config"])
    score = eval(**eval_input)
    score.update({"evaluator_id": evaluator.id})
    track_event("gen.ai." + evaluator.__name__, targeting_id, score)