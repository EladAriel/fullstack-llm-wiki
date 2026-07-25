---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/instructor/javascript.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.210182Z"
---
# Javascript

---
title: "Instructor JavaScript SDK Integration"
sidebarTitle: "JavaScript"
description: "Use Instructor's JavaScript SDK to log your LLM calls in Helicone."
"twitter:title": "Instructor JavaScript SDK Integration - Helicone OSS LLM Observability"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

[Instructor](https://useinstructor.com/) is a popular framework for extracting structured output from text using LLMs. Here's how you can use Helicone to track your calls while using Instructor:

<Steps>
  <Step title="Follow useinstructor.com to get setup with Instructor's JS SDK.">
  </Step>
  <Step title="Modify the base url and add a Helicone-Auth header">
<CodeGroup>

```javascript Instructor SDK
const oai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: "https://oai.helicone.ai/v1",
  defaultHeaders: {
    "Helicone-Auth": "Bearer " + process.env.HELICONE_API_KEY
  }
})
// ... Call OpenAI using Instructor
```
</CodeGroup>

  </Step>
  <Step title="Call OpenAI using Instructor and see the logs on Helicone.">
  </Step>
</Steps>