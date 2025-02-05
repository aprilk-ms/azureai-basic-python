## Experiment analysis

> [!TIP]
> For interactive navigation of the latest analysis results for this experiment, view the [Experiment Analysis workbook](https://portal.azure.com/#blade/AppInsightsExtension/WorkbookViewerBlade/ComponentId/%2Fsubscriptions%2F80d2c6c6-fa64-4ab1-8aa5-4e118c6b16ce%2FresourceGroups%2Frg-aprilk-azure-ai-basic-01a%2Fproviders%2FMicrosoft.OperationalInsights%2Fworkspaces%2Flog-e6pnryr2q3qeg/ConfigurationId/Community-Workbooks%2FOnline%20Experimentation%2FExperiment%20Analysis/WorkbookTemplateName/Experiment%20Analysis/NotebookParams/%7B%22Workspace%22%3A%20%22%2Fsubscriptions%2F80d2c6c6-fa64-4ab1-8aa5-4e118c6b16ce%2FresourceGroups%2Frg-aprilk-azure-ai-basic-01a%2Fproviders%2FMicrosoft.OperationalInsights%2Fworkspaces%2Flog-e6pnryr2q3qeg%22%2C%20%22TimeRange%22%3A%20%7B%22durationMs%22%3A%207776000000%7D%2C%20%22FeatureName%22%3A%20%22prompty_file%22%2C%20%22AllocationId%22%3A%20%22Qi7LDcLPLBNCx5IM4AUV%22%7D).

* ✨ **Feature flag:** prompty_file
* 🔬 **Allocation ID:** Qi7LDcLPLBNCx5IM4AUV
* 📅 **Analysis period:** 0.0 days (02/05/2025 03:00 - 02/05/2025 04:00 UTC)
* 🔖 **Scorecard ID:** 400010050

### Summary of variants

| Variant 💊 | Type | Allocation | Assignment | Data quality | Treatment effect |
|:--------|:-----|-----------:|-----------:|:------------:|:----------------:|
| v1 | Control | 50% | 11 | n/a | n/a |
| v2 | Treatment | 50% | 11 | ![SRM check: Pass](https://img.shields.io/badge/SRM%20check-Pass-157e3b "No sample ratio mismatch detected.") | ![Change: Undetected](https://img.shields.io/badge/Change-Undetected-e6e6e3 "Observed metric movements are consistent with statistical noise.&#013;Either the experiment is underpowered or had limited impact on the metrics.") |


### Metric results

> [!TIP]
> Hover your cursor over a **treatment effect badge** to display the metric value and the p-value of the statistical test.

<details open="true">
<summary><strong>Important</strong> (0 of 2 conclusive)</summary>

| Metric                     |   v1 💊 | v2 💊                                                                                                                                                                                                                                |
|:---------------------------|--------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI usage tokens |      50 | ![Too few samples: +236.0%](https://img.shields.io/badge/Too%20few%20samples-%2B236.0%25-f0e543 "Metric value = 168.&#013;Insufficient observations to determine statistical significance")                                          |
| Number of GenAI users      |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Average GenAI usage tokens:*** The average usage tokens (both input and output) per GenAI call of any type. Default desiredDirection is 'Decrease', appropriate for cases where cost reduction is a priority. If you are optimizing for user engagement regardless of cost, you may want to change this to 'Neutral'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_tokens"+path%3A*.json "")</dd>
> * ***Number of GenAI users:*** The number of users producing at least one GenAI span. This metric measures discovery/adoption of your GenAI features. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_users"+path%3A*.json "")</dd>
>
> </details>

</details>



<details>
<summary><strong>Usage</strong> (0 of 4 conclusive)</summary>

| Metric                     |   v1 💊 | v2 💊                                                                                                                                                                                                                                |
|:---------------------------|--------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of GenAI chat calls |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |
| Number of GenAI chat users |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |
| Number of GenAI spans      |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |
| Number of GenAI users      |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Number of GenAI chat calls:*** The number of GenAI spans with gen_ai.operation.name =='chat'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_chats"+path%3A*.json "")</dd>
> * ***Number of GenAI chat users:*** The number of users with at least one GenAI span with gen_ai.operation.name =='chat'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_chat_users"+path%3A*.json "")</dd>
> * ***Number of GenAI spans:*** The number of GenAI spans. This is an approximation of the number of total GenAI requests made. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_spans"+path%3A*.json "")</dd>
> * ***Number of GenAI users:*** The number of users producing at least one GenAI span. This metric measures discovery/adoption of your GenAI features. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_users"+path%3A*.json "")</dd>
>
> </details>

</details>



<details>
<summary><strong>Cost</strong> (0 of 5 conclusive)</summary>

| Metric                            |   v1 💊 | v2 💊                                                                                                                                                                                                                                    |
|:----------------------------------|--------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI usage input tokens  |      19 | ![Too few samples: +545.6%](https://img.shields.io/badge/Too%20few%20samples-%2B545.6%25-f0e543 "Metric value = 122.7.&#013;Insufficient observations to determine statistical significance")                                            |
| Average GenAI usage output tokens |      31 | ![Too few samples: +46.2%](https://img.shields.io/badge/Too%20few%20samples-%2B46.2%25-f0e543 "Metric value = 45.33.&#013;Insufficient observations to determine statistical significance")                                              |
| Average GenAI usage tokens        |      50 | ![Too few samples: +236.0%](https://img.shields.io/badge/Too%20few%20samples-%2B236.0%25-f0e543 "Metric value = 168.&#013;Insufficient observations to determine statistical significance")                                              |
| Total GenAI chat usage tokens     |      50 | ![Too few samples: +908.0%](https://img.shields.io/badge/Too%20few%20samples-%2B908.0%25-f0e543 "Metric value = 504 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |
| Total GenAI usage tokens          |      50 | ![Too few samples: +908.0%](https://img.shields.io/badge/Too%20few%20samples-%2B908.0%25-f0e543 "Metric value = 504 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Average GenAI usage input tokens:*** The average tokens used on input (prompt) per GenAI call of any type. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_input_tokens"+path%3A*.json "")</dd>
> * ***Average GenAI usage output tokens:*** The average tokens used on output (response) per GenAI call of any type. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_output_tokens"+path%3A*.json "")</dd>
> * ***Average GenAI usage tokens:*** The average usage tokens (both input and output) per GenAI call of any type. Default desiredDirection is 'Decrease', appropriate for cases where cost reduction is a priority. If you are optimizing for user engagement regardless of cost, you may want to change this to 'Neutral'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_tokens"+path%3A*.json "")</dd>
> * ***Total GenAI chat usage tokens:*** The total usage tokens (both input and output) for GenAI chat calls. Assuming equal number of chat calls, we want total token usage to reduce or remain constant. The statistical test on this metric compares the token usage per user: meaning increased usage may increase the total usage tokens without flagging this metric as statistically significant. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="sum_genai_chat_tokens"+path%3A*.json "")</dd>
> * ***Total GenAI usage tokens:*** While average usage tokens gives an indication of per-call efficiency, your cost is based on the total token usage. This metric show total usage tokens (both input and output) for any type of GenAI calls. Assuming equal number of GenAI calls, we want total token usage to reduce or remain constant. The statistical test on this metric compares the token usage per user: meaning increased usage may increase the total usage tokens without flagging this metric as statistically significant. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="sum_genai_tokens"+path%3A*.json "")</dd>
>
> </details>

</details>



<details>
<summary><strong>Performance</strong> (0 of 1 conclusive)</summary>

| Metric                           |   v1 💊 | v2 💊                                                                                                                                                                                          |
|:---------------------------------|--------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI call duration [ms] |       0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Average GenAI call duration [ms]:*** The average duration in milliseconds per GenAI operation. Duration is measured by the DurationMS property of the span capturing GenAI call completion. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_duration"+path%3A*.json "")</dd>
>
> </details>

</details>



<details>
<summary><strong>GenAI</strong> (0 of 11 conclusive)</summary>

| Metric                                          |   v1 💊 | v2 💊                                                                                                                                                                                                                                    |
|:------------------------------------------------|--------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI call duration [ms]                |       0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")                                           |
| Average GenAI usage input tokens                |      19 | ![Too few samples: +545.6%](https://img.shields.io/badge/Too%20few%20samples-%2B545.6%25-f0e543 "Metric value = 122.7.&#013;Insufficient observations to determine statistical significance")                                            |
| Average GenAI usage output tokens               |      31 | ![Too few samples: +46.2%](https://img.shields.io/badge/Too%20few%20samples-%2B46.2%25-f0e543 "Metric value = 45.33.&#013;Insufficient observations to determine statistical significance")                                              |
| Average GenAI usage tokens                      |      50 | ![Too few samples: +236.0%](https://img.shields.io/badge/Too%20few%20samples-%2B236.0%25-f0e543 "Metric value = 168.&#013;Insufficient observations to determine statistical significance")                                              |
| Number of GenAI chat calls                      |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance")     |
| Number of GenAI chat users                      |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance")     |
| Number of GenAI operations that end in an error |       3 | ![Too few samples: -66.7%](https://img.shields.io/badge/Too%20few%20samples---66.7%25-f0e543 "Metric value = 1 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance")      |
| Number of GenAI spans                           |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance")     |
| Number of GenAI users                           |       7 | ![Too few samples: +14.3%](https://img.shields.io/badge/Too%20few%20samples-%2B14.3%25-f0e543 "Metric value = 8 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance")     |
| Total GenAI chat usage tokens                   |      50 | ![Too few samples: +908.0%](https://img.shields.io/badge/Too%20few%20samples-%2B908.0%25-f0e543 "Metric value = 504 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |
| Total GenAI usage tokens                        |      50 | ![Too few samples: +908.0%](https://img.shields.io/badge/Too%20few%20samples-%2B908.0%25-f0e543 "Metric value = 504 (comparison accounts for unequal allocation).&#013;Insufficient observations to determine statistical significance") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Average GenAI call duration [ms]:*** The average duration in milliseconds per GenAI operation. Duration is measured by the DurationMS property of the span capturing GenAI call completion. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_duration"+path%3A*.json "")</dd>
> * ***Average GenAI usage input tokens:*** The average tokens used on input (prompt) per GenAI call of any type. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_input_tokens"+path%3A*.json "")</dd>
> * ***Average GenAI usage output tokens:*** The average tokens used on output (response) per GenAI call of any type. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_output_tokens"+path%3A*.json "")</dd>
> * ***Average GenAI usage tokens:*** The average usage tokens (both input and output) per GenAI call of any type. Default desiredDirection is 'Decrease', appropriate for cases where cost reduction is a priority. If you are optimizing for user engagement regardless of cost, you may want to change this to 'Neutral'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_tokens"+path%3A*.json "")</dd>
> * ***Number of GenAI chat calls:*** The number of GenAI spans with gen_ai.operation.name =='chat'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_chats"+path%3A*.json "")</dd>
> * ***Number of GenAI chat users:*** The number of users with at least one GenAI span with gen_ai.operation.name =='chat'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_chat_users"+path%3A*.json "")</dd>
> * ***Number of GenAI operations that end in an error:*** The number of GenAI calls that have a non-empty 'error.type' attribute. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_with_error"+path%3A*.json "")</dd>
> * ***Number of GenAI spans:*** The number of GenAI spans. This is an approximation of the number of total GenAI requests made. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_spans"+path%3A*.json "")</dd>
> * ***Number of GenAI users:*** The number of users producing at least one GenAI span. This metric measures discovery/adoption of your GenAI features. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_users"+path%3A*.json "")</dd>
> * ***Total GenAI chat usage tokens:*** The total usage tokens (both input and output) for GenAI chat calls. Assuming equal number of chat calls, we want total token usage to reduce or remain constant. The statistical test on this metric compares the token usage per user: meaning increased usage may increase the total usage tokens without flagging this metric as statistically significant. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="sum_genai_chat_tokens"+path%3A*.json "")</dd>
> * ***Total GenAI usage tokens:*** While average usage tokens gives an indication of per-call efficiency, your cost is based on the total token usage. This metric show total usage tokens (both input and output) for any type of GenAI calls. Assuming equal number of GenAI calls, we want total token usage to reduce or remain constant. The statistical test on this metric compares the token usage per user: meaning increased usage may increase the total usage tokens without flagging this metric as statistically significant. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="sum_genai_tokens"+path%3A*.json "")</dd>
>
> </details>

</details>

---

### Guide

<details>
<summary><strong>Treatment effect badges</strong></summary>

Each treatment column displays the impact of the treatment variant upon the metric value, relative to the control variant. For example, "+5.3%" means the metric value is 5.3% higher in the treatment variant than the control variant. The experiment analysis checks whether the observed treatment effect could be explained by random noise in the data.

* If not statistically significant, we display the badge: ![Inconclusive: +5.3%](https://img.shields.io/badge/Inconclusive-%2B5.3%25-e6e6e3 "Not statistically significant.")
* If statistically significant, the badge color reflects the desired direction of the metric and the strength of confidence:

| Observed treatment effect | Marginal confidence<br />(p-value ≤ 0.05) | High confidence<br />(p-value ≤ 0.001) |
|:--------------------------|:------------------------------------------|:---------------------------------------|
| Against the desired direction | ![Degraded: +5.3%](https://img.shields.io/badge/Degraded-%2B5.3%25-fcae91 "Marginally statistically significant.") | ![Degraded: +5.3%](https://img.shields.io/badge/Degraded-%2B5.3%25-d03536 "Highly statistically significant.") |
| Matches the desired direction | ![Improved: +5.3%](https://img.shields.io/badge/Improved-%2B5.3%25-a1d99b "Marginally statistically significant.") | ![Improved: +5.3%](https://img.shields.io/badge/Improved-%2B5.3%25-157e3b "Highly statistically significant.") |
| Desired direction is neutral | ![Changed: +5.3%](https://img.shields.io/badge/Changed-%2B5.3%25-9ecae1 "Marginally statistically significant.") | ![Changed: +5.3%](https://img.shields.io/badge/Changed-%2B5.3%25-1c72af "Highly statistically significant.") |

</details>
