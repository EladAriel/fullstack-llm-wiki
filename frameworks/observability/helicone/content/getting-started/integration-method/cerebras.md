---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/cerebras.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.226267Z"
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
