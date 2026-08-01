---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/examples/pydantic-model.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.855650Z"
---
# Pydantic Model

Simple example of using Pydantic AI to construct a Pydantic model from a text input.

Demonstrates:

- [structured `output_type`](../output.md#structured-output)

## Running the Example

With [dependencies installed and environment variables set](./setup.md#usage), run:

```bash
python/uv-run -m pydantic_ai_examples.pydantic_model
```

This examples uses `openai:gpt-5` by default, but it works well with other models, e.g. you can run it
with Gemini using:

```bash
PYDANTIC_AI_MODEL=gemini-3-pro-preview python/uv-run -m pydantic_ai_examples.pydantic_model
```

(or `PYDANTIC_AI_MODEL=gemini-3-flash-preview ...`)

## Example Code

```snippet {path="/examples/pydantic_ai_examples/pydantic_model.py"}```
