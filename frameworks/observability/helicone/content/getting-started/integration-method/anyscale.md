---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/anyscale.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.225895Z"
---
# Anyscale

---
title: "Anyscale Integration"
sidebarTitle: "Anyscale"
description: "Connect Helicone with any LLM deployed on Anyscale, including Llama, Mistral, Gemma, and GPT."
"twitter:title": "Anyscale Integration - Helicone OSS LLM Observability"
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

You can use Helicone with your OpenAI compatible models that are deployed on Anyscale.

Follow the Helicone integration as normal in the [proxy approach](/getting-started/integration-method/openai-proxy) but add the following header.

```bash
Helicone-OpenAI-API-Base: https://api.endpoints.anyscale.com/v1
```

This will route traffic through Helicone to your Anyscale deployment.
