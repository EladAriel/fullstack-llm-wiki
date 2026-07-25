---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/ai-gateway/post-v1-responses.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.255835Z"
---
# Post V1 Responses

---
title: "Responses (Gateway)"
sidebarTitle: "Responses"
description: "Create responses via the AI Gateway"
openapi: post /v1/responses
---

This request schema applies when using the Helicone AI Gateway with pass‑through billing (credits). In BYOK mode, the standard OpenAI Responses API schema is allowed. The schema is defined based on fields that are stable across all provider-model mappings.

[Learn more about pass‑through billing vs BYOK](/gateway/provider-routing).

<RequestExample>

```bash cURL
curl https://ai-gateway.helicone.ai/v1/responses \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "input": "Say hello in one sentence."
  }'
```

```typescript TypeScript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://ai-gateway.helicone.ai/v1",
  apiKey: process.env.HELICONE_API_KEY,
});

const response = await client.responses.create({
  model: "gpt-4o-mini",
  input: "Say hello in one sentence.",
});
```

```python Python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://ai-gateway.helicone.ai/v1",
    api_key=os.environ.get("HELICONE_API_KEY"),
)

response = client.responses.create(
    model="gpt-4o-mini",
    input="Say hello in one sentence.",
)
```

</RequestExample>
