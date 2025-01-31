from azure.ai.projects import AIProjectClient 
from azure.identity import DefaultAzureCredential 

name = "online_eval_name"

# Connection string to your Azure AI Foundry project
# Currently, it should be in the format "<HostName>;<AzureSubscriptionId>;<ResourceGroup>;<HubName>"
PROJECT_CONNECTION_STRING = "eastus2.api.azureml.ms;80d2c6c6-fa64-4ab1-8aa5-4e118c6b16ce;rg-aprilk-azure-ai-basic-01a;ai-project-e6pnryr2q3qeg"

# Connect to your Azure AI Foundry Project
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=PROJECT_CONNECTION_STRING
)

get_evaluation_schedule = project_client.evaluations.get_schedule(name)

print(get_evaluation_schedule)