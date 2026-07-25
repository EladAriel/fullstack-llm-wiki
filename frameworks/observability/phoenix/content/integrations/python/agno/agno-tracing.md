---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/python/agno/agno-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.862071Z"
---
# Agno Tracing

---
title: "Agno Tracing"
description: "Phoenix provides seamless observability and tracing for Agno agents through the OpenInference instrumentation package. This integration automatically captures agent interactions, tool usage, reasoning steps, and multi-agent conversations, giving you complete visibility into your Agno applications. Monitor performance, debug issues, and evaluate agent behavior in real-time as your agents execute complex workflows and collaborate in teams."
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

Agno is a lightweight, high-performance Python framework for building AI agents with tools, memory, and reasoning capabilities. It enables developers to create autonomous agents that can perform complex tasks, access knowledge bases, and collaborate in multi-agent teams. With support for 23+ model providers and lightning-fast performance (\~3μs instantiation), Agno is designed for production-ready AI applications.
<Frame caption="Agno Traces in Phoenix">
  <img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/phoenix-docs-images/agno-example-trace.png" />
</Frame>

## Key Features

* **Model Agnostic**: Connect to OpenAI, Anthropic, Google, and 20+ other providers

* **Lightning Fast**: Agents instantiate in \~3μs with minimal memory footprint

* **Built-in Reasoning**: First-class support for chain-of-thought and reasoning models

* **Multi-Modal**: Native support for text, image, audio, and video processing

* **Agentic RAG**: Advanced retrieval-augmented generation with hybrid search

* **Multi-Agent Teams**: Coordinate multiple agents for complex workflows

* **Production Ready**: Pre-built FastAPI routes and monitoring capabilities

## Install

```bash
pip install openinference-instrumentation-agno agno
```

## Setup

<RegisterTracerPython projectName="my-llm-app" />

## Run Agno

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    markdown=True,
    debug_mode=True,
)

agent.run("What is currently trending on Twitter?")
```

## Observe

Now that you have tracing setup, all invocations of Agno agents will be streamed to Phoenix for observability and evaluation.

## Resources

* [OpenInference package](https://pypi.org/project/openinference-instrumentation-agno/)

* [Example](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-agno)


