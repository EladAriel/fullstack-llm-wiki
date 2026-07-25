---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/gateway/concepts/responses-api.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.276074Z"
---
# Responses Api

---
title: "Responses API"
description: "Use the OpenAI Responses API format through Helicone AI Gateway with your Helicone API key"
---

The Responses API is OpenAI's newer interface for conversational AI that supports advanced features like reasoning, tool use, and streaming. Helicone's AI Gateway supports the Responses API format for both OpenAI and Anthropic models.

## Quick Start

Use your Helicone API key and the AI Gateway base URL. Then call the OpenAI SDK's `responses.create` method as usual.

<CodeGroup>

```typescript TypeScript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.HELICONE_API_KEY,
  baseURL: "https://ai-gateway.helicone.ai/v1",
});

const response = await client.responses.create({
  model: "gpt-5",
  input: "Write a one-sentence bedtime story about a unicorn.",
});

console.log(response.output_text);
```

```python Python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("HELICONE_API_KEY"),
    base_url="https://ai-gateway.helicone.ai/v1",
)

response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn.",
)

print(response.output_text)
```

```bash
curl https://ai-gateway.helicone.ai/v1/responses \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5",
    "input": "Write a one-sentence bedtime story about a unicorn."
  }'
```

</CodeGroup>

<Note>
For Chat Completions usage and more background on the AI Gateway, see the
[AI Gateway Overview](/gateway/overview).
</Note>

## References

- OpenAI Responses guide: https://platform.openai.com/docs/guides/text
- Helicone AI Gateway overview: https://docs.helicone.ai/gateway/overview
