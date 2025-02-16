from azure.ai.projects import AIProjectClient 
from azure.identity import DefaultAzureCredential 
from azure.ai.projects.models import ( 
    ApplicationInsightsConfiguration,
    EvaluatorConfiguration,
    EvaluationSchedule,
    RecurrenceTrigger,
)
from azure.ai.evaluation import CoherenceEvaluator 

import os
from dotenv import load_dotenv

load_dotenv()

# Name of your online evaluation schedule
SAMPLE_NAME = "online_eval_name"

# Connection string to your Azure AI Foundry project
# Currently, it should be in the format "<HostName>;<AzureSubscriptionId>;<ResourceGroup>;<HubName>"
PROJECT_CONNECTION_STRING = os.getenv("AZURE_AIPROJECT_CONNECTION_STRING")

ai_services_connection = os.getenv("AZURE_AI_CONNECTION_NAME")
ai_project_user_identity_client_id = os.getenv("AZURE_AIPROJECT_USER_IDENTITY_CLIENT_ID")

# Your Application Insights resource ID
APPLICATION_INSIGHTS_RESOURCE_ID =  os.getenv("APPLICATION_INSIGHTS_RESOURCE_ID")

# Kusto Query Language (KQL) query to query data from Application Insights resource
# This query is compatible with data logged by the Azure AI Inferencing Tracing SDK (linked in documentation)
# You can modify it depending on your data schema
# The KQL query must output these required columns: operation_ID, operation_ParentID, and gen_ai_response_id
# You can choose which other columns to output as required by the evaluators you are using
KUSTO_QUERY = "let gen_ai_spans=(dependencies | where isnotnull(customDimensions[\"gen_ai.system\"]) | extend response_id = tostring(customDimensions[\"gen_ai.response.id\"]) | project id, operation_Id, operation_ParentId, timestamp, response_id); let gen_ai_events=(traces | where message in (\"gen_ai.choice\", \"gen_ai.user.message\", \"gen_ai.system.message\") or tostring(customDimensions[\"event.name\"]) in (\"gen_ai.choice\", \"gen_ai.user.message\", \"gen_ai.system.message\") | project id= operation_ParentId, operation_Id, operation_ParentId, user_input = iff(message == \"gen_ai.user.message\" or tostring(customDimensions[\"event.name\"]) == \"gen_ai.user.message\", parse_json(iff(message == \"gen_ai.user.message\", tostring(customDimensions[\"gen_ai.event.content\"]), message)).content, \"\"), system = iff(message == \"gen_ai.system.message\" or tostring(customDimensions[\"event.name\"]) == \"gen_ai.system.message\", parse_json(iff(message == \"gen_ai.system.message\", tostring(customDimensions[\"gen_ai.event.content\"]), message)).content, \"\"), llm_response = iff(message == \"gen_ai.choice\", parse_json(tostring(parse_json(tostring(customDimensions[\"gen_ai.event.content\"])).message)).content, iff(tostring(customDimensions[\"event.name\"]) == \"gen_ai.choice\", parse_json(parse_json(message).message).content, \"\")) | summarize operation_ParentId = any(operation_ParentId), Input = maxif(user_input, user_input != \"\"), System = maxif(system, system != \"\"), Output = maxif(llm_response, llm_response != \"\") by operation_Id, id); gen_ai_spans | join kind=inner (gen_ai_events) on id, operation_Id | project Input, System, Output, operation_Id, operation_ParentId, gen_ai_response_id = response_id"

# Connect to your Azure AI Foundry Project
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=PROJECT_CONNECTION_STRING
)

# Connect to your Application Insights resource 
app_insights_config = ApplicationInsightsConfiguration(
    resource_id=APPLICATION_INSIGHTS_RESOURCE_ID,
    query=KUSTO_QUERY
)

# Connect to your Azure OpenAI Service resource. You must use a GPT model deployment for this example.
deployment_name = "gpt-4o-mini"
api_version = "2024-08-01-preview"

# This is your Azure OpenAI Service connection name, which can be found in your Azure AI Foundry project under the 'Models + Endpoints' tab.
default_connection = project_client.connections._get_connection(ai_services_connection)

model_config = {
    "azure_deployment": deployment_name,
    "api_version": api_version,
    "type": "azure_openai",
    "azure_endpoint": default_connection.properties["target"]
}

# RelevanceEvaluator
# id for each evaluator can be found in your Azure AI Foundry registry - please see documentation for more information
# init_params is the configuration for the model to use to perform the evaluation
# data_mapping is used to map the output columns of your query to the names required by the evaluator
# relevance_evaluator_config = EvaluatorConfiguration(
#     id="azureml://registries/azureml-staging/models/Relevance-Evaluator/versions/4",
#     init_params={"model_config": model_config},
#     data_mapping={"query": "${data.Input}", "response": "${data.Output}"}
# )

# CoherenceEvaluator
coherence_evaluator_config = EvaluatorConfiguration(
    id=CoherenceEvaluator.id,
    init_params={"model_config": model_config},
    data_mapping={"query": "${data.Input}", "response": "${data.Output}"}
)

# Frequency to run the schedule
recurrence_trigger = RecurrenceTrigger(frequency="hour", interval=1)

# Dictionary of evaluators
evaluators = {
    #"relevance": relevance_evaluator_config,
    "coherence" : coherence_evaluator_config
}

name = SAMPLE_NAME
description = f"{SAMPLE_NAME} description"
# AzureMSIClientId is the clientID of the User-assigned managed identity created during set-up - see documentation for how to find it
# https://ms.portal.azure.com/#view/Microsoft_AAD_IAM/ManagedAppMenuBlade/~/Overview/objectId/83c77e9f-bbc1-41a6-8956-4e36e992336f/appId/4610a06d-56a0-47ab-aeb6-cf95bc662052
properties = {"AzureMSIClientId": ai_project_user_identity_client_id, "Environment": "azureml://registries/azureml/environments/azureml-evaluations-built-in/versions/14"}

# Configure the online evaluation schedule
evaluation_schedule = EvaluationSchedule(
    data=app_insights_config,
    evaluators=evaluators,
    trigger=recurrence_trigger,
    description=description,
    properties=properties)

# Create the online evaluation schedule 
created_evaluation_schedule = project_client.evaluations.create_or_replace_schedule(name, evaluation_schedule)
print(f"Successfully submitted the online evaluation schedule creation request - {created_evaluation_schedule.name}, currently in {created_evaluation_schedule.provisioning_state} state.")

# Check schedule
#get_evaluation_schedule = project_client.evaluations.get_schedule(name)

# Disable schedule
#project_client.evaluations.disable_schedule(name)