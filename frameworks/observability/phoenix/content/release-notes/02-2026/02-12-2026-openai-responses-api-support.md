---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/02-2026/02-12-2026-openai-responses-api-support.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.888098Z"
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
