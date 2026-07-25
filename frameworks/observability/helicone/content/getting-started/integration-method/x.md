---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/x.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.225718Z"
---
---
title: "X AI Integration"
sidebarTitle: "X AI"
description: "Connect Helicone with X AI, a platform that provides powerful language models including MoE and Code models for various AI applications."
"twitter:title": "X AI Integration - Helicone OSS LLM Observability"
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

You can follow their documentation here: [https://api-docs.x.ai/](https://api-docs.x.ai/)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Create an X AI account">
    Log into https://console.x.ai/ or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>
  <Step title="Set HELICONE_API_KEY and XAI_API_KEY as environment variables">
```javascript
HELICONE_API_KEY=<your API key>
XAI_API_KEY=<your API key>
```
  </Step>
  <Step title="Modify the base URL and add Auth headers">

Replace the following X AI URL with the Helicone Gateway URL:

`https://api.x.ai/v1/chat/completions` -> `https://x.helicone.ai/v1/chat/completions`

and then add the following authentication headers:

```javascript
Authorization: Bearer $XAI_API_KEY
Helicone-Auth: Bearer $HELICONE_API_KEY
```

</Step>
</Steps>

Now you can access all the models on X AI with a simple fetch call:

## Example

```bash
curl --request POST \
      --url https://x.helicone.ai/v1/chat/completions \
      --header "Content-Type: application/json" \
      --header "Authorization: Bearer $XAI_API_KEY" \
      --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      --data '{
          "model": "grok-4-latest",
          "messages": [
              {
                  "role": "system",
                  "content": "You are a robot called Marvin with a brain the size of the planet."
              },
              {
                  "role": "user",
                  "content": "Say this is a test"
              }
          ],
          "temperature": 1
        }'
```

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use X AI, see [X AI Docs](https://docs.x.ai/docs/overview).
