---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/02-2026/02-11-2026-custom-providers.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.859162Z"
---
---
title: "Release Notes"
---

# Custom Providers for Playground and Prompts

February 11, 2026

Phoenix now supports **custom providers** for OpenAI, Azure OpenAI, Anthropic, AWS Bedrock, and Google GenAI. Custom providers let you store provider credentials and routing configuration on the server and reuse them across the playground and saved prompt versions.

![Custom provider configuration in Phoenix](https://storage.googleapis.com/arize-phoenix-assets/assets/images/custom-provider-config.png)

**Key capabilities:**

- **Centralized configuration:** Manage provider credentials and routing in Settings and reuse them across the playground and prompt versions.
- **SDK-specific authentication:** Support API keys, Azure AD token providers, or default credentials (Azure/AWS) depending on the SDK.
- **Model selection integration:** Custom providers show up in model menus as their own provider group and inherit model listings from the underlying SDK.
- **Request-level overrides:** Continue to supply custom request headers per prompt while using custom provider configuration for routing and authentication.

To get started, open **Settings → AI Providers → Custom Providers**, create a provider configuration, and select it from the model menu in the playground.
