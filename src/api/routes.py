import json

import fastapi
import pydantic
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from featuremanagement.azuremonitor import track_event

import uuid
import pathlib
from azure.ai.inference.prompts import PromptTemplate

from .shared import globals
from azure.core.settings import settings 

from opentelemetry.baggage import get_baggage
from azure.ai.inference.aio import ChatCompletionsClient

settings.tracing_implementation = "opentelemetry" 
router = fastapi.APIRouter()
templates = Jinja2Templates(directory="api/templates")


class Message(pydantic.BaseModel):
    content: str
    role: str = "user"


class ChatRequest(pydantic.BaseModel):
    messages: list[Message]

@router.get("/test/hello")
async def test():
    return "helloworld"

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/chat/stream")
async def chat_stream_handler(
    chat_request: ChatRequest
) -> fastapi.responses.StreamingResponse:
    chat_client = globals["chat"]
    if chat_client is None:
        raise Exception("Chat client not initialized")

    async def response_stream():
        messages = [{"role": message.role, "content": message.content} for message in chat_request.messages]
        model_deployment_name = globals["chat_model"]
        feature_manager = globals["feature_manager"]

        targeting_id = get_baggage("Microsoft.TargetingId") or str(uuid.uuid4())

        # fetch prompt variant, if any
        prompt_variant = feature_manager.get_variant("prompty_file", targeting_id) # replace this with prompt_asset
        if prompt_variant and prompt_variant.configuration:
            # Replace this with prompt API
            prompt = PromptTemplate.from_prompty(pathlib.Path(__file__).parent.resolve() / prompt_variant.configuration)
        else:
            prompt = globals["prompt"]

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

    return fastapi.responses.StreamingResponse(response_stream())
