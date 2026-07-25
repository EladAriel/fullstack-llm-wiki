---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/platforms/prompt-flow/prompt-flow-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.856496Z"
---
# Prompt Flow Tracing

---
title: "Prompt Flow Tracing"
description: Create flows using Microsoft PromptFlow and send their traces to Phoenix
---

This integration will allow you to trace [Microsoft PromptFlow](https://github.com/microsoft/promptflow) flows and send their traces into[`arize-phoenix`](https://github.com/Arize-ai/phoenix).

## Install

```bash
pip install promptflow
```

## Setup

Set up the OpenTelemetry endpoint to point to Phoenix and use Prompt flow's `setup_exporter_from_environ` to start tracing any further flows and LLM calls.

```swift
import os
from opentelemetry.sdk.environment_variables import OTEL_EXPORTER_OTLP_ENDPOINT
from promptflow.tracing._start_trace import setup_exporter_from_environ

endpoint = f"{os.environ["PHOENIX_COLLECTOR_ENDPOINT]}/v1/traces" # replace with your Phoenix endpoint if self-hosting
os.environ[OTEL_EXPORTER_OTLP_ENDPOINT] = endpoint
setup_exporter_from_environ()
```

## Run PromptFlow

Proceed with creating Prompt flow flows as usual. See this [example notebook](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-promptflow/examples/chat_flow_example_to_phoenix.ipynb) for inspiration.

## Observe

You should see the spans render in Phoenix as shown in the below screenshots.

## Resources

* [Example Notebook](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-promptflow/examples/chat_flow_example_to_phoenix.ipynb)


