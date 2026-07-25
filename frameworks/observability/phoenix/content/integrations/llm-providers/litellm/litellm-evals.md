---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/litellm/litellm-evals.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.850169Z"
---
# Litellm Evals

---
title: "LiteLLM Evals"
description: Configure and run LiteLLM for evals
---

### Using LiteLLM with Phoenix Evals

<Info>
Requires `litellm>=1.0.3`

```sh
pip install "arize-phoenix-evals>=3" litellm
```
</Info>

Create an `LLM` instance with the LiteLLM provider:

```python
from phoenix.evals import LLM

llm = LLM(provider="litellm", model="gpt-4o")
```

LiteLLM supports [100+ providers](https://docs.litellm.ai/docs/providers). Set the appropriate environment variables for your provider before creating the LLM. For provider-specific configuration, see [LiteLLM provider params](https://docs.litellm.ai/docs/completion/input#provider-specific-params).

### Ollama example

```python
import os
from phoenix.evals import LLM

os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

llm = LLM(provider="litellm", model="ollama/llama3")
```

### Using with evaluators

```python
from phoenix.evals import LLM, evaluate_dataframe
from phoenix.evals.metrics import FaithfulnessEvaluator

llm = LLM(provider="litellm", model="ollama/llama3")
evaluator = FaithfulnessEvaluator(llm=llm)

results_df = evaluate_dataframe(dataframe=df, evaluators=[evaluator])
```
