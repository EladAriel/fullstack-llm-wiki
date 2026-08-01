---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/examples/twelvelabs-video-agent.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.855296Z"
---
# Twelvelabs Video Agent

Example of a Pydantic AI agent that understands video using [TwelveLabs](https://twelvelabs.io) Pegasus.

Demonstrates:

- [tools](../tools.md)
- [agent dependencies](../dependencies.md)
- wrapping a third-party multimodal API as a tool

In this case the idea is a "video analyst" agent — the user asks questions about a video
(given its URL), and the agent uses the `analyze_video` tool to call TwelveLabs Pegasus,
a video-understanding model, to answer. The LLM decides *what* to ask about the video, and
Pegasus does the actual video understanding.

## Running the Example

You'll need a TwelveLabs API key set via `TWELVELABS_API_KEY`. You can grab a free key at
[twelvelabs.io](https://twelvelabs.io) — there's a generous free tier.

The example agent runs on `openai:gpt-5-mini`, so you'll also need an OpenAI API key set via
`OPENAI_API_KEY`.

Optionally set `VIDEO_URL` to point the agent at your own publicly-accessible video;
otherwise a short public sample clip is used.

With [dependencies installed and environment variables set](./setup.md#usage), run:

```bash
python/uv-run -m pydantic_ai_examples.twelvelabs_video_agent
```

## Example Code
```snippet {path="/examples/pydantic_ai_examples/twelvelabs_video_agent.py"}```
