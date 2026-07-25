---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/openai/openai-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.848921Z"
---
# Openai Tracing

---
title: "OpenAI Tracing"
description: "Phoenix provides auto-instrumentation for the [OpenAI Python Library](https://github.com/openai/openai-python)."
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

<Info>
**Note***: This instrumentation also works with Azure OpenAI

</Info>

## Install

```bash
pip install openinference-instrumentation-openai openai
```

## Setup

Add your OpenAI API key as an environment variable:

```shell
export OPENAI_API_KEY=[your_key_here]
```

<RegisterTracerPython projectName="my-llm-app" />

## Run OpenAI

```python
import openai

client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Write a haiku."}],
)
print(response.choices[0].message.content)
```

## Observe

Now that you have tracing setup, all invocations of OpenAI (completions, chat completions, embeddings) will be streamed to your running Phoenix for observability and evaluation.

## Resources

* [Example notebook](https://github.com/Arize-ai/phoenix/blob/main/tutorials/tracing/openai_tracing_tutorial.ipynb)

* [OpenInference package](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-openai)

* [Working examples](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-openai/examples)


