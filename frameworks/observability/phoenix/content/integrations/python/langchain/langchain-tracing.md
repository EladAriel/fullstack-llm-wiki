---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/python/langchain/langchain-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.858721Z"
---
# Langchain Tracing

---
title: "LangChain Tracing"
description: How to use the python LangChainInstrumentor to trace LangChain
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

Phoenix has first-class support for [LangChain](https://langchain.com/) applications.

## Install

```bash
pip install openinference-instrumentation-langchain langchain_openai
```

## Setup

<RegisterTracerPython projectName="my-llm-app" />

## Run LangChain

By instrumenting LangChain, spans will be created whenever a chain is run and will be sent to the Phoenix server for collection.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("{x} {y} {z}?").partial(x="why is", z="blue")
chain = prompt | ChatOpenAI(model_name="gpt-3.5-turbo")
chain.invoke(dict(y="sky"))
```

## Observe

Now that you have tracing setup, all invocations of chains will be streamed to your running Phoenix for observability and evaluation.

## Resources

* [Example notebook](https://colab.research.google.com/github/Arize-ai/phoenix/blob/main/tutorials/tracing/langchain_tracing_tutorial.ipynb)

* [OpenInference package](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-langchain)

* [Working examples](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-langchain/examples)


