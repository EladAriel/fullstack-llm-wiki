---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/python/strands-agents/strands-agents-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.859845Z"
---
---
title: "Strands Agents Tracing"
description: "Phoenix provides tracing support for Strands Agents through a span processor that transforms Strands' native OpenTelemetry spans into OpenInference format."
---

[Strands Agents](https://strandsagents.com/) is an open-source AI agent SDK that uses model-driven orchestration to build production-ready, multi-agent systems in a few lines of code. It supports many LLM providers (Amazon Bedrock, OpenAI, Anthropic, and more) and offers multi-agent patterns, custom tool creation, and native AWS integrations.

## Install

```bash
pip install arize-phoenix-otel openinference-instrumentation-strands-agents strands-agents openai
```

## Setup

Set your model provider API key as an environment variable. This example uses OpenAI:

```shell
export OPENAI_API_KEY=[your_key_here]
```

Strands Agents provides its own OpenTelemetry-based telemetry. The `openinference-instrumentation-strands-agents` package adds a span processor that transforms Strands' native spans into OpenInference format for Phoenix.

```python
from phoenix.otel import HTTPSpanExporter, SimpleSpanProcessor, register
from openinference.instrumentation.strands_agents import StrandsAgentsToOpenInferenceProcessor

# Strands reads the global tracer provider, so start with register() to make
# Phoenix's provider the process-wide default.
tracer_provider = register(
    project_name="strands-agents",
)

# This processor rewrites Strands' native spans into OpenInference spans, so it
# must run before the Phoenix exporter that sends spans to your collector.
tracer_provider.add_span_processor(StrandsAgentsToOpenInferenceProcessor())
tracer_provider.add_span_processor(
    SimpleSpanProcessor(HTTPSpanExporter()),
)
```

<Info>
**Processor ordering matters.** `register()` sets Phoenix as the global tracer provider for Strands, but it also installs Phoenix's default exporter-backed processor immediately. Replace that default with `StrandsAgentsToOpenInferenceProcessor()`, then add the Phoenix exporter back after it so Phoenix receives the transformed OpenInference spans.
</Info>

## Run Strands Agents

```python
from strands import Agent
from strands.models.openai import OpenAIModel

model = OpenAIModel(model_id="gpt-4o-mini")
agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant.",
)

result = agent("Explain the theory of relativity in simple terms.")
```

## Observe

Now that you have tracing setup, all invocations of Strands agents — including LLM calls, tool executions, and event loop cycles — will be streamed to your running Phoenix for observability and evaluation.

## Resources

* [OpenInference package](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-strands-agents)

* [Working examples](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-strands-agents/examples)

* [Strands Agents documentation](https://strandsagents.com/docs/user-guide/quickstart/overview/)
