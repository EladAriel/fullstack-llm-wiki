---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/nvidia/dynamo.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.350958Z"
---
# Dynamo

---
title: "Nvidia Dynamo Integration"
sidebarTitle: "Dynamo"
description: "Use Nvidia Dynamo with Helicone for comprehensive logging and monitoring."
"twitter:title": "Nvidia Dynamo Integration - Helicone OSS LLM Observability"
icon: "server"
iconType: "solid"
---

import { strings } from "/snippets/strings.mdx";
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

Use Nvidia Dynamo or other OpenAI-compatible Nvidia inference providers with Helicone by routing through our gateway with custom headers.

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    ```bash
    HELICONE_API_KEY=<your-helicone-api-key>
    NVIDIA_API_KEY=<your-nvidia-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>

<CodeGroup>
```bash cURL
curl -X POST https://gateway.helicone.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $NVIDIA_API_KEY" \
  -H "Helicone-Auth: Bearer $HELICONE_API_KEY" \
  -H "Helicone-Target-Url: https://your-dynamo-endpoint.com" \
  -d '{
    "model": "your-model-name",
    "messages": [
      {
        "role": "user",
        "content": "Hello, how are you?"
      }
    ],
    "max_tokens": 1024,
    "temperature": 0.7
  }'
```

```javascript JavaScript
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.NVIDIA_API_KEY,
  baseURL: "https://gateway.helicone.ai/v1",
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
    "Helicone-Target-Url": "https://your-dynamo-endpoint.com"
  }
});

const response = await openai.chat.completions.create({
  model: "your-model-name",
  messages: [{ role: "user", content: "Hello, how are you?" }],
  max_tokens: 1024,
  temperature: 0.7
});

console.log(response);
```

```python Python
from openai import OpenAI
import os

client = OpenAI(
  api_key=os.getenv("NVIDIA_API_KEY"),
  base_url="https://gateway.helicone.ai/v1",
  default_headers={
    "Helicone-Auth": f"Bearer {os.getenv('HELICONE_API_KEY')}",
    "Helicone-Target-Url": "https://your-dynamo-endpoint.com"
  }
)

chat_completion = client.chat.completions.create(
  model="your-model-name",
  messages=[{"role": "user", "content": "Hello, how are you?"}],
  max_tokens=1024,
  temperature=0.7
)

print(chat_completion)
```
</CodeGroup>

  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Dynamo") }} />
  </Step>
</Steps>
