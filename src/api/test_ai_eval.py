from src.api.main import create_app
from fastapi.testclient import TestClient
import json
import os
import uuid
from azure.ai.evaluation import evaluate, FluencyEvaluator, RelevanceEvaluator, GroundednessEvaluator, SimilarityEvaluator, F1ScoreEvaluator, RougeScoreEvaluator, CoherenceEvaluator, RougeType

def get_model_config():
    return {
        "type": "azure_openai",
        "azure_deployment": "gpt-4o-mini",
        "api_version": "2024-08-01-preview",
        "azure_endpoint": "https://aoai-e6pnryr2q3qeg.openai.azure.com/"
    }

def get_eval_data_set():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "data/eval-data-set-large.jsonl")
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


def test_simulate_traffic():
    app = create_app()
    with TestClient(app) as client:
        for i in range(20):
            for data in get_eval_data_set():
                query = data["query"]
                response = client.post("/chat", json={
                    "messages": [
                        {"role": "user", "content": query},
                    ]
                })            
                answer = ""
                for line in response.text.splitlines():
                    answer += json.loads(line).get("delta", {}).get("content", "") or ""
                print(answer)


def test_simulate_traffic_nostream():
    app = create_app()
    with TestClient(app) as client:
        for i in range(20):
            for data in get_eval_data_set():
                query = data["query"]
                response = client.post("/chat", json={
                    "messages": [
                        {"role": "user", "content": query},
                    ]
                })            
                print(response.text)

def test_generate_ai_eval_input():
    app = create_app()
    with TestClient(app) as client:
        evalInput = ""
        for variant in get_prompt_template_variants():
            variant_name = variant["name"]
            prompty_file = variant["configuration_value"]
            for data in get_eval_data_set():
                query = data["query"]
                response = client.post("/chat", json={
                    "messages": [
                        {"role": "user", "content": query},
                    ],
                    "prompt_override": prompty_file
                })

                answer = response.text            
                description = {"context": {"system-prompt": prompty_file}}
                input = {
                    "id": str(uuid.uuid4()),
                    "description": json.dumps(description),
                    "query": data["query"],
                    "response": answer,
                    "ground_truth": data["ground-truth"],
                    "context": "prompty template variant: " + variant_name
                },
                evalInput += json.dumps(input) + "\n"

    output_path = "evaluation-input.jsonl"
    with open(output_path, "w") as file:
        file.write(evalInput)

def test_run_ai_eval():
    model_config = get_model_config()
    output_path = "evaluation-results.json"
    result = evaluate(
        data="evaluation-input.jsonl",
        evaluators={
            "groundedness": GroundednessEvaluator(model_config),
            "relevance": RelevanceEvaluator(model_config),
            "fluency": FluencyEvaluator(model_config),
            "coherence": CoherenceEvaluator(model_config),
            "similarity": SimilarityEvaluator(model_config),
            "f1score": F1ScoreEvaluator(),
            "rougescore": RougeScoreEvaluator(RougeType.ROUGE_L),
        },
        evaluator_config={
            "default": {
                "column_mapping": {
                    "query": "${data.query}",
                    "context": "${data.context}",
                    "response": "${data.response}",
                    "ground_truth": "${data.ground_truth}",
                } 
            }
        },
        output_path=output_path
    )

    with open(output_path, "w") as file:
        json.dump(result, file, indent=4)