---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/datasets-and-experiments/how-to-experiments.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.825450Z"
---
# How To Experiments

---
title: "How to: Experiments"
sidebarTitle: "Overview"
---

## Running Experiments

Phoenix supports two workflows for experiments: a UI-driven flow in the Playground and a programmatic SDK flow.

<CardGroup cols={2}>
  <Card title="Run Experiments in the UI" icon="flask" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/run-experiments#run-experiments-in-the-ui">
    Configure prompts and evaluators in the Playground and compare results.
  </Card>
  <Card title="Run Experiments with the SDK" icon="code" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/run-experiments#run-experiments-with-the-sdk">
    Run experiments programmatically with tasks and evaluators in code.
  </Card>
  <Card title="Run Experiments in the Background" icon="server" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/run-experiments-in-background">
    Start experiments from the Playground that keep running after you close the browser, and stop or resume them anytime.
  </Card>
</CardGroup>

## SDK Experiment Steps

<CardGroup cols={2}>
  <Card title="Upload a Dataset" icon="database" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/run-experiments#load-a-dataset">
    Load your test cases into Phoenix to use as inputs for experiments.
  </Card>
  <Card title="Create a Task" icon="play" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/run-experiments#create-a-task">
    Define the function or workflow you want to evaluate against your dataset.
  </Card>
  <Card title="Configure Evaluators" icon="gauge" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/run-experiments#define-evaluators">
    Set up the scoring criteria to assess your task outputs.
  </Card>
  <Card title="Run an Experiment" icon="rocket" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/run-experiments#run-an-experiment">
    Execute your task across all dataset examples and collect evaluation results.
  </Card>
  <Card title="Use Repetitions" icon="repeat" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/repetitions">
    Run tasks multiple times to measure variance and consistency.
  </Card>
  <Card title="Dataset Splits" icon="scissors" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/splits">
    Run experiments on specific subsets of your dataset.
  </Card>
</CardGroup>

## Using Evaluators

<CardGroup cols={2}>
  <Card title="LLM Evaluators" icon="brain" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/using-evaluators#llm-evaluators">
    Use LLM-as-a-judge to assess quality, correctness, and other criteria.
  </Card>
  <Card title="Code Evaluators" icon="code" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/using-evaluators#code-evaluators">
    Built-in heuristic evaluators like exact match, JSON distance, and regex.
  </Card>
  <Card title="Custom Evaluators" icon="wand-magic-sparkles" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/using-evaluators#custom-llm-evaluators">
    Build your own evaluation logic with custom prompts or code.
  </Card>
  <Card title="Dataset Evaluators" icon="clipboard-check" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/how-to-dataset-evaluators">
    Attach evaluators to datasets for automatic scoring during experiments.
  </Card>
</CardGroup>
