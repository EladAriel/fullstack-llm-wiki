---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/evaluation-integrations/mlflow.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.846861Z"
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
