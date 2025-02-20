# ASP.NET
See [here](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-variant-feature-flags-aspnet-core) for the full tutorial.


## Install SDK via .NET CLI

```
dotnet add package Azure.Identity
dotnet add package Microsoft.Extensions.Configuration.AzureAppConfiguration
dotnet add package Microsoft.FeatureManagement.AspNetCore
```

## Initialize Application Insights

[Connect to Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/asp-net-core) to instrument your application.

```dotnet
builder.Services.AddApplicationInsightsTelemetry();
```

## Initialize App Configuration

[Connect to App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-aspnet-core-app?tabs=entra-id), which supplies feature flags and other configurations to your application. 
Use `DefaultAzureCredential` to authenticate to your App Configuration store. Follow the [instructions](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-enable-rbac#authentication-with-token-credentials) to assign your credential the App Configuration Data Reader role. 


```dotnet
builder.Configuration.AddAzureAppConfiguration(options =>
{
    options.Connect(new Uri(endpoint), new DefaultAzureCredential());
});
```

## Setup Feature Management

Add Feature Management to the service collection and the targeting middleware to provide user Id for variant assignments.

```dotnet
builder.Services.AddFeatureManagement()
    .WithTargeting()
    .AddApplicationInsightsTelemetry();
 
app.UseMiddleware<TargetingHttpContextMiddleware>();
```

## Use Feature Flag

Use dependency injection to retrieve an instance of `IVariantFeatureManager` and get the feature variant assigned to the user. 

```dotnet
Variant variant = await featureManager
    .GetVariantAsync("<placeholder-feature-flag-name>", HttpContext.RequestAborted);
```

## Log Events
Use dependency injection to retrieve `TelemetryClient` to log custom events.

```dotnet
telemetryClient.TrackEvent("<placeholder-event-name>");
```

## Validate Event Logs
- Run your application and trigger one or more get_variant() calls for the test feature flag.
- Go to the Log Analytics workspace (add link to LA workspace/log page) and execute the following query. After a short ingestion delay, you should see the log events for the feature evaluation calls.

```
AppEvents | where Name == "FeatureEvaluation"
```