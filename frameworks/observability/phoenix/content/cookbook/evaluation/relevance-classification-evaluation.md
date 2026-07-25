---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/cookbook/evaluation/relevance-classification-evaluation.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.869819Z"
---
---
description: "Evaluate the relevance of documents retrieved by RAG applications using Phoenix's evaluation framework."
title: "Relevance Classification Evaluation"
---

This tutorial shows how to classify documents as relevant or irrelevant to queries using benchmark datasets with ground-truth labels.

**Key Points:**

- Download and prepare benchmark datasets for relevance classification
- Compare different LLM models (GPT-4, GPT-3.5, GPT-4 Turbo) for classification accuracy
- Analyze results with confusion matrices and detailed reports
- Get explanations for LLM classifications to understand decision-making
- Measure retrieval quality using ranking metrics like precision@k

## Notebook Walkthrough

We will go through key code snippets on this page. To follow the full tutorial, check out the full notebook.

<Card
  title="Google Colab"
  href="https://colab.research.google.com/github/Arize-ai/tutorials/blob/main/python/cookbooks/phoenix_evals_examples/evaluate_relevance_classifications.ipynb"
  icon="https://storage.googleapis.com/arize-phoenix-assets/assets/images/phoenix-docs-images/gc.ico"
  horizontal
>
  colab.research.google.com
</Card>

## Download Benchmark Dataset

```python
df = download_benchmark_dataset(
    task="binary-relevance-classification",
    dataset_name="wiki_qa-train"
)
```

## Configure Evaluation

```python
N_EVAL_SAMPLE_SIZE = 100
df_sample = df.sample(n=N_EVAL_SAMPLE_SIZE).reset_index(drop=True)
df_sample = df_sample.rename(columns={
    "query_text": "input",
    "document_text": "reference",
})
```

## Run Relevance Classification

```python
from phoenix.evals import LLM, async_evaluate_dataframe
from phoenix.evals.metrics import DocumentRelevanceEvaluator

llm = LLM(provider="openai", model="gpt-4")
relevance_evaluator = DocumentRelevanceEvaluator(llm=llm)

evals_df = await async_evaluate_dataframe(dataframe=df_sample, evaluators=[relevance_evaluator], concurrency=10)
relevance_classifications = evals_df["document_relevance_score"].str["label"].tolist()
choices = relevance_evaluator.CHOICES
```

## Evaluate Results

```python
true_labels = df_sample["relevant"].map({True: "relevant", False: "unrelated"}).tolist()

print(classification_report(true_labels, relevance_classifications, labels=choices))
confusion_matrix = ConfusionMatrix(
    actual_vector=true_labels, predict_vector=relevance_classifications, classes=choices
)
confusion_matrix.plot(
    cmap=plt.colormaps["Blues"],
    number_label=True,
    normalized=True,
)
```

<Frame>
  <img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/relevance-classification-cookbook.png" />
</Frame>

## Get Explanations

```python
relevance_classifications_df = await async_evaluate_dataframe(
    dataframe=df_sample.sample(n=5),
    evaluators=[relevance_evaluator],
    concurrency=10,
)
relevance_classifications_df["label"] = relevance_classifications_df["document_relevance_score"].str[
    "label"
]
relevance_classifications_df["explanation"] = relevance_classifications_df[
    "document_relevance_score"
].str["explanation"]
```

## Compare Models

Run the same evaluation with different models:

```python
# GPT-3.5
llm_gpt35 = LLM(provider="openai", model="gpt-3.5-turbo")

# GPT-4 Turbo
llm_gpt4turbo = LLM(provider="openai", model="gpt-4-turbo-preview")
```
