---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/deepseek.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.319328Z"
---
---
title: "DeepSeek AI Integration"
sidebarTitle: "DeepSeek AI"
description: "Connect Helicone with DeepSeek AI, a platform that provides powerful language models including MoE and Code models for various AI applications."
"twitter:title": "DeepSeek AI Integration - Helicone OSS LLM Observability"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

You can follow their documentation here: [https://api-docs.deepseek.com/](https://api-docs.deepseek.com/)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Create a DeepSeek AI account">
    Log into platform.deepseek.ai or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>
  <Step title="Set HELICONE_API_KEY and DEEPSEEK_API_KEY as environment variable">
```javascript
HELICONE_API_KEY=<your API key>
DEEPSEEK_API_KEY=<your API key>
```
  </Step>
  <Step title="Modify the base URL and add Auth headers">

Replace the following DeepSeek AI URL with the Helicone Gateway URL:

`https://api.deepseek.ai/v1/chat/completions` -> `https://deepseek.helicone.ai/v1/chat/completions`

and then add the following authentication headers:

```javascript
Authorization: Bearer <your API key>
```

</Step>
</Steps>

Now you can access all the models on DeepSeek AI with a simple fetch call:

## Example

```bash
curl --request POST \
      --url https://deepseek.helicone.ai/chat/completions \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $DEEPSEEK_API_KEY" \
      --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      --data '{
          "model": "deepseek-chat",
          "messages": [
              {
                  "role": "system",
                  "content": "Say Hello!"
              }
          ],
          "temperature": 1,
          "max_tokens": 30
        }'
```

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use DeepSeek AI, see [DeepSeek AI Docs](https://platform.deepseek.ai/docs).
