---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/perplexity.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.226091Z"
---
---
title: "Perplexity AI Integration"
sidebarTitle: "Perplexity AI"
description: "Connect Helicone with Perplexity AI, a platform that provides powerful language models including Sonar and Sonar Pro for various AI applications."
"twitter:title": "Perplexity AI Integration - Helicone OSS LLM Observability"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

You can follow their documentation here: [https://docs.perplexity.ai/](https://docs.perplexity.ai/)

# Gateway Integration

<Steps>
  <Step title="Create a Helicone account">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Create a Perplexity AI account">
    Log into [Perplexity AI](https://www.perplexity.ai) or create an account. Once you have an account, you
    can generate an API key from your dashboard.
  </Step>
  <Step title="Set HELICONE_API_KEY and PERPLEXITY_API_KEY as environment variable">
```javascript
HELICONE_API_KEY=<your API key>
PERPLEXITY_API_KEY=<your API key>
```
  </Step>
  <Step title="Modify the base URL and add Auth headers">

Replace the following Perplexity AI URL with the Helicone Gateway URL:

`https://api.perplexity.ai/chat/completions` -> `https://perplexity.helicone.ai/chat/completions`

and then add the following authentication headers:

```javascript
Authorization: Bearer <your API key>
```

</Step>
</Steps>

Now you can access all the models on Perplexity AI with a simple fetch call:

## Example

```bash
curl --request POST \
  --url https://perplexity.helicone.ai/chat/completions \
  --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
  --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": "Say this is a test"}]
}'
```

For more information on how to use headers, see [Helicone Headers](https://docs.helicone.ai/helicone-headers/header-directory#utilizing-headers) docs.
And for more information on how to use Perplexity AI, see [Perplexity AI Docs](https://docs.perplexity.ai/).
