---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/groq/javascript.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.347636Z"
---
# Javascript

---
title: "Groq JavaScript SDK Integration"
sidebarTitle: "JavaScript"
description: "Use Groq's JavaScript SDK to integrate with Helicone to log your Groq usage."
"twitter:title": "Groq JavaScript SDK Integration - Helicone OSS LLM Observability"
icon: "js"
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

```javascript Groq SDK
const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,
  baseUrl: "https://groq.helicone.ai/openai/v1",
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
  },
});
```

</CodeGroup>

  </Step>
</Steps>
