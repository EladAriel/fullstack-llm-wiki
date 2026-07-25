---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/nebius.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.230058Z"
---
---
title: "Nebius Token Factory Integration"
sidebarTitle: "Nebius Token Factory"
description: "Connect Helicone with Nebius Token Factory, a platform that provides powerful AI models including text and multimodal models, embeddings and guardrails, and text-to-image models."
"twitter:title": "Nebius Token Factory AI Integration - Helicone OSS LLM Observability"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

You can follow their documentation here: [https://docs.tokenfactory.nebius.com/](https://docs.tokenfactory.nebius.com/)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Create a Nebius Token Factory account">
    Log into [Nebius Token Factory](https://tokenfactory.nebius.com/) or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>
  <Step title="Set HELICONE_API_KEY and NEBIUS_API_KEY as environment variable">
```javascript
HELICONE_API_KEY=<your API key>
NEBIUS_API_KEY=<your API key>
```
  </Step>
  <Step title="Modify the base URL and add Auth headers">

Replace the following Nebius Token Factory URL with the Helicone Gateway URL:

`https://api.tokenfactory.nebius.com` -> `https://nebius.helicone.ai`

and then add the following authentication headers:

```javascript
Authorization: Bearer <your API key>
```

</Step>
</Steps>

Now you can access all the models on Nebius Token Factory with a simple fetch call:

## Example - Text Completion

```bash
curl \
  --header "Authorization: Bearer $NEBIUS_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "deepseek-ai/DeepSeek-R1",
    "messages": [
      {
        "role": "user",
        "content": "Explain quantum computing in simple terms"
      }
    ]
}' \
  --url https://nebius.helicone.ai/v1/chat/completions
```

## Example - Image Generation

```bash
curl \
  --header "Authorization: Bearer $NEBIUS_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "black-forest-labs/flux-schnell",
    "prompt": "A beautiful sunset over a mountain landscape"
}' \
  --url https://nebius.helicone.ai/v1/images/generations
```

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use Nebius Token Factory, see [Nebius Token Factory Docs](https://docs.tokenfactory.nebius.com/).
