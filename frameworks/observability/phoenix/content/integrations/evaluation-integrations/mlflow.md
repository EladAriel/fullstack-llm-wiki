---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/evaluation-integrations/mlflow.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.917620Z"
---
# Mlflow

---
title: "MLflow"
description: "Use Phoenix evaluators as MLflow scorers for GenAI evaluation workflows."
---

[MLflow](https://mlflow.org/) includes built-in support for Phoenix evaluators through its third-party scorer interface. This allows Phoenix users to run their existing evaluation metrics within MLflow's `mlflow.genai.evaluate()` pipeline alongside experiment tracking and model management.

## Using Phoenix Evaluators in MLflow

Phoenix evaluators such as `Hallucination`, `QACorrectness`, and `Toxicity` can be used directly as MLflow scorers:

```python
from mlflow.genai.scorers.phoenix import Hallucination, QACorrectness

import mlflow

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="openai:/gpt-4o"),
        QACorrectness(model="openai:/gpt-4o"),
    ],
)
```

For details on available scorers and configuration, see the [MLflow Phoenix integration docs](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/third-party/phoenix.html).
