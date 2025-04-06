targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name of the the environment which is used to generate a short unique hash used in all resources.')
param environmentName string

@minLength(1)
@description('Location for all resources')
// Look for desired models on the availability table:
// https://learn.microsoft.com/azure/ai-services/openai/concepts/models#global-standard-model-availability
@allowed([
  'australiaeast'
  'brazilsouth'
  'canadaeast'
  'eastus'
  'eastus2'
  'francecentral'
  'germanywestcentral'
  'japaneast'
  'koreacentral'
  'northcentralus'
  'norwayeast'
  'polandcentral'
  'spaincentral'
  'southafricanorth'
  'southcentralus'
  'southindia'
  'swedencentral'
  'switzerlandnorth'
  'uksouth'
  'westeurope'
  'westus'
  'westus3'
])
@metadata({
  azd: {
    type: 'location'
  }
})
param location string

@description('Use this parameter to use an existing AI project connection string')
param aiExistingProjectConnectionString string = ''
@description('The Azure resource group where new resources will be deployed')
param resourceGroupName string = ''
@description('The Azure AI Foundry Hub resource name. If ommited will be generated')
param aiHubName string = ''
@description('The Azure AI Foundry project name. If ommited will be generated')
param aiProjectName string = ''
@description('The application insights resource name. If ommited will be generated')
param applicationInsightsName string = ''
@description('The AI Services resource name. If ommited will be generated')
param aiServicesName string = ''
@description('The AI Services connection name. If ommited will use a default value')
param aiServicesConnectionName string = ''
@description('The AI Services content safety connection name. If ommited will use a default value')
param aiServicesContentSafetyConnectionName string = ''
@description('The Azure Key Vault resource name. If ommited will be generated')
param keyVaultName string = ''
@description('The Azure Search resource name. If ommited will be generated')
param searchServiceName string = ''
@description('The Azure Search connection name. If ommited will use a default value')
param searchConnectionName string = ''
@description('The search index name')
param aiSearchIndexName string = ''
@description('The Azure Storage Account resource name. If ommited will be generated')
param storageAccountName string = ''
@description('The log analytics workspace name. If ommited will be generated')
param logAnalyticsWorkspaceName string = ''
@description('Random seed to be used during generation of new resources suffixes.')
param seed string = newGuid()

// Chat completion model
@description('Format of the chat model to deploy')
@allowed(['Microsoft', 'OpenAI'])
param chatModelFormat string = 'OpenAI'

@description('Name of the chat model to deploy')
param chatModelName string = 'gpt-4o-mini'
@description('Name of the model deployment')
param chatDeploymentName string = 'gpt-4o-mini'

@description('Version of the chat model to deploy')
// See version availability in this table:
// https://learn.microsoft.com/azure/ai-services/openai/concepts/models#global-standard-model-availability
param chatModelVersion string = '2024-07-18'

@description('Sku of the chat deployment')
param chatDeploymentSku string = 'GlobalStandard'

@description('Capacity of the chat deployment')
// You can increase this, but capacity is limited per model/region, so you will get errors if you go over
// https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits
param chatDeploymentCapacity int = 30

// Embedding model
@description('Format of the embedding model to deploy')
@allowed(['Microsoft', 'OpenAI'])
param embedModelFormat string = 'OpenAI'

@description('Name of the embedding model to deploy')
param embedModelName string = 'text-embedding-3-small'
@description('Name of the embedding model deployment')
param embeddingDeploymentName string = 'text-embedding-3-small'
@description('Embedding model dimensionality')
param embeddingDeploymentDimensions string = '100'

@description('Version of the embedding model to deploy')
// See version availability in this table:
// https://learn.microsoft.com/azure/ai-services/openai/concepts/models#embeddings-models
param embedModelVersion string = '1'

@description('Sku of the embeddings model deployment')
param embedDeploymentSku string = 'Standard'

@description('Capacity of the embedding deployment')
// You can increase this, but capacity is limited per model/region, so you will get errors if you go over
// https://learn.microsoft.com/azure/ai-services/openai/quotas-limits
param embedDeploymentCapacity int = 30

param useApplicationInsights bool = true
@description('Use the RAG search')
param useSearchService bool = false

var abbrs = loadJsonContent('./abbreviations.json')
var resourceToken = toLower(uniqueString(subscription().id, environmentName, location, seed))
var projectName = !empty(aiProjectName) ? aiProjectName : 'ai-project-${resourceToken}'
var tags = { 'azd-env-name': environmentName }

var aiChatModel = [
  {
    name: chatDeploymentName
    model: {
      format: chatModelFormat
      name: chatModelName
      version: chatModelVersion
    }
    sku: {
      name: chatDeploymentSku
      capacity: chatDeploymentCapacity
    }
  }
]
var aiEmbeddingModel = [ 
  {
    name: embeddingDeploymentName
    model: {
      format: embedModelFormat
      name: embedModelName
      version: embedModelVersion
    }
    sku: {
      name: embedDeploymentSku
      capacity: embedDeploymentCapacity
    }
  }
]

var aiDeployments = concat(
  aiChatModel,
  useSearchService ? aiEmbeddingModel : [])

// Organize resources in a resource group
resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: !empty(resourceGroupName) ? resourceGroupName : '${abbrs.resourcesResourceGroups}${environmentName}'
  location: location
  tags: tags
}

var logAnalyticsWorkspaceResolvedName = !useApplicationInsights
  ? ''
  : !empty(logAnalyticsWorkspaceName)
      ? logAnalyticsWorkspaceName
      : '${abbrs.operationalInsightsWorkspaces}${resourceToken}'


var resolvedSearchServiceName = !useSearchService
  ? ''
  : !empty(searchServiceName) ? searchServiceName : '${abbrs.searchSearchServices}${resourceToken}'

module ai 'core/host/ai-environment.bicep' = if (empty(aiExistingProjectConnectionString)) {
  name: 'ai'
  scope: rg
  params: {
    location: location
    tags: tags
    hubName: !empty(aiHubName) ? aiHubName : 'ai-hub-${resourceToken}'
    projectName: projectName
    keyVaultName: !empty(keyVaultName) ? keyVaultName : '${abbrs.keyVaultVaults}${resourceToken}'
    storageAccountName: !empty(storageAccountName)
      ? storageAccountName
      : '${abbrs.storageStorageAccounts}${resourceToken}'
    aiServicesName: !empty(aiServicesName) ? aiServicesName : 'aoai-${resourceToken}'
    aiServicesConnectionName: !empty(aiServicesConnectionName) ? aiServicesConnectionName : 'aoai-${resourceToken}'
    aiServicesContentSafetyConnectionName: !empty(aiServicesContentSafetyConnectionName)
      ? aiServicesContentSafetyConnectionName
      : 'aoai-content-safety-connection'
    aiServiceModelDeployments: aiDeployments
    logAnalyticsName: logAnalyticsWorkspaceResolvedName
    applicationInsightsName: !useApplicationInsights
      ? ''
      : !empty(applicationInsightsName) ? applicationInsightsName : '${abbrs.insightsComponents}${resourceToken}'
    searchServiceName: resolvedSearchServiceName
    searchConnectionName: !useSearchService
      ? ''
      : !empty(searchConnectionName) ? searchConnectionName : 'search-service-connection'
    identityName: '${abbrs.managedIdentityUserAssignedIdentities}ai-project-${resourceToken}'
  }
}

var searchServiceEndpoint = !useSearchService
      ? ''
      : ai.outputs.searchServiceEndpoint

// If bringing an existing AI project, set up the log analytics workspace here
module logAnalytics 'core/monitor/loganalytics.bicep' = if (!empty(aiExistingProjectConnectionString)) {
  name: 'logAnalytics'
  scope: rg
  params: {
    location: location
    tags: tags
    name: logAnalyticsWorkspaceResolvedName
  }
}

var hostName = empty(aiExistingProjectConnectionString) && !empty(ai.outputs.discoveryUrl) && contains(ai.outputs.discoveryUrl, '/') ? split(ai.outputs.discoveryUrl, '/')[2] : ''
var projectConnectionString = empty(hostName)
  ? aiExistingProjectConnectionString
  : '${hostName};${subscription().subscriptionId};${rg.name};${projectName}'


//Container apps host and api
// Container apps host
module containerApps 'core/host/container-apps.bicep' = {
  name: 'container-apps'
  scope: rg
  params: {
    name: 'app'
    location: location
    tags: tags
    containerAppsEnvironmentName: 'containerapps-env-${resourceToken}'
    logAnalyticsWorkspaceName: empty(aiExistingProjectConnectionString)
      ? ai.outputs.logAnalyticsWorkspaceName
      : logAnalytics.outputs.name
  }
}


// API app
module api 'api.bicep' = {
  name: 'api'
  scope: rg
  params: {
    name: 'ca-api-${resourceToken}'
    location: location
    tags: tags
    identityName: '${abbrs.managedIdentityUserAssignedIdentities}api-${resourceToken}'
    containerAppsEnvironmentName: containerApps.outputs.environmentName
    projectConnectionString: projectConnectionString
    chatDeploymentName: chatDeploymentName
    embeddingDeploymentName: embeddingDeploymentName
    embeddingDeploymentDimensions: embeddingDeploymentDimensions
    aiSearchIndexName: aiSearchIndexName
    searchServiceEndpoint: searchServiceEndpoint
    projectName: projectName
  }
}


module userAcrRolePush 'core/security/role.bicep' = {
  name: 'user-role-acr-push'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '8311e382-0749-4cb8-b61a-304f252e45ec'
  }
}

module userAcrRolePull 'core/security/role.bicep' = {
  name: 'user-role-acr-pull'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '7f951dda-4ed3-4680-a7ca-43fe172d538d'
  }
}

module userRoleDataScientist 'core/security/role.bicep' = {
  name: 'user-role-data-scientist'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: 'f6c7c914-8db3-469d-8ca1-694a8f32e121'
  }
}

module userRoleSecretsReader 'core/security/role.bicep' = {
  name: 'user-role-secrets-reader'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: 'ea01e6af-a1c1-4350-9563-ad00f8c72ec5'
  }
}

module userRoleAzureAIDeveloper 'core/security/role.bicep' = {
  name: 'user-role-azureai-developer'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '64702f94-c441-49e6-a78b-ef80e0188fee'
  }
}

module backendRoleAzureAIDeveloperRG 'core/security/role.bicep' = {
  name: 'backend-role-azureai-developer-rg'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '64702f94-c441-49e6-a78b-ef80e0188fee'
  }
}

var resolvedApplicationInsightsName = !useApplicationInsights || !empty(aiExistingProjectConnectionString)
  ? ''
  : !empty(applicationInsightsName) ? applicationInsightsName : '${abbrs.insightsComponents}${resourceToken}'

module monitoringMetricsContribuitorRoleAzureAIDeveloperRG 'core/security/appinsights-access.bicep' = if (!empty(resolvedApplicationInsightsName)) {
  name: 'monitoringmetricscontributor-role-azureai-developer-rg'
  scope: rg
  params: {
    appInsightsName: resolvedApplicationInsightsName
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
  }
}

resource existingProjectRG 'Microsoft.Resources/resourceGroups@2021-04-01' existing = if (!empty(aiExistingProjectConnectionString) && contains(aiExistingProjectConnectionString, ';')) {
  name: split(aiExistingProjectConnectionString, ';')[2]
}

module userRoleAzureAIDeveloperBackendExistingProjectRG 'core/security/role.bicep' = if (!empty(aiExistingProjectConnectionString)) {
  name: 'backend-role-azureai-developer-existing-project-rg'
  scope: existingProjectRG
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '64702f94-c441-49e6-a78b-ef80e0188fee'
  }
}

module backendRoleSearchIndexDataContributorRG 'core/security/role.bicep' = if (useSearchService) {
  name: 'backend-role-azure-index-data-contributor-rg'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '8ebe5a00-799e-43f5-93ac-243d3dce84a7'
  }
}

module backendRoleSearchIndexDataReaderRG 'core/security/role.bicep' = if (useSearchService) {
  name: 'backend-role-azure-index-data-reader-rg'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '1407120a-92aa-4202-b7e9-c0e197c71c8f'
  }
}

module backendRoleSearchServiceContributorRG 'core/security/role.bicep' = if (useSearchService) {
  name: 'backend-role-azure-search-service-contributor-rg'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '7ca78c08-252a-4471-8644-bb5ff32d4ba0'
  }
}

module userRoleSearchIndexDataContributorRG 'core/security/role.bicep' = if (useSearchService) {
  name: 'user-role-azure-index-data-contributor-rg'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '8ebe5a00-799e-43f5-93ac-243d3dce84a7'
  }
}

module userRoleSearchIndexDataReaderRG 'core/security/role.bicep' = if (useSearchService) {
  name: 'user-role-azure-index-data-reader-rg'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '1407120a-92aa-4202-b7e9-c0e197c71c8f'
  }
}

module userRoleSearchServiceContributorRG 'core/security/role.bicep' = if (useSearchService) {
  name: 'user-role-azure-search-service-contributor-rg'
  scope: rg
  params: {
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    roleDefinitionId: '7ca78c08-252a-4471-8644-bb5ff32d4ba0'
  }
}

// Provision App Configuration
module configStore 'core/config/configstore.bicep' = {
  name: 'configstore'
  scope: rg
  params: {
    location: location
    name: '${abbrs.appConfigurationStores}${resourceToken}'
    tags: tags
    principalId: api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
    appInsightsName: ai.outputs.applicationInsightsName
  }
}

module experimentWorkspace 'core/config/experimentworkspace.bicep' = {
  name: 'expWorkspace'
  scope: rg
  params: {
    name: 'exp${substring(resourceToken, 0, 10)}'
    location: 'eastus2'
    tags: tags
    userPrincipalId: principalId
    createRoleForUser: true
    pipelineServicePrincipalId: principalId
    logAnalyticsWorkspaceName: ai.outputs.logAnalyticsWorkspaceName
    storageAccountName: ai.outputs.storageAccountName
    identityName: '${abbrs.managedIdentityUserAssignedIdentities}exp-${resourceToken}'
  }
}

// Allow experiment workspace read access to storage
module logAnalyticsExpAccess 'core/security/role.bicep' = {
  scope: rg
  name: 'storage-account-exp-role'
  params: {
    principalId: experimentWorkspace.outputs.expWorkspaceIdentityPrincipalId
    roleDefinitionId: '2a2b9908-6ea1-4ae2-8e65-a410df84e7d1' // Storage Blob Data Reader
    principalType: 'ServicePrincipal'
  }
}

// Allow experiment workspace read access to log analytics workspace
module storageAccountExpAccess 'core/security/role.bicep' = {
  scope: rg
  name: 'log-analytics-exp-role'
  params: {
    principalId: experimentWorkspace.outputs.expWorkspaceIdentityPrincipalId
    roleDefinitionId: '73c42c96-874c-492b-b04d-ab87d138a893' // Log Analytics Reader
    principalType: 'ServicePrincipal'
  }
}

// Allow pipeline access to Log Analytics workspace
// module logAnalyticsRole 'core/security/role.bicep' = if (!createRoleForUser) {
//   scope: resourceGroup
//   name: 'log-analytics-role-pipeline'
//   params: {
//     principalId: principalId
//     roleDefinitionId: '92aaf0da-9dab-42b6-94a3-d43ce8d16293' // Log Analytics Contributor
//     principalType: 'ServicePrincipal'
//   }
// }

module dataExportRule 'core/monitor/dataexports.bicep' = {
  name: 'loganalytics-dataexportrule'
  scope: rg
  params: {
    name: 'dataexportrule'
    logAnalyticsWorkspaceName: ai.outputs.logAnalyticsWorkspaceName
    storageAccountName: ai.outputs.storageAccountName
    tables: [
      'AppEvents'
      'AppEvents_CL'
    ]
  }
}

// Provision summary rules aggregating data for experiment workspace
var ruleDefinitions = loadYamlContent('./la-summary-rules.yaml')
module summaryRules 'core/monitor/summaryrule.bicep' =  [ for (rule, i) in ruleDefinitions.summaryRules:  {
  name: 'loganalytics-summaryrule-${i}'
  scope: rg
  params: {
    location: location
    logAnalyticsWorkspaceName: ai.outputs.logAnalyticsWorkspaceName
    summaryRuleName: rule.name
    description: rule.description
    query: rule.query
    binSize: rule.binSize // see choices at https://aka.ms/LogsSummaryRule#create-or-update-a-summary-rule
    destinationTable: rule.destinationTable
  }
} ]

output AZURE_RESOURCE_GROUP string = rg.name

// Outputs required for local development server
output AZURE_TENANT_ID string = tenant().tenantId
output AZURE_AIPROJECT_CONNECTION_STRING string = projectConnectionString
output AZURE_AI_CHAT_DEPLOYMENT_NAME string = chatDeploymentName
output AZURE_AI_EMBED_DEPLOYMENT_NAME string = embeddingDeploymentName
output AZURE_AI_SEARCH_INDEX_NAME string = aiSearchIndexName
output AZURE_AI_SEARCH_ENDPOINT string = searchServiceEndpoint
output AZURE_AI_EMBED_DIMENSIONS string = embeddingDeploymentDimensions
output AZURE_AIPROJECT_USER_IDENTITY_PRINCIPAL_ID string = ai.outputs.ProjectUserIdentityPrincipalId
output AZURE_AI_SERVICE_ENDPOINT string = ai.outputs.aiServiceEndpoint

// Outputs required by azd for ACA
output AZURE_CONTAINER_ENVIRONMENT_NAME string = containerApps.outputs.environmentName
output SERVICE_API_IDENTITY_PRINCIPAL_ID string = api.outputs.SERVICE_API_IDENTITY_PRINCIPAL_ID
output SERVICE_API_NAME string = api.outputs.SERVICE_API_NAME
output SERVICE_API_URI string = api.outputs.SERVICE_API_URI
output SERVICE_API_IMAGE_NAME string = api.outputs.SERVICE_API_IMAGE_NAME
output SERVICE_API_ENDPOINTS array = ['${api.outputs.SERVICE_API_URI}']

output APP_CONFIGURATION_ENDPOINT string = configStore.outputs.endpoint
output EXPERIMENT_WORKSPACE_ID string = experimentWorkspace.outputs.expWorkspaceId
output APPLICATIONINSIGHTS_CONNECTION_STRING string = ai.outputs.applicationInsightsConnectionString

