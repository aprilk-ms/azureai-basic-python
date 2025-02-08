# Define the .env file path
$envFilePath = "src\.env"

# Clear the contents of the .env file
Set-Content -Path $envFilePath -Value ""

# Append new values to the .env file
$azureAiProjectConnectionString = azd env get-value AZURE_AIPROJECT_CONNECTION_STRING
$azureAiChatDeploymentName = azd env get-value AZURE_AI_CHAT_DEPLOYMENT_NAME
$azureTenantId = azd env get-value AZURE_TENANT_ID
$appInsightsResourceId = azd env get-value APPLICATION_INSIGHTS_RESOURCE_ID
$azureAiConnectionName = azd env get-value AZURE_AI_CONNECTION_NAME
$azureAiProjectUserIdentityClientId = azd env get-value AZURE_AIPROJECT_USER_IDENTITY_CLIENT_ID

Add-Content -Path $envFilePath -Value "AZURE_AIPROJECT_CONNECTION_STRING=$azureAiProjectConnectionString"
Add-Content -Path $envFilePath -Value "AZURE_AI_CHAT_DEPLOYMENT_NAME=$azureAiChatDeploymentName"
Add-Content -Path $envFilePath -Value "AZURE_TENANT_ID=$azureTenantId"
Add-Content -Path $envFilePath -Value "APPLICATION_INSIGHTS_RESOURCE_ID=$appInsightsResourceId"
Add-Content -Path $envFilePath -Value "AZURE_AI_CONNECTION_NAME=$azureAiConnectionName"
Add-Content -Path $envFilePath -Value "AZURE_AIPROJECT_USER_IDENTITY_CLIENT_ID=$azureAiProjectUserIdentityClientId"