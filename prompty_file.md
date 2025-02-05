## Experiment analysis

> [!TIP]
> For interactive navigation of the latest analysis results for this experiment, view the [Experiment Analysis workbook](https://portal.azure.com/#blade/AppInsightsExtension/WorkbookViewerBlade/ComponentId/%2Fsubscriptions%2F80d2c6c6-fa64-4ab1-8aa5-4e118c6b16ce%2FresourceGroups%2Frg-aprilk-azure-ai-basic-01a%2Fproviders%2FMicrosoft.OperationalInsights%2Fworkspaces%2Flog-e6pnryr2q3qeg/ConfigurationId/Community-Workbooks%2FOnline%20Experimentation%2FExperiment%20Analysis/WorkbookTemplateName/Experiment%20Analysis/NotebookParams/%7B%22Workspace%22%3A%20%22%2Fsubscriptions%2F80d2c6c6-fa64-4ab1-8aa5-4e118c6b16ce%2FresourceGroups%2Frg-aprilk-azure-ai-basic-01a%2Fproviders%2FMicrosoft.OperationalInsights%2Fworkspaces%2Flog-e6pnryr2q3qeg%22%2C%20%22TimeRange%22%3A%20%7B%22durationMs%22%3A%207776000000%7D%2C%20%22FeatureName%22%3A%20%22prompty_file%22%2C%20%22AllocationId%22%3A%20%22Qi7LDcLPLBNCx5IM4AUV%22%7D).

* ✨ **Feature flag:** prompty_file
* 🔬 **Allocation ID:** Qi7LDcLPLBNCx5IM4AUV
* 📅 **Analysis period:** 0.2 days (02/05/2025 03:00 - 02/05/2025 07:00 UTC)
* 🔖 **Scorecard ID:** 400010051

### Summary of variants

| Variant 💊 | Type | Allocation | Assignment | Data quality | Treatment effect |
|:--------|:-----|-----------:|-----------:|:------------:|:----------------:|
| v1 | Control | 50% | 531 | n/a | n/a |
| v2 | Treatment | 50% | 570 | ![SRM check: Pass](https://img.shields.io/badge/SRM%20check-Pass-157e3b "No sample ratio mismatch detected.") | ![Change: Detected](https://img.shields.io/badge/Change-Detected-1c72af "Observed metric movements are inconsistent with statistical noise.") |


### Metric results

> [!TIP]
> Hover your cursor over a **treatment effect badge** to display the metric value and the p-value of the statistical test.

<details open="true">
<summary><strong>Important</strong> (1 of 2 conclusive)</summary>

| Metric                     |   v1 💊 | v2 💊                                                                                                                                                                                                      |
|:---------------------------|--------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI usage tokens |   207.1 | ![Improved: -20.3%](https://img.shields.io/badge/Improved---20.3%25-157e3b "Metric value = 165.1.&#013;Highly statistically significant (p-value: 1e-4).")                                                 |
| Number of GenAI users      |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).") |

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

| Metric                     |   v1 💊 | v2 💊                                                                                                                                                                                                      |
|:---------------------------|--------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of GenAI chat calls |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).") |
| Number of GenAI chat users |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).") |
| Number of GenAI spans      |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).") |
| Number of GenAI users      |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).") |

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
<summary><strong>Cost</strong> (5 of 5 conclusive)</summary>

| Metric                            |   v1 💊 | v2 💊                                                                                                                                                                                                         |
|:----------------------------------|--------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI usage input tokens  |   22.69 | ![Degraded: +134.5%](https://img.shields.io/badge/Degraded-%2B134.5%25-d03536 "Metric value = 53.2.&#013;Highly statistically significant (p-value: 1e-313).")                                                |
| Average GenAI usage output tokens |   184.4 | ![Improved: -39.3%](https://img.shields.io/badge/Improved---39.3%25-157e3b "Metric value = 111.9.&#013;Highly statistically significant (p-value: 6e-11).")                                                   |
| Average GenAI usage tokens        |   207.1 | ![Improved: -20.3%](https://img.shields.io/badge/Improved---20.3%25-157e3b "Metric value = 165.1.&#013;Highly statistically significant (p-value: 1e-4).")                                                    |
| Total GenAI chat usage tokens     |  92,778 | ![Improved: -17.3%](https://img.shields.io/badge/Improved---17.3%25-a1d99b "Metric value = 82,386 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.003).") |
| Total GenAI usage tokens          |  92,778 | ![Improved: -17.3%](https://img.shields.io/badge/Improved---17.3%25-a1d99b "Metric value = 82,386 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.003).") |

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
<summary><strong>GenAI</strong> (5 of 11 conclusive)</summary>

| Metric                                          |   v1 💊 | v2 💊                                                                                                                                                                                                         |
|:------------------------------------------------|--------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI call duration [ms]                |       0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")                |
| Average GenAI usage input tokens                |   22.69 | ![Degraded: +134.5%](https://img.shields.io/badge/Degraded-%2B134.5%25-d03536 "Metric value = 53.2.&#013;Highly statistically significant (p-value: 1e-313).")                                                |
| Average GenAI usage output tokens               |   184.4 | ![Improved: -39.3%](https://img.shields.io/badge/Improved---39.3%25-157e3b "Metric value = 111.9.&#013;Highly statistically significant (p-value: 6e-11).")                                                   |
| Average GenAI usage tokens                      |   207.1 | ![Improved: -20.3%](https://img.shields.io/badge/Improved---20.3%25-157e3b "Metric value = 165.1.&#013;Highly statistically significant (p-value: 1e-4).")                                                    |
| Number of GenAI chat calls                      |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).")    |
| Number of GenAI chat users                      |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).")    |
| Number of GenAI operations that end in an error |      10 | ![Inconclusive: -34.8%](https://img.shields.io/badge/Inconclusive---34.8%25-e6e6e3 "Metric value = 7 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.382).")     |
| Number of GenAI spans                           |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).")    |
| Number of GenAI users                           |     527 | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 567 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.638).")    |
| Total GenAI chat usage tokens                   |  92,778 | ![Improved: -17.3%](https://img.shields.io/badge/Improved---17.3%25-a1d99b "Metric value = 82,386 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.003).") |
| Total GenAI usage tokens                        |  92,778 | ![Improved: -17.3%](https://img.shields.io/badge/Improved---17.3%25-a1d99b "Metric value = 82,386 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.003).") |

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
