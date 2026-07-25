---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/openai/openai-agents-sdk-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.849745Z"
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


