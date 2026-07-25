---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/sdk-api-reference/python/arize-phoenix-evals.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.946073Z"
---
---
title: "arize-phoenix-evals"
description: Tooling to evaluate LLM applications including faithfulness, correctness, relevance, and more.
---

[![PyPI Version](https://img.shields.io/pypi/v/arize-phoenix-evals)](https://pypi.org/project/arize-phoenix-evals/)

Phoenix Evals provides:

* Built-in evaluators for common tasks (faithfulness, correctness, relevance, conciseness, and more)
* A unified `LLM` wrapper supporting OpenAI, Anthropic, Google, LiteLLM, and other providers
* Batch evaluation over pandas DataFrames with `async_evaluate_dataframe` (or sync `evaluate_dataframe`)
* Custom evaluator creation via `create_evaluator` decorator or `ClassificationEvaluator`
* Benchmark datasets for testing evaluator accuracy

## Installation

```sh
pip install "arize-phoenix-evals>=3"
```

Install the LLM vendor SDK for your chosen provider:

```sh
pip install openai  # or anthropic, google-generativeai, litellm, etc.
```

## Quick example

```python
import os
from phoenix.evals import LLM, async_evaluate_dataframe
from phoenix.evals.metrics import DocumentRelevanceEvaluator

os.environ["OPENAI_API_KEY"] = "<your-openai-key>"

llm = LLM(provider="openai", model="gpt-4o")
relevance_evaluator = DocumentRelevanceEvaluator(llm=llm)

# DataFrame must have columns matching the evaluator's input schema
# DocumentRelevanceEvaluator expects: 'input' (query) and 'output' (document)
results_df = await async_evaluate_dataframe(
    dataframe=df,
    evaluators=[relevance_evaluator],
    concurrency=10,
)
```

## Core API

| Symbol | Description |
| :----- | :---------- |
| `LLM(provider=..., model=...)` | Unified LLM wrapper for all supported providers |
| `evaluate_dataframe(dataframe, evaluators)` | Run evaluators over a DataFrame (sync) |
| `async_evaluate_dataframe(dataframe, evaluators)` | Async variant with concurrency control |
| `create_evaluator(name, kind=...)` | Decorator to turn a function into an `Evaluator` |
| `ClassificationEvaluator(name, prompt_template, llm, choices)` | Custom classification evaluator for LLM-as-a-judge tasks |
| `bind_evaluator(evaluator, input_mapping)` | Bind field mappings to an evaluator |

## Built-in evaluators

All built-in evaluators live in `phoenix.evals.metrics` and accept `llm: LLM` as their first argument:

| Evaluator | Input fields | Labels |
| :-------- | :----------- | :----- |
| `FaithfulnessEvaluator` | `input`, `output`, `context` | faithful / unfaithful |
| `CorrectnessEvaluator` | `input`, `output` | correct / incorrect |
| `DocumentRelevanceEvaluator` | `input`, `output` | relevant / unrelated |
| `ConcisenessEvaluator` | `input`, `output` | concise / verbose / too_concise |
| `RefusalEvaluator` | `input`, `output` | refusal / no_refusal |
| `ToolSelectionEvaluator` | `input`, `output`, `tool_name`, `expected_tool` | correct / incorrect |
| `ToolInvocationEvaluator` | `input`, `tool_name`, `tool_call_args` | correct / incorrect |
| `ToolResponseHandlingEvaluator` | `input`, `tool_response`, `output` | good / bad |
| `exact_match` | `output`, `expected` | (code-based, no LLM) |
| `MatchesRegex(pattern=...)` | `output` | (code-based, no LLM) |

To learn more about LLM Evals, see the [evals quickstart](/docs/phoenix/evaluation/evals).

---

## Reference Documentation

<Card title="Full API Reference" icon="arrow-up-right-from-square" href="https://arize-phoenix.readthedocs.io/projects/evals/">
  Complete API documentation for evaluators, metrics, and LLM classification
</Card>
