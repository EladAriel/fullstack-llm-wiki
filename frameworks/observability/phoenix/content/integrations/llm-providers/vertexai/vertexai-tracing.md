---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/vertexai/vertexai-tracing.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.944136Z"
---
# Vertexai Tracing

---
title: "VertexAI Tracing"
description: Instrument LLM calls made using VertexAI's SDK via the VertexAIInstrumentor
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

The VertexAI SDK can be instrumented using the [`openinference-instrumentation-vertexai`](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-vertexai) package.

## Install

```bash
pip install openinference-instrumentation-vertexai vertexai
```

## Setup

See Google's [guide](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal#expandable-1) on setting up your environment for the Google Cloud AI Platform. You can also store your Project ID in the `CLOUD_ML_PROJECT_ID` environment variable.

<RegisterTracerPython projectName="my-llm-app" />

## Run VertexAI

```python
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(location="us-central1")
model = GenerativeModel("gemini-1.5-flash")

print(model.generate_content("Why is sky blue?").text)
```

## Observe

Now that you have tracing setup, all invocations of Vertex models will be streamed to your running Phoenix for observability and evaluation.

## Resources

* [Example notebook](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-vertexai/examples/basic_generation.py)

* [OpenInference package](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-vertexai)

* [Working examples](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-vertexai/examples)


