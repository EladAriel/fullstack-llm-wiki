---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/cerebras.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.324815Z"
---
# Cerebras

---
title: "Cerebras Integration"
sidebarTitle: "Cerebras"
description: "Connect Helicone with Cerebras, a platform for running open-source language models. Monitor and optimize your AI applications using Cerebras' powerful models through a simple base_url configuration."
"twitter:title": "Cerebras Integration - Helicone OSS LLM Observability"
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

You can seamlessly integrate Helicone with your OpenAI compatible models that are deployed on Cerebras.

The integration process closely mirrors the [proxy approach](/integrations/openai/javascript). The only distinction lies in the modification of the base_url to point to the dedicated Cerebras endpoint `https://cerebras.helicone.ai/v1`.

```bash
base_url="https://cerebras.helicone.ai/v1"
```

Please ensure that the base_url is correctly set to ensure successful integration.
