---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/faq/secret-vs-public-key.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.192969Z"
---
# Secret Vs Public Key

---
title: "Secret vs Public Key"
sidebarTitle: "Secret vs Public Key"
description: "Understanding the difference between secret and public API keys in Helicone. Learn about access levels, usage examples, and best practices."
"twitter:title": "Secret vs Public Key - Helicone OSS LLM Observability"
---

import QuestionsSection from "/snippets/questions-section.mdx";

| Key Type   | Access       | Path Auth       | Header Auth | REST API |
| ---------- | ------------ | --------------- | ----------- | -------- |
| **Public** | Write-Only   | Yes             | Yes         | No       |
| **Secret** | Read + Write | Not Recommended | Yes         | Yes      |

### Usage Examples

<CodeGroup>

```javascript Header Auth
import OpenAI from "openai";

// Use secret or public key
const openai = new OpenAI({
  apiKey: request.env.OPENAI_API_KEY,
  baseURL: "https://oai.helicone.ai/v1",
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${HELICONE_SECRET_API_KEY}`,
  },
});
```

```javascript Path Auth
import OpenAI from "openai";

// Use public key
const openai = new OpenAI({
  apiKey: request.env.OPENAI_API_KEY,
  baseURL: `https://oai.helicone.ai/${HELICONE_PUBLIC_API_KEY}/v1`,
});
```

</CodeGroup>

<Note>
  Ensure that secret keys are always kept secure and never exposed in
  client-side code.
</Note>

<QuestionsSection />
