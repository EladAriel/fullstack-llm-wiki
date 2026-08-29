---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/02-2026/02-12-2026-openai-responses-api-support.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.858034Z"
---
# 02 12 2026 Openai Responses Api Support

---
title: "OpenAI Responses API Type Support"
description: "Choose between Chat Completions and Responses API for OpenAI and Azure OpenAI."
---

Phoenix now supports selecting the **OpenAI API type** for OpenAI and Azure OpenAI calls in the Playground and custom providers.

**Key capabilities:**

- **API type selection:** Choose **Chat Completions** (`chat.completions.create`) or **Responses** (`responses.create`) per model configuration.
- **Custom provider support:** OpenAI and Azure OpenAI custom providers can be configured with an API type for consistent routing.
- **Parameter compatibility:** Phoenix maps shared invocation parameters to the chosen API type and filters unsupported fields automatically.

To get started, open the model configuration panel in the Playground and select an **OpenAI API type**. For server-managed setups, configure the API type in **Settings → AI Providers → Custom Providers**.
