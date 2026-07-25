---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/groq/python.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.206704Z"
---
# Python

---
title: "Groq Python SDK Integration"
sidebarTitle: "Python"
description: "Use Groq's Python SDK to integrate with Helicone to log your Groq usage."
"twitter:title": "Groq Python SDK Integration - Helicone OSS LLM Observability"
icon: "python"
iconType: "solid"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

<Note>

Depending on the model you are using, you may need to adjust the base URL.
For most cases with Groq, the base URL will be `https://groq.helicone.ai/openai/v1`.

However, in some cases, you may need to use `https://groq.helicone.ai/v1`.

</Note>

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Set HELICONE_API_KEY as an environment variable">
```javascript
HELICONE_API_KEY=<your API key>
```
  </Step>
  <Step title="Modify the base path and add a Helicone-Auth header">
<CodeGroup>

```Python Groq SDK
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://groq.helicone.ai/openai/v1",
    default_headers={
        "Helicone-Auth": f"Bearer {os.environ.get('HELICONE_API_KEY')}",
    }
)
```

</CodeGroup>

  </Step>
</Steps>
