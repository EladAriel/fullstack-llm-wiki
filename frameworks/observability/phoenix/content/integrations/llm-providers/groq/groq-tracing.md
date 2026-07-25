---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/groq/groq-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.849956Z"
---
# Groq Tracing

---
title: "Groq Tracing"
description: Instrument LLM applications built with Groq
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

[Groq](http://groq.com/) provides low latency and lightning-fast inference for AI models. Arize supports instrumenting Groq API calls, including role types such as system, user, and assistant messages, as well as tool use. You can create a free GroqCloud account and [generate a Groq API Key here](https://console.groq.com) to get started.

## Install

```bash
pip install openinference-instrumentation-groq groq
```

## Setup

<RegisterTracerPython projectName="my-llm-app" />

## Run Groq

A simple Groq application that is now instrumented

```python
import os
from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="mixtral-8x7b-32768",
)
print(chat_completion.choices[0].message.content)
```

## Observe

Now that you have tracing setup, all invocations of pipelines will be streamed to your running Phoenix for observability and evaluation.

## Resources:

* [Example Chat Completions](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-groq/examples/chat_completions.py)

* [Example Async Chat Completions](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-groq/examples/async_chat_completions.py)

* [Tutorial](https://github.com/Arize-ai/phoenix/blob/main/tutorials/tracing/groq_tracing_tutorial.ipynb)

* [OpenInference package](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-groq)


