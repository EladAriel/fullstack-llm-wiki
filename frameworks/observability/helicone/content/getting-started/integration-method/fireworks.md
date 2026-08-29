---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/fireworks.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.322124Z"
---
---
title: "Fireworks AI Integration"
sidebarTitle: "Fireworks AI"
description: "Connect Helicone with Fireworks AI, a platform that provides a fast, affordable, and customizable solution for generative artificial intelligence that helps product developers run, fine-tune, and share large language models."
"twitter:title": "Fireworks AI Integration - Helicone OSS LLM Observability"
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

You can follow their documentation here: [https://docs.fireworks.ai/getting-started/quickstart](https://docs.fireworks.ai/getting-started/quickstart)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Create an FireworksAI account">
    Log into www.fireworks.ai or create an account. Once you have an account, you
    can generate an [API key](https://fireworks.ai/api-keys).
  </Step>
  <Step title="Set HELICONE_API_KEY and FIREWORKS_API_KEY as environment variable">
```javascript
HELICONE_API_KEY=<your API key>
FIREWORKS_API_KEY=<your API key>
```
  </Step>
  <Step title="Modify the base URL and add Auth headers">

Replace the following FireworksAI URL with the Helicone Gateway URL:

`https://api.fireworks.ai/inference/v1/chat/completions` -> `https://fireworks.helicone.ai/inference/v1/chat/completions`

and then add the following authentication headers.

```
Helicone-Auth: `Bearer ${HELICONE_API_KEY}`
Authorization: `Bearer ${FIREWORKS_API_KEY}`
```

</Step>
</Steps>

Now you can access all the models on FireworksAI with a simple fetch call:

## Example

```bash
curl --request POST \
  --url https://fireworks.helicone.ai/inference/v1/completions \
  --header "Authorization: Bearer $FIREWORKS_API_KEY" \
  --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "accounts/fireworks/models/llama-v3-8b-instruct",
    "prompt": "Say this is a test"
}'
```

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use FireworksAI, see [FireworksAI Docs](https://docs.fireworks.ai/).
