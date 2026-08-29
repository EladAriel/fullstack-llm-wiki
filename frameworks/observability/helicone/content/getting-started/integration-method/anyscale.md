---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/anyscale.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.319717Z"
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
