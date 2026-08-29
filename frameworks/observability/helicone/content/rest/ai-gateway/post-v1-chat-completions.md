---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/ai-gateway/post-v1-chat-completions.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.294818Z"
---
# Post V1 Chat Completions

---
title: "Chat Completions (Gateway)"
sidebarTitle: "Chat Completions"
description: "Create chat completions via the AI Gateway"
openapi: post /v1/chat/completions
---

This request schema applies when using the Helicone AI Gateway with pass‑through billing (credits). In BYOK mode, the standard OpenAI Chat Completions schema is allowed. The schema is defined based on fields that are stable across all provider-model mappings.

[Learn more about pass‑through billing vs BYOK](/gateway/provider-routing).

<RequestExample>

```bash cURL
curl https://ai-gateway.helicone.ai/v1/chat/completions \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      { "role": "system", "content": "You are a helpful assistant." },
      { "role": "user", "content": "Say hello in one sentence." }
    ]
  }'
```

```typescript TypeScript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://ai-gateway.helicone.ai/v1",
  apiKey: process.env.HELICONE_API_KEY,
});

const response = await client.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Say hello in one sentence." },
  ],
});
```

```python Python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://ai-gateway.helicone.ai/v1",
    api_key=os.environ.get("HELICONE_API_KEY"),
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello in one sentence."},
    ],
)
```

</RequestExample>
