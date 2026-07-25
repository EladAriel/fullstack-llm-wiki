---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/anthropic/anthropic-evals.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.850563Z"
---
# Anthropic Evals

---
title: "Anthropic Evals"
sidebarTitle: "Anthropic Evals"
description: Configure and run Anthropic for evals
---

### Using Anthropic with Phoenix Evals

<Info>
Requires `anthropic`

```sh
pip install "arize-phoenix-evals>=3" anthropic
```
</Info>

Create an `LLM` instance with the Anthropic provider:

```python
from phoenix.evals import LLM

llm = LLM(provider="anthropic", model="claude-sonnet-4-20250514")
```

The `LLM` wrapper reads your API key from the `ANTHROPIC_API_KEY` environment variable, or you can pass it directly:

```python
llm = LLM(provider="anthropic", model="claude-sonnet-4-20250514", api_key="sk-ant-...")
```

### Using with evaluators

```python
from phoenix.evals import LLM, evaluate_dataframe
from phoenix.evals.metrics import FaithfulnessEvaluator

llm = LLM(provider="anthropic", model="claude-sonnet-4-20250514")
evaluator = FaithfulnessEvaluator(llm=llm)

results_df = evaluate_dataframe(dataframe=df, evaluators=[evaluator])
```
