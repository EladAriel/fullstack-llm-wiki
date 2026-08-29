---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/vertexai/vertexai-evals.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.944333Z"
---
# Vertexai Evals

---
title: "VertexAI Evals"
description: Configure and run VertexAI for evals
---

### Using Google Vertex AI with Phoenix Evals

<Info>
Requires `google-genai`

```sh
pip install "arize-phoenix-evals>=3" google-genai
```
</Info>

Create an `LLM` instance with the Google provider:

```python
from phoenix.evals import LLM

llm = LLM(provider="google", model="gemini-2.0-flash")
```

The `LLM` wrapper reads your API key from the `GOOGLE_API_KEY` environment variable, or you can authenticate via Application Default Credentials for Vertex AI.

### Using with evaluators

```python
from phoenix.evals import LLM, evaluate_dataframe
from phoenix.evals.metrics import FaithfulnessEvaluator

llm = LLM(provider="google", model="gemini-2.0-flash")
evaluator = FaithfulnessEvaluator(llm=llm)

results_df = evaluate_dataframe(dataframe=df, evaluators=[evaluator])
```
