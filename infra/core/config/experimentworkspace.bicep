metadata description = 'Creates an experiment workspace'
param name string
param location string = resourceGroup().location
param tags object = {}

param logAnalyticsWorkspaceName string
param storageAccountName string
param identityName string
param appConfigName string

resource expIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: identityName
  location: location
}

// Noite: no intellisense during private preview period
#disable-next-line BCP081
resource expWorkspace 'Microsoft.OnlineExperimentation/workspaces@2025-05-31-preview' = {
  name: name
  location: location
  tags: tags
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: { '${expIdentity.id}': {} }
  }
  properties: {
    logAnalyticsWorkspaceResourceId: logAnalyticsWorkspace.id
    logsExporterStorageAccountResourceId: storageAccount.id
    appConfigurationResourceId: appConfig.id
  }
  sku: {
    name: 'F0'
  }
}


// // Noite: no intellisense during private preview period
// #disable-next-line BCP081
// resource expWorkspace 'Microsoft.Experimentation/experimentWorkspaces@2024-11-30-preview' = {
//   name: name
//   location: location
//   tags: tags
//   kind: 'Regular'
//   identity: {
//     type: 'UserAssigned'
//     userAssignedIdentities: { '${expIdentity.id}': {} }
//   }
//   properties: {
//     logAnalyticsWorkspaceResourceId: logAnalyticsWorkspace.id
//     logsExporterStorageAccountResourceId: storageAccount.id
//   }
// }

// resource experimentMetricRoleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
//   scope: expWorkspace
//   name: guid(resourceGroup().id, userPrincipalId, experimentMetricRoleDefinition.id)
//   properties: {
//     principalId: userPrincipalId
//     roleDefinitionId: experimentMetricRoleDefinition.id
//     principalType: 'User'
//   }
// }

resource appConfig 'Microsoft.AppConfiguration/configurationStores@2023-09-01-preview'  existing = {
  name: appConfigName
}

resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2021-12-01-preview'  existing = {
  name: logAnalyticsWorkspaceName
}

resource storageAccount  'Microsoft.Storage/storageAccounts@2022-09-01'  existing = {
  name: storageAccountName
}

output expWorkspaceId string = expWorkspace.properties.workspaceId
output expWorkspaceName string = expWorkspace.name
output expWorkspaceIdentityPrincipalId string = expIdentity.properties.principalId
