---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/groq/curl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.206916Z"
---
# Curl

---
title: "Groq cURL Integration"
sidebarTitle: "cURL"
description: "Use cURL to integrate Groq with Helicone to log your Groq usage."
"twitter:title": "Groq cURL Integration - Helicone OSS LLM Observability"
icon: "code"
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

```cURL CLI example
curl -X POST "https://groq.staging.helicone.ai/openai/v1/chat/completions" \
     -H "Authorization: Bearer $GROQ_API_KEY" \
     -H "Helicone-Auth: Bearer $HELICONE_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"messages": [{"role": "user", "content": "Explain the importance of fast language models"}], "model": "llama3-8b-8192"}'
```

</CodeGroup>

  </Step>
</Steps>
