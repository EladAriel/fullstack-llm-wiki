---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/03-2025/03-14-2025-openai-agents-instrumentation.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.890123Z"
---
# 03 14 2025 Openai Agents Instrumentation

---
title: "03.14.2025: OpenAI agents instrumentation"
description: Available in Phoenix 8.13+
---

<Update label="03.14.2025">

## OpenAI Agents Instrumentation

<Frame>
  <iframe
    src="https://cdn.iframe.ly/sDk1x3T"
    width={1000}
    height={400}
    allowFullScreen
  />
</Frame>

We've introduced the **OpenAI Agents SDK** for Python which provides enhanced visibility into agent behavior and performance.

**Installation**

```bash
pip install openinference-instrumentation-openai-agents openai-agents
```

* Includes an OpenTelemetry Instrumentor that traces agents, LLM calls, tool usage, and handoffs.
* With minimal setup, use the `register` function to connect your app to Phoenix and view real-time traces of agent workflows.

### Walkthrough Video

<Frame>
  <iframe
    src="https://www.youtube.com/embed/iOGu7-HYm6s"
    width={1000}
    height={563}
    allowFullScreen
  />
</Frame>

For more details on a quick setup, check out our integration documentation:

<Card title="OpenAI Agents SDK | Phoenix" icon="book" href="/docs/phoenix/integrations/llm-providers/openai/openai-agents-sdk-tracing" horizontal description="OpenAI Agents SDK docs">
</Card>

### Improvements and Bug Fixes 🐛

* [**Prompt Playground**](https://github.com/Arize-ai/phoenix/issues/6788): Azure API key made optional, included specialized UI for thinking budget parameter
* [**Performance**](https://github.com/Arize-ai/phoenix/pull/6756): Make the spans table the default tab
* [**Components**](https://github.com/Arize-ai/phoenix/issues/6771): Added react-aria Tabs components
* [**Enhancement**](https://github.com/Arize-ai/phoenix/pull/6749): Download experiment runs and annotations as CSV
</Update>
