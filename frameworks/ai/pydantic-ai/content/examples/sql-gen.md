---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/examples/sql-gen.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.856362Z"
---
# SQL Generation

Example demonstrating how to use Pydantic AI to generate SQL queries based on user input.

Demonstrates:

- [dynamic system prompt](../agent.md#system-prompts)
- [structured `output_type`](../output.md#structured-output)
- [output validation](../output.md#output-validator-functions)
- [agent dependencies](../dependencies.md)

## Running the Example

The resulting SQL is validated by running it as an `EXPLAIN` query on PostgreSQL. To run the example, you first need to run PostgreSQL, e.g. via Docker:

```bash
docker run --rm -e POSTGRES_PASSWORD=postgres -p 54320:5432 postgres
```

_(we run postgres on port `54320` to avoid conflicts with any other postgres instances you may have running)_

With [dependencies installed and environment variables set](./setup.md#usage), run:

```bash
python/uv-run -m pydantic_ai_examples.sql_gen
```

or to use a custom prompt:

```bash
python/uv-run -m pydantic_ai_examples.sql_gen "find me errors"
```

This model uses `gemini-3-flash-preview` by default since Gemini is good at single shot queries of this kind.

## Example Code

```snippet {path="/examples/pydantic_ai_examples/sql_gen.py"}```
