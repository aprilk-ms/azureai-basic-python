## Experiment analysis

> [!TIP]
> For interactive navigation of the latest analysis results for this experiment, view the [Experiment Analysis workbook](https://portal.azure.com/#blade/AppInsightsExtension/WorkbookViewerBlade/ComponentId/%2Fsubscriptions%2F80d2c6c6-fa64-4ab1-8aa5-4e118c6b16ce%2FresourceGroups%2Frg-aprilk-azure-ai-basic-01a%2Fproviders%2FMicrosoft.OperationalInsights%2Fworkspaces%2Flog-e6pnryr2q3qeg/ConfigurationId/Community-Workbooks%2FOnline%20Experimentation%2FExperiment%20Analysis/WorkbookTemplateName/Experiment%20Analysis/NotebookParams/%7B%22Workspace%22%3A%20%22%2Fsubscriptions%2F80d2c6c6-fa64-4ab1-8aa5-4e118c6b16ce%2FresourceGroups%2Frg-aprilk-azure-ai-basic-01a%2Fproviders%2FMicrosoft.OperationalInsights%2Fworkspaces%2Flog-e6pnryr2q3qeg%22%2C%20%22TimeRange%22%3A%20%7B%22durationMs%22%3A%207776000000%7D%2C%20%22FeatureName%22%3A%20%22prompty_file%22%2C%20%22AllocationId%22%3A%20%22cP_8eVbhELWLSLnV9WcR%22%7D).

* ✨ **Feature flag:** prompty_file
* 🔬 **Allocation ID:** cP_8eVbhELWLSLnV9WcR
* 📅 **Analysis period:** 0.0 days (02/20/2025 03:47 - 02/20/2025 04:47 UTC)
* 🔖 **Scorecard ID:** 400011058

### Summary of variants

| Variant 💊 | Type | Allocation | Assignment | Data quality | Treatment effect |
|:--------|:-----|-----------:|-----------:|:------------:|:----------------:|
| prompt.v1.prompty | Control | 50% | 206 | n/a | n/a |
| prompt.v2.prompty | Treatment | 50% | 218 | ![SRM check: Pass](https://img.shields.io/badge/SRM%20check-Pass-157e3b "No sample ratio mismatch detected.") | ![Change: Detected](https://img.shields.io/badge/Change-Detected-1c72af "Observed metric movements are inconsistent with statistical noise.") |


### Metric results

> [!TIP]
> Hover your cursor over a **treatment effect badge** to display the metric value and the p-value of the statistical test.

<details open="true">
<summary><strong>Important</strong> (1 of 2 conclusive)</summary>

| Metric                     |   prompt.v1.prompty 💊 | prompt.v2.prompty 💊                                                                                                                                                                                       |
|:---------------------------|-----------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI usage tokens |                  216.5 | ![Improved: -25.5%](https://img.shields.io/badge/Improved---25.5%25-157e3b "Metric value = 161.4.&#013;Highly statistically significant (p-value: 9e-4).")                                                 |
| Number of GenAI users      |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |

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

| Metric                     |   prompt.v1.prompty 💊 | prompt.v2.prompty 💊                                                                                                                                                                                       |
|:---------------------------|-----------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of GenAI chat calls |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |
| Number of GenAI chat users |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |
| Number of GenAI spans      |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |
| Number of GenAI users      |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |

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

| Metric                            |   prompt.v1.prompty 💊 | prompt.v2.prompty 💊                                                                                                                                                                                     |
|:----------------------------------|-----------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI usage input tokens  |                  22.84 | ![Degraded: +130.4%](https://img.shields.io/badge/Degraded-%2B130.4%25-d03536 "Metric value = 52.63.&#013;Highly statistically significant (p-value: ≈0).")                                              |
| Average GenAI usage output tokens |                  193.7 | ![Improved: -43.8%](https://img.shields.io/badge/Improved---43.8%25-157e3b "Metric value = 108.8.&#013;Highly statistically significant (p-value: 4e-7).")                                               |
| Average GenAI usage tokens        |                  216.5 | ![Improved: -25.5%](https://img.shields.io/badge/Improved---25.5%25-157e3b "Metric value = 161.4.&#013;Highly statistically significant (p-value: 9e-4).")                                               |
| Total GenAI chat usage tokens     |                 44,384 | ![Improved: -25.4%](https://img.shields.io/badge/Improved---25.4%25-157e3b "Metric value = 35,021 (comparison accounts for unequal allocation).&#013;Highly statistically significant (p-value: 9e-4).") |
| Total GenAI usage tokens          |                 44,384 | ![Improved: -25.4%](https://img.shields.io/badge/Improved---25.4%25-157e3b "Metric value = 35,021 (comparison accounts for unequal allocation).&#013;Highly statistically significant (p-value: 9e-4).") |

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

| Metric                           |   prompt.v1.prompty 💊 | prompt.v2.prompty 💊                                                                                                                                                                           |
|:---------------------------------|-----------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI call duration [ms] |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Average GenAI call duration [ms]:*** The average duration in milliseconds per GenAI operation. Duration is measured by the DurationMS property of the span capturing GenAI call completion. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_duration"+path%3A*.json "")</dd>
>
> </details>

</details>



<details>
<summary><strong>GenAI</strong> (5 of 18 conclusive)</summary>

| Metric                                          |   prompt.v1.prompty 💊 | prompt.v2.prompty 💊                                                                                                                                                                                       |
|:------------------------------------------------|-----------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Average GenAI call duration [ms]                |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")             |
| Average GenAI usage input tokens                |                  22.84 | ![Degraded: +130.4%](https://img.shields.io/badge/Degraded-%2B130.4%25-d03536 "Metric value = 52.63.&#013;Highly statistically significant (p-value: ≈0).")                                                |
| Average GenAI usage output tokens               |                  193.7 | ![Improved: -43.8%](https://img.shields.io/badge/Improved---43.8%25-157e3b "Metric value = 108.8.&#013;Highly statistically significant (p-value: 4e-7).")                                                 |
| Average GenAI usage tokens                      |                  216.5 | ![Improved: -25.5%](https://img.shields.io/badge/Improved---25.5%25-157e3b "Metric value = 161.4.&#013;Highly statistically significant (p-value: 9e-4).")                                                 |
| Coherence score                                 |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")             |
| Fluency score                                   |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")             |
| Hate unfairness score                           |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")             |
| Number of GenAI chat calls                      |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |
| Number of GenAI chat users                      |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |
| Number of GenAI operations that end in an error |                      0 | ![Inconclusive: --](https://img.shields.io/badge/Inconclusive------e6e6e3 "Metric value = 1 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).")           |
| Number of GenAI spans                           |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |
| Number of GenAI users                           |                    205 | ![Inconclusive: +0.5%](https://img.shields.io/badge/Inconclusive-%2B0.5%25-e6e6e3 "Metric value = 218 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.318).") |
| Protected material score                        |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")             |
| Relevance score                                 |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")             |
| Sexual content score                            |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")             |
| Total GenAI chat usage tokens                   |                 44,384 | ![Improved: -25.4%](https://img.shields.io/badge/Improved---25.4%25-157e3b "Metric value = 35,021 (comparison accounts for unequal allocation).&#013;Highly statistically significant (p-value: 9e-4).")   |
| Total GenAI usage tokens                        |                 44,384 | ![Improved: -25.4%](https://img.shields.io/badge/Improved---25.4%25-157e3b "Metric value = 35,021 (comparison accounts for unequal allocation).&#013;Highly statistically significant (p-value: 9e-4).")   |
| Violent content score                           |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection")             |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Average GenAI call duration [ms]:*** The average duration in milliseconds per GenAI operation. Duration is measured by the DurationMS property of the span capturing GenAI call completion. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_duration"+path%3A*.json "")</dd>
> * ***Average GenAI usage input tokens:*** The average tokens used on input (prompt) per GenAI call of any type. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_input_tokens"+path%3A*.json "")</dd>
> * ***Average GenAI usage output tokens:*** The average tokens used on output (response) per GenAI call of any type. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_output_tokens"+path%3A*.json "")</dd>
> * ***Average GenAI usage tokens:*** The average usage tokens (both input and output) per GenAI call of any type. Default desiredDirection is 'Decrease', appropriate for cases where cost reduction is a priority. If you are optimizing for user engagement regardless of cost, you may want to change this to 'Neutral'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="avg_genai_tokens"+path%3A*.json "")</dd>
> * ***Coherence score:*** Coherence score given by Azure AI evaluation. The coherence measure assesses the ability of the language model to generate text that reads naturally, flows smoothly, and resembles human-like language in its responses. Use it when assessing the readability and user-friendliness of a model's generated responses in real-world applications. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.coherenceevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_coherence"+path%3A*.json "")</dd>
> * ***Fluency score:*** Fluency score given by Azure AI evaluation. The fluency measure assesses the extent to which the generated text conforms to grammatical rules, syntactic structures, and appropriate vocabulary usage, resulting in linguistically correct responses. The fluency score range from 1 to 5. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.fluencyevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_fluency"+path%3A*.json "")</dd>
> * ***Hate unfairness score:*** Hate and unfair score given by Azure AI evaluation. Hateful and unfair content refers to any language pertaining to hate toward or unfair representations of individuals and social groups along factors including but not limited to race, ethnicity, nationality, gender, sexual orientation, religion, immigration status, ability, personal appearance, and body size. Unfairness occurs when AI systems treat or represent social groups inequitably, creating or contributing to societal inequities. Safety evaluations annotate self-harm-related content using a 0-7 scale. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.hateunfairnessevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_hate_unfairness"+path%3A*.json "")</dd>
> * ***Number of GenAI chat calls:*** The number of GenAI spans with gen_ai.operation.name =='chat'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_chats"+path%3A*.json "")</dd>
> * ***Number of GenAI chat users:*** The number of users with at least one GenAI span with gen_ai.operation.name =='chat'. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_chat_users"+path%3A*.json "")</dd>
> * ***Number of GenAI operations that end in an error:*** The number of GenAI calls that have a non-empty 'error.type' attribute. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_with_error"+path%3A*.json "")</dd>
> * ***Number of GenAI spans:*** The number of GenAI spans. This is an approximation of the number of total GenAI requests made. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_spans"+path%3A*.json "")</dd>
> * ***Number of GenAI users:*** The number of users producing at least one GenAI span. This metric measures discovery/adoption of your GenAI features. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="count_genai_users"+path%3A*.json "")</dd>
> * ***Protected material score:*** Protected material score by Azure AI content safety API. The Protected material detection APIs scan the output of large language models to identify and flag known protected material. See (https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/protected-material?tabs=text) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_protected_material"+path%3A*.json "")</dd>
> * ***Relevance score:*** Relevance score given by Azure AI evaluation. The relevance measure assesses the ability of answers to capture the key points of the context. High relevance scores signify the AI system's understanding of the input and its capability to produce coherent and contextually appropriate outputs. Conversely, low relevance scores indicate that generated responses might be off-topic, lacking in context, or insufficient in addressing the user's intended queries. Relevance scores range from 1 to 5. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.relevanceevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_relevance"+path%3A*.json "")</dd>
> * ***Sexual content score:*** Score for sexual content given by Azure AI evaluation. Sexual score is range from 0 to 7. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.sexualevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_sexual"+path%3A*.json "")</dd>
> * ***Total GenAI chat usage tokens:*** The total usage tokens (both input and output) for GenAI chat calls. Assuming equal number of chat calls, we want total token usage to reduce or remain constant. The statistical test on this metric compares the token usage per user: meaning increased usage may increase the total usage tokens without flagging this metric as statistically significant. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="sum_genai_chat_tokens"+path%3A*.json "")</dd>
> * ***Total GenAI usage tokens:*** While average usage tokens gives an indication of per-call efficiency, your cost is based on the total token usage. This metric show total usage tokens (both input and output) for any type of GenAI calls. Assuming equal number of GenAI calls, we want total token usage to reduce or remain constant. The statistical test on this metric compares the token usage per user: meaning increased usage may increase the total usage tokens without flagging this metric as statistically significant. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="sum_genai_tokens"+path%3A*.json "")</dd>
> * ***Violent content score:*** Violence score given by Azure AI evaluation, Violence score is range from 0 to 7. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.violenceevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_violence"+path%3A*.json "")</dd>
>
> </details>

</details>



<details>
<summary><strong>azure_ai_evaluation</strong> (0 of 7 conclusive)</summary>

| Metric                   |   prompt.v1.prompty 💊 | prompt.v2.prompty 💊                                                                                                                                                                           |
|:-------------------------|-----------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Coherence score          |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |
| Fluency score            |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |
| Hate unfairness score    |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |
| Protected material score |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |
| Relevance score          |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |
| Sexual content score     |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |
| Violent content score    |                      0 | ![Zero samples: 0%](https://img.shields.io/badge/Zero%20samples-0%25-f0e543 "Metric value = 0.&#013;Zero observations might indicate a problem with the metric definition or data collection") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Coherence score:*** Coherence score given by Azure AI evaluation. The coherence measure assesses the ability of the language model to generate text that reads naturally, flows smoothly, and resembles human-like language in its responses. Use it when assessing the readability and user-friendliness of a model's generated responses in real-world applications. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.coherenceevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_coherence"+path%3A*.json "")</dd>
> * ***Fluency score:*** Fluency score given by Azure AI evaluation. The fluency measure assesses the extent to which the generated text conforms to grammatical rules, syntactic structures, and appropriate vocabulary usage, resulting in linguistically correct responses. The fluency score range from 1 to 5. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.fluencyevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_fluency"+path%3A*.json "")</dd>
> * ***Hate unfairness score:*** Hate and unfair score given by Azure AI evaluation. Hateful and unfair content refers to any language pertaining to hate toward or unfair representations of individuals and social groups along factors including but not limited to race, ethnicity, nationality, gender, sexual orientation, religion, immigration status, ability, personal appearance, and body size. Unfairness occurs when AI systems treat or represent social groups inequitably, creating or contributing to societal inequities. Safety evaluations annotate self-harm-related content using a 0-7 scale. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.hateunfairnessevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_hate_unfairness"+path%3A*.json "")</dd>
> * ***Protected material score:*** Protected material score by Azure AI content safety API. The Protected material detection APIs scan the output of large language models to identify and flag known protected material. See (https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/protected-material?tabs=text) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_protected_material"+path%3A*.json "")</dd>
> * ***Relevance score:*** Relevance score given by Azure AI evaluation. The relevance measure assesses the ability of answers to capture the key points of the context. High relevance scores signify the AI system's understanding of the input and its capability to produce coherent and contextually appropriate outputs. Conversely, low relevance scores indicate that generated responses might be off-topic, lacking in context, or insufficient in addressing the user's intended queries. Relevance scores range from 1 to 5. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.relevanceevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_relevance"+path%3A*.json "")</dd>
> * ***Sexual content score:*** Score for sexual content given by Azure AI evaluation. Sexual score is range from 0 to 7. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.sexualevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_sexual"+path%3A*.json "")</dd>
> * ***Violent content score:*** Violence score given by Azure AI evaluation, Violence score is range from 0 to 7. See (https://learn.microsoft.com/en-us/python/api/azure-ai-evaluation/azure.ai.evaluation.violenceevaluator?view=azure-python) for more details. [Search for metric definition.](https://github.com/aprilk-ms/azureai-basic-python/search?q="genai_evaluation_violence"+path%3A*.json "")</dd>
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
