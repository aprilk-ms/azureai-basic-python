metadata description = 'Creates an experiment workspace'
param name string
param location string = resourceGroup().location
param tags object = {}
param userPrincipalId string
param createRoleForUser bool
param pipelineServicePrincipalId string
param logAnalyticsWorkspaceName string
param storageAccountName string
param identityName string

resource experimentMetricRoleDefinition 'Microsoft.Authorization/roleDefinitions@2022-04-01' existing = {
  name: '6188b7c9-7d01-4f99-a59f-c88b630326c0'
}

resource expIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: identityName
  location: location
}

// Noite: no intellisense during private preview period
#disable-next-line BCP081
resource expWorkspace 'Microsoft.Experimentation/experimentWorkspaces@2024-11-30-preview' = {
  name: name
  location: location
  tags: tags
  kind: 'Regular'
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: { '${expIdentity.id}': {} }
  }
  properties: {
    logAnalyticsWorkspaceResourceId: logAnalyticsWorkspace.id
    logsExporterStorageAccountResourceId: storageAccount.id
  }
}

resource experimentMetricRoleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (createRoleForUser) {
  scope: expWorkspace
  name: guid(resourceGroup().id, userPrincipalId, experimentMetricRoleDefinition.id)
  properties: {
    principalId: userPrincipalId
    roleDefinitionId: experimentMetricRoleDefinition.id
    principalType: 'User'
  }
}

resource pipelineExperimentMetricRoleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (!createRoleForUser) {
  scope: expWorkspace
  name: guid(resourceGroup().id, pipelineServicePrincipalId, experimentMetricRoleDefinition.id)
  properties: {
    principalId: pipelineServicePrincipalId
    roleDefinitionId: experimentMetricRoleDefinition.id
    principalType: 'ServicePrincipal'
  }
}

resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2021-12-01-preview'  existing = {
  name: logAnalyticsWorkspaceName
}

resource storageAccount  'Microsoft.Storage/storageAccounts@2022-09-01'  existing = {
  name: storageAccountName
}

output expWorkspaceId string = expWorkspace.properties.expWorkspaceId
output expWorkspaceName string = expWorkspace.name
output expWorkspaceIdentityPrincipalId string = expIdentity.properties.principalId
