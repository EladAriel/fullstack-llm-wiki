---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/anthropic/anthropic-evals.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.942816Z"
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
