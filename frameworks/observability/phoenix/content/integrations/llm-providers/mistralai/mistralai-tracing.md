---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/mistralai/mistralai-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.852942Z"
---
# Mistralai Tracing

---
title: "MistralAI Tracing"
description: Instrument LLM calls made using MistralAI's SDK via the MistralAIInstrumentor
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

MistralAI is a leading provider for state-of-the-art LLMs. The MistralAI SDK can be instrumented using the [`openinference-instrumentation-mistralai`](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-mistralai) package.

## Install

```bash
pip install openinference-instrumentation-mistralai mistralai
```

## Setup

Set the `MISTRAL_API_KEY` environment variable to authenticate calls made using the SDK.

```javascript
export MISTRAL_API_KEY=[your_key_here]
```

<RegisterTracerPython projectName="my-llm-app" />

## Run Mistral

```python
import os

from mistralai import Mistral
from mistralai.models import UserMessage

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-tiny"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[UserMessage(content="What is the best French cheese?")],
)
print(chat_response.choices[0].message.content)
```

## Observe

Now that you have tracing setup, all invocations of Mistral (completions, chat completions, embeddings) will be streamed to your running Phoenix for observability and evaluation.

## Resources

* [Example notebook](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-mistralai/examples/chat_completions.py)

* [OpenInference package](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-mistralai)

* [Working examples](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-mistralai/examples)


