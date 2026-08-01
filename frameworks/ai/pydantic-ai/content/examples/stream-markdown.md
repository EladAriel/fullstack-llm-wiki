---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/examples/stream-markdown.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.854927Z"
---
# Stream Markdown

This example shows how to stream markdown from an agent, using the [`rich`](https://github.com/Textualize/rich) library to highlight the output in the terminal.

It'll run the example with both OpenAI and Google Gemini models if the required environment variables are set.

Demonstrates:

* [streaming text responses](../output.md#streaming-text)

## Running the Example

With [dependencies installed and environment variables set](./setup.md#usage), run:

```bash
python/uv-run -m pydantic_ai_examples.stream_markdown
```

## Example Code

```snippet {path="/examples/pydantic_ai_examples/stream_markdown.py"}```
