from src.api.main import create_app
from fastapi.testclient import TestClient
import json
import os
import uuid

from azure.ai.projects.aio import AIProjectClient
from azure.ai.evaluation import evaluate, FluencyEvaluator
from azure.identity import DefaultAzureCredential

def get_eval_data_set():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "data/eval-data-set.jsonl")
    with open(file_path) as file:
        dataSet = json.load(file)
    return dataSet

def get_prompt_template_variants():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../../.config/feature-flags.json")
    with open(file_path) as file:
        feature_flags = json.load(file)
    for feature_flag in feature_flags["feature_management"]["feature_flags"]:
        if feature_flag["id"] == "prompty_file":
            return feature_flag["variants"]


def test_generate_ai_eval_input():
    app = create_app()
    with TestClient(app) as client:
        evalInput = ""
        for variant in get_prompt_template_variants():
            variant_name = variant["name"]
            prompty_file = variant["configuration_value"]
            for data in get_eval_data_set():
                query = data["query"]
                response = client.post("/chat/stream", json={
                    "messages": [
                        {"role": "user", "content": query},
                    ],
                    "prompt_override": prompty_file
                })

                answer = ""
                for line in response.text.splitlines():
                    answer += json.loads(line).get("delta", {}).get("content", "") or ""
            
                description = {"context": {"prompt-template": prompty_file}}
                input = {
                    "id": str(uuid.uuid4()),
                    "description": json.dumps(description),
                    "query": data["query"],
                    "response": answer,
                    "ground_truth": data["ground-truth"],
                    "context": "prompty template variant: " + variant_name
                }
                evalInput += json.dumps(input) + "\n"

    output_path = "evaluation-input.jsonl"
    with open(output_path, "w") as file:
        file.write(evalInput)

    #credential = DefaultAzureCredential()
    # project_conn_str = os.environ["AZURE_AIPROJECT_CONNECTION_STRING"]
    # project = AIProjectClient.from_connection_string(
    #     credential=credential,
    #     conn_str=project_conn_str
    # )
    # default_connection = project.connections._get_connection(
    #     "aoai-e6pnryr2q3qeg_aoai"
    # )
    # deployment_name = "gpt-4o-mini"
    # api_version = "2024-08-01-preview"
    # model_config = {
    #     "azure_deployment": deployment_name,
    #     "api_version": api_version,
    #     "type": "azure_openai",
    #     "azure_endpoint": "https://aoai-e6pnryr2q3qeg.openai.azure.com/"
    # }
    # fluency_eval = FluencyEvaluator(model_config)
    # eval_result = evaluate(
    #     data=output_path,
    #     evaluators= {
    #         "FluencyEvaluator": fluency_eval
    #     },
    #     # column mapping
    #     evaluator_config={
    #         "groundedness": {
    #             "column_mapping": {
    #                 "query": "${data.queries}",
    #                 "context": "${data.context}",
    #                 "response": "${data.response}"
    #             } 
    #         }
    #     },
    #     # Optionally provide your Azure AI project information to track your evaluation results in your Azure AI project
    #     azure_ai_project = project,
    #     # Optionally provide an output path to dump a json of metric summary, row level data and metric and Azure AI project URL
    #     output_path="./eval-results.json"
    # )