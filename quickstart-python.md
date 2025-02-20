# Python
See [here](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-variant-feature-flags-python) for the full tutorial.

## Install SDK

```
pip install azure-identity 
pip install azure-appconfiguration-provider
pip install featuremanagement[AzureMonitor]
```

## Define a targeting context accessor method

The accessor method is called from both Feature Management and Azure Monitor to identify the user for the current request.

```python
async def my_targeting_accessor() -> TargetingContext:
    user_id = request.headers.get('user-id', str(uuid.uuid4())
    return TargetingContext(user_id=user_id)
```

## Initialize Application Insights

[Connect to Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/asp-net-core) to instrument your application. Include the `TargetingSpanProcessor` to allow request and dependency data to be available for metrics.

```python
from azure.monitor.opentelemetry import configure_azure_monitor
from featuremanagement.azuremonitor import TargetingSpanProcessor

configure_azure_monitor(
    connection_string=os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"),
    span_processors=[TargetingSpanProcessor(targeting_context_accessor=my_targeting_accessor)]
)
```

## Initialize App Configuration and Feature Manager

[Connect to App Configuration](https://learn.microsoft.com/azure/azure-app-configuration/quickstart-feature-flag-python#console-applications), which supplies feature flags and other configurations to your application. Use `DefaultAzureCredential` to authenticate to your App Configuration store. Follow the [instructions](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-enable-rbac#authentication-with-token-credentials) to assign your credential the App Configuration Data Reader role. 

```python
from azure.appconfiguration.provider import load
from azure.identity import DefaultAzureCredential
from featuremanagement import FeatureManager
from featuremanagement.azuremonitor import publish_telemetry, track_event

azure_app_config = load(endpoint="<your-endpoint>", credential=DefaultAzureCredential(), feature_flag_enabled=True, feature_flag_refresh_enabled=True)
feature_manager = FeatureManager(azure_app_config, on_feature_evaluated=publish_telemetry, targeting_context_accessor=my_targeting_accessor)
```

## Use Feature Flag

Use feature manager to get the feature variant assigned to the user.

```python
my_feature_flag = feature_manager.get_variant("<placeholder-feature-flag-name>"):
if my_feature_flag:
    variant_name = my_feature_flag.name
    variant_value = my_feature_flag.configuration
    # do something with the variant value
```

## Log event
```
# The user_id from the targeting context needs to be manually added for now due to an missing Azure Monitor support.
track_event("<placeholder-event-name>", my_targeting_accessor().user_id)
```

## Validate Event Logs
- Run your application and trigger one or more get_variant() calls for the test feature flag.
- Go to the Log Analytics workspace (add link to LA workspace/log page) and execute the following query. After a short ingestion delay, you should see the log events for the feature evaluation calls.

```
AppEvents | where Name == "FeatureEvaluation"
```