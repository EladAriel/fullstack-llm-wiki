---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/anthropic/curl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.207764Z"
---
# Curl

---
title: "Anthropic cURL Integration"
sidebarTitle: "cURL"
description: "Use cURL to integrate Anthropic with Helicone to log your Anthropic LLM usage."
"twitter:title": "Anthropic cURL Integration - Helicone OSS LLM Observability"
icon: "code"
iconType: "solid"
---

import { strings } from "/snippets/strings.mdx";
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## {strings.howToIntegrate}

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Modify the API base and add the `Helicone-Auth` header">

    <Note>
    Please ensure to replace API keys with your own.
    </Note>

    ```bash
    curl --request POST \
      --url https://anthropic.helicone.ai/v1/messages \
      --header "Content-Type: application/json" \
      --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      --header "User-Agent: insomnia/8.6.1" \
      --header "anthropic-version: 2023-06-01" \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --data '{
            "model": "claude-3-opus-20240229",
            "max_tokens": 50,
            "system": "Respond only in Spanish.",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Test"
                        }
                    ]
                }
            ],
            "stream": true
    }'
    ```

  </Step>
</Steps>
