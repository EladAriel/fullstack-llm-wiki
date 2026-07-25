---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/03-2025/03-07-2025-new-prompt-playground-evals-and-integration-support.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.890671Z"
---
# 03 07 2025 New Prompt Playground Evals And Integration Support

---
title: "03.07.2025: New prompt playground, evals, and integration support"
description: Available in Phoenix 8.9+
---

<Update label="03.07.2025">

## New Prompt Playground, Evals, And Integration Support

<Frame>
  <iframe 
    src="https://cdn.iframe.ly/GFVzMH7" 
    width={1000} 
    height={400}
    allowFullScreen
  />
</Frame>

New update overview:

* **Prompt Playground**: Now supports [GPT-4.5](https://github.com/Arize-ai/phoenix/issues/6629) & Anthropic Sonnet 3.7 and Thinking Budgets
* **Instrumentation**: SmolagentsInstrumentor to trace smolagents by Hugging Face
* **Evals**: o3 support, Audio & Multi-Modal Evaluations
* **Integrations**: Phoenix now supports LiteLLM Proxy & Cleanlabs evals

### Improvements and Bug Fixes 🐛

* [**Admin**](https://github.com/Arize-ai/phoenix/issues/6722)**:** Show percent used of DB
* [**Configuration**](https://github.com/Arize-ai/phoenix/issues/6664): Add environment variable for allocated DB storage capacity
* [**Tracing**](https://github.com/Arize-ai/phoenix/pull/6681): Delete selected traces
* [**Tracing**](https://github.com/Arize-ai/phoenix/pull/6665): Make trace tree more readable on smaller sizes
* [**Experiments**](https://github.com/Arize-ai/phoenix/pull/6708): Ensure type is correct on `run_experiment`
* [**Experiments**](https://github.com/Arize-ai/phoenix/pull/6642): Allow experiment run JSON downloads
* [**Python Client**](https://github.com/Arize-ai/phoenix/issues/6659): Add anthropic thinking config param
* [**Components**](https://github.com/Arize-ai/phoenix/pull/6679): Add ToggleButton
</Update>

