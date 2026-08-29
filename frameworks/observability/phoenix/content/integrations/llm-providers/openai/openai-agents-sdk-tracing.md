---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/openai/openai-agents-sdk-tracing.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.942385Z"
---
# Openai Agents Sdk Tracing

---
title: "OpenAI Agents SDK Tracing"
description: "Use Phoenix and OpenAI Agents SDK for powerful multi-agent tracing"
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

<Note>Looking for TypeScript? See the [TypeScript guide](/docs/phoenix/integrations/typescript/openai-agents).</Note>

## 1. Install

```bash
pip install openinference-instrumentation-openai-agents openai-agents
```

## 2. Set up Tracing

Add your OpenAI API key as an environment variable:

```shell
export OPENAI_API_KEY=[your_key_here]
```

<RegisterTracerPython projectName="agents" />

Run your `agents`code.

```python
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")
result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)
```

View your traces in Phoenix.

## Resources

* [Example notebook](https://colab.research.google.com/github/Arize-ai/phoenix/blob/c02f0e7d807129952afa5da430299aec32fafcc9/tutorials/evals/openai_agents_cookbook.ipynb#L4)


