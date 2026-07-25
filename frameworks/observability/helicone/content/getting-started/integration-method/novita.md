---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/novita.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.227865Z"
---
---
title: "Novita AI Integration"
sidebarTitle: "Novita AI"
description: "Connect Helicone with Novita AI, a platform that provides powerful LLM models including DeepSeek, Llama, Mistral, and more."
"twitter:title": "Novita AI Integration - Helicone OSS LLM Observability"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

You can follow their documentation here: [https://novita.ai/docs](https://novita.ai/docs)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Create a Novita AI account">
    Log into [Novita AI](https://novita.ai) or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>
  <Step title="Set HELICONE_API_KEY and NOVITA_API_KEY as environment variable">
```javascript
HELICONE_API_KEY=<your API key>
NOVITA_API_KEY=<your API key>
```
  </Step>
  <Step title="Modify the base URL and add Auth headers">

Replace the following Novita AI URL with the Helicone Gateway URL:

`https://api.novita.ai` -> `https://novita.helicone.ai`

and then add the following authentication headers:

```javascript
Authorization: Bearer <your API key>
```

</Step>
</Steps>

Now you can access all the models on Novita AI with a simple fetch call:

## Example

```bash
curl \
  --header "Authorization: Bearer $NOVITA_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "deepseek/deepseek-r1",
    "messages": [
      {
        "role": "user",
        "content": "What is the capital of France?"
      }
    ]
}' \
  --url https://novita.helicone.ai/v3/chat/completions
```

## Referral Program

Novita AI offers a referral program that provides $20 in credits for both you and your referrals when using the DeepSeek R1 & V3 APIs. Share your referral link with others to earn credits and help them get started with Novita. Learn more about the program at [Novita's blog](https://blogs.novita.ai/earn-up-to-500-in-deepseek-api-credits-supercharge-your-ai-projects-today/).

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use Novita AI, see [Novita AI Docs](https://novita.ai/docs).
