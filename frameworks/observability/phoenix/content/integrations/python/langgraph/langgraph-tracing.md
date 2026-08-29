---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/python/langgraph/langgraph-tracing.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.934132Z"
---
# Langgraph Tracing

---
title: "LangGraph Tracing"
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

Phoenix has first-class support for [LangGraph](https://www.langchain.com/langgraph) applications.

<Info>
LangGraph is supported by our LangChain instrumentor. If you've already set up instrumentation with LangChain, you don't need to complete the set up below

</Info>

## Install

```bash
pip install openinference-instrumentation-langchain
```

Install the OpenInference Langchain library before your application code. Our LangChainInstrumentor works for both standard LangChain applications and for LangGraph agents.

## Setup

<RegisterTracerPython projectName="my-llm-app" />

## Run LangGraph

By instrumenting LangGraph, spans will be created whenever an agent is invoked and will be sent to the Phoenix server for collection.

## Observe

Now that you have tracing setup, all invocations of chains will be streamed to your running Phoenix for observability and evaluation.

## Resources

* [Example notebook](https://github.com/Arize-ai/phoenix/blob/main/tutorials/tracing/langgraph_agent_tracing_tutorial.ipynb)

* [OpenInference package](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-langchain)

* [Blog walkthrough](https://arize.com/blog/langgraph/)


