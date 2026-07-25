---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/11-2025/11-09-2025-openinference-typescript-2-0.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.885817Z"
---
# 11 09 2025 Openinference Typescript 2 0

---
title: "11.09.2025 OpenInference TypeScript 2.0"
---

<Frame>
  <img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/traced_agent.mp4" alt="traced agent.mp4" />
</Frame>

<Card title="TypeScript SDK API Reference" href="/docs/phoenix/sdk-api-reference/typescript/overview" icon="brackets-curly" description="TypeScript SDK reference"/>

* Added **easy manual instrumentation** with the same decorators, wrappers, and attribute helpers found in the Python `openinference-instrumentation` package.
* Introduced **function tracing utilities** that automatically create spans for sync/async function execution, including specialized wrappers for **chains**, **agents**, and **tools**.
* Added **decorator-based method tracing**, enabling automatic span creation on class methods via the `@observe` decorator.
* Expanded **attribute helper utilities** for standardized OpenTelemetry metadata creation, including helpers for **inputs/outputs**, **LLM operations**, **embeddings**, **retrievers**, and **tool definitions**.
* Overall, tracing workflows, agent behavior, and external tool calls is now significantly simpler and more consistent across languages.
