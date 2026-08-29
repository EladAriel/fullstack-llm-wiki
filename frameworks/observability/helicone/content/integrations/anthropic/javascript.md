---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/anthropic/javascript.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.353064Z"
---
# Javascript

---
title: "Anthropic JavaScript SDK Integration"
sidebarTitle: "JavaScript"
description: "Use Anthropic's JavaScript SDK to integrate with Helicone to log your Anthropic LLM usage."
"twitter:title": "Anthropic JavaScript SDK Integration - Helicone OSS LLM Observability"
icon: "js"
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
```javascript
HELICONE_API_KEY=<your API key>
```
  </Step>
  <Step title="Modify the base path and add a Helicone-Auth header">
<CodeGroup>

```javascript example.js
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  baseURL: "https://anthropic.helicone.ai",
  apiKey: process.env.ANTHROPIC_API_KEY,
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
  },
});

await anthropic.messages.create({
  model: "claude-3-opus-20240229",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello, world" }],
});
```

</CodeGroup>

  </Step>
</Steps>
