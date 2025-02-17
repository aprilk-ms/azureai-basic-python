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

from opentelemetry.baggage import get_baggage
from azure.ai.evaluation import CoherenceEvaluator, FluencyEvaluator, RelevanceEvaluator, ViolenceEvaluator, SexualEvaluator, HateUnfairnessEvaluator, ProtectedMaterialEvaluator, ContentSafetyEvaluator
import asyncio
from opentelemetry.baggage import set_baggage, get_baggage
from opentelemetry.context import attach
from featuremanagement import TargetingContext

router = fastapi.APIRouter()
templates = Jinja2Templates(directory="api/templates")


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
        
        # figure out which prompty template to use (replace file to API)
        if chat_request.prompt_override:
            prompt = PromptTemplate.from_prompty(pathlib.Path(__file__).parent.resolve() / chat_request.prompt_override)
        else:                       
            prompt_variant = feature_manager.get_variant("prompty_file") # replace this with prompt_asset
            if prompt_variant and prompt_variant.configuration:
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


def get_targeting_context():
    return TargetingContext(user_id=get_baggage("Microsoft.TargetingId"))

@router.post("/chat")
async def chat_nostream_handler(
    chat_request: ChatRequest,
    request: Request
):
    chat_client = globals["chat"]
    if chat_client is None:
        raise Exception("Chat client not initialized")
   
    messages = [{"role": message.role, "content": message.content} for message in chat_request.messages]
    model_deployment_name = globals["chat_model"]
    feature_manager = globals["feature_manager"] 

    targeting_id = chat_request.sessionState['sessionId'] or str(uuid.uuid4())
    attach(set_baggage("Microsoft.TargetingId", targeting_id))
    
    # figure out which prompty template to use (replace file to API)
    variant = "none"
    if chat_request.prompt_override:
        prompt = PromptTemplate.from_prompty(pathlib.Path(__file__).parent.resolve() / chat_request.prompt_override)
        variant = chat_request.prompt_override
    else:                       
        prompt_variant = feature_manager.get_variant("prompty_file") # replace this with prompt_asset
        if prompt_variant and prompt_variant.configuration:
            prompt = PromptTemplate.from_prompty(pathlib.Path(__file__).parent.resolve() / prompt_variant.configuration)
            variant = prompt_variant.name
        else:
            prompt = globals["prompt"]

    prompt_messages = prompt.create_messages()

    try:
        response = await chat_client.complete(
            model=model_deployment_name, messages=prompt_messages + messages, stream=False
        )
        track_event("RequestMade", targeting_id)
    except Exception as e:
        error = {"Error": str(e)}
        track_event("ErrorLLM", targeting_id, error)
        
    answer = response.choices[0].message.content

    # eval_sampling = feature_manager.get_variant("eval_sampling", targeting_id)
    # if eval_sampling and eval_sampling.configuration == True:
    # eval_input = { "conversation": { "messages": messages } }
    # project = globals["project"]
    #asyncio.create_task(run_evals(eval_input, targeting_id, project.scope, DefaultAzureCredential()))
   
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