---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/groq/groq-tracing.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.940907Z"
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


