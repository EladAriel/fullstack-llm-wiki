---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/python/guardrails-ai/guardrails-ai-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.858268Z"
---
# Guardrails Ai Tracing

---
title: "Guardrails AI Tracing"
description: Instrument LLM applications that use the Guardrails AI framework
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

<Frame>
<iframe src="https://cdn.iframe.ly/kZuhMOt" className="w-full h-full aspect-video"></iframe>
</Frame>

In this example we will instrument a small program that uses the [Guardrails AI](https://www.guardrailsai.com/) framework to protect their LLM calls.

## Install

```bash
pip install openinference-instrumentation-guardrails guardrails-ai
```

## Setup

<RegisterTracerPython projectName="my-llm-app" />

## Run Guardrails

From here, you can run Guardrails as normal:

```python
from guardrails import Guard
from guardrails.hub import TwoWords
import openai

guard = Guard().use(
    TwoWords(),
)
response = guard(
    llm_api=openai.chat.completions.create,
    prompt="What is another name for America?",
    model="gpt-3.5-turbo",
    max_tokens=1024,
)

print(response)
```

## Observe

Now that you have tracing setup, all invocations of underlying models used by Guardrails (completions, chat completions, embeddings) will be streamed to your running Phoenix for observability and evaluation. Additionally, Guards will be present as a new span kind in Phoenix.

## Resources

* [Example notebook](https://github.com/Arize-ai/dataset-embeddings-guardrails/blob/main/validator/arize_demo_dataset_embeddings_guard.ipynb)

* [OpenInference package](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-guardrails)


