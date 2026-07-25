---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/datasets-and-experiments/how-to-datasets.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.826091Z"
---
# How To Datasets

---
title: "How to: Datasets"
sidebarTitle: "Overview"
description: Datasets are critical assets for building robust prompts, evals, fine-tuning,
---

## How to create datasets

Datasets are critical assets for building robust prompts, evals, fine-tuning, and much more. Phoenix allows you to build datasets manually, programmatically, or from files.

<CardGroup cols={2}>
  <Card title="Create datasets from CSV" href="/docs/phoenix/datasets-and-experiments/how-to-datasets/creating-datasets#from-csv" icon="file-csv" description="CSV dataset import"/>
  <Card title="Create datasets from JSONL" href="/docs/phoenix/datasets-and-experiments/how-to-datasets/creating-datasets#from-jsonl" icon="file-lines" description="JSONL dataset import"/>
  <Card title="Create datasets from Pandas" href="/docs/phoenix/datasets-and-experiments/how-to-datasets/creating-datasets#from-pandas" icon="table" description="Pandas dataframe import"/>
  <Card title="Create datasets from spans" href="/docs/phoenix/datasets-and-experiments/how-to-datasets/creating-datasets#from-spans" icon="route" description="Build datasets from spans"/>
  <Card title="Create datasets using synthetic data" href="/docs/phoenix/datasets-and-experiments/how-to-datasets/creating-datasets#synthetic-data" icon="wand-magic-sparkles" description="Generate synthetic datasets"/>
</CardGroup>


## Exporting datasets

Export datasets for offline analysis, evals, and fine-tuning.

* [Exporting to CSV](/docs/phoenix/datasets-and-experiments/how-to-datasets/exporting-datasets#exporting-to-csv) - how to quickly download a dataset to use elsewhere

* [Exporting to OpenAI Ft](/docs/phoenix/datasets-and-experiments/how-to-datasets/exporting-datasets#exporting-for-fine-tuning) - want to fine tune an LLM for better accuracy and cost? Export llm examples for fine-tuning.

* [Exporting to OpenAI Evals](/docs/phoenix/datasets-and-experiments/how-to-datasets/exporting-datasets#exporting-openai-evals) - have some good examples to use for benchmarking of llms using OpenAI evals? export to OpenAI evals format.

