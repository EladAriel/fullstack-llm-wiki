---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/vertexai/vertexai-evals.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.848419Z"
---
# Vertexai Evals

---
title: "VertexAI Evals"
description: Configure and run VertexAI for evals
---

### Using Google Vertex AI with Phoenix Evals

<Info>
Requires `google-generativeai`

```sh
pip install "arize-phoenix-evals>=3" google-generativeai
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
