---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/python/llamaindex/llamaindex-workflows-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.859628Z"
---
# Llamaindex Workflows Tracing

---
title: "LlamaIndex Workflows Tracing"
description: How to use the python LlamaIndexInstrumentor to trace LlamaIndex Workflows
---

[LlamaIndex Workflows](https://www.llamaindex.ai/blog/introducing-workflows-beta-a-new-way-to-create-complex-ai-applications-with-llamaindex) are a subset of the LlamaIndex package specifically designed to support agent development.

<Tip>
Our LlamaIndexInstrumentor automatically captures traces for LlamaIndex Workflows agents. If you've already enabled that instrumentor, you do not need to complete the steps below.

</Tip>

<Info>
We recommend using `llama_index >= 0.11.0`

</Info>

## Install

```bash
pip install openinference-instrumentation-llama_index
```

## Setup

Initialize the LlamaIndexInstrumentor before your application code. This instrumentor will trace both LlamaIndex Workflows calls, as well as calls to the general LlamaIndex package.

```python
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from phoenix.otel import register

tracer_provider = register()
LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)
```

## Run LlamaIndex Workflows

By instrumenting LlamaIndex, spans will be created whenever an agent is invoked and will be sent to the Phoenix server for collection.

## Observe

Now that you have tracing setup, all invocations of chains will be streamed to your running Phoenix for observability and evaluation.

## Resources

* [Example project](https://github.com/Arize-ai/phoenix/tree/main/examples/llamaindex-workflows-research-agent)

* [OpenInference package](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-llama-index)


