---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/anthropic/python.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.353766Z"
---
# Python

---
title: "Anthropic Python SDK Integration"
sidebarTitle: "Python"
description: "Use Anthropic's Python SDK to integrate with Helicone to log your Anthropic LLM usage."
"twitter:title": "Anthropic Python SDK Integration - Helicone OSS LLM Observability"
icon: "python"
iconType: "solid"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## Proxy Integration

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Set HELICONE_API_KEY as an environment variable">
```Python
export HELICONE_API_KEY=<your API key>
```

  </Step>
  <Step title="Modify the base path and add a Helicone-Auth header">
<CodeGroup>

```Python example.py
import anthropic
import os

client = anthropic.Anthropic(
  api_key=os.environ.get("ANTHROPIC_API_KEY"),
  base_url="https://anthropic.helicone.ai",
  default_headers={
    "Helicone-Auth": f"Bearer {os.environ.get("HELICONE_API_KEY")}",
  },
)

client.messages.create(
  model="claude-3-opus-20240229",
  max_tokens=1024,
  messages=[
    {"role": "user", "content": "Hello, world"}
  ]
)
```

</CodeGroup>
  </Step>
</Steps>
