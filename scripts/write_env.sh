#!/bin/bash

# Define the .env file path
ENV_FILE_PATH="src/.env"

# Clear the contents of the .env file
> $ENV_FILE_PATH

echo "AZURE_AIPROJECT_CONNECTION_STRING=$(azd env get-value AZURE_AIPROJECT_CONNECTION_STRING)" >> $ENV_FILE_PATH
echo "AZURE_AI_CHAT_DEPLOYMENT_NAME=$(azd env get-value AZURE_AI_CHAT_DEPLOYMENT_NAME)" >> $ENV_FILE_PATH
echo "AZURE_TENANT_ID=$(azd env get-value AZURE_TENANT_ID)" >> $ENV_FILE_PATH
echo "APPLICATION_INSIGHTS_RESOURCE_ID=$(azd env get-value APPLICATION_INSIGHTS_RESOURCE_ID)" >> $ENV_FILE_PATH
echo "AZURE_AI_CONNECTION_NAME=$(azd env get-value AZURE_AI_CONNECTION_NAME)" >> $ENV_FILE_PATH
echo "AZURE_AIPROJECT_USER_IDENTITY_CLIENT_ID=$(azd env get-value AZURE_AIPROJECT_USER_IDENTITY_CLIENT_ID)" >> $ENV_FILE_PATH
echo "AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true" >> $ENV_FILE_PATH