---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/llama/curl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.213320Z"
---
# Curl

---
title: "Llama cURL Integration"
sidebarTitle: "cURL Integration"
description: "Use cURL to integrate Llama with Helicone to log your Llama LLM usage."
"twitter:title": "Llama cURL Integration - Helicone OSS LLM Observability"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [Helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Modify the API base and add the `Helicone-Auth` header">

    ```bash
    curl -X POST https://llama.helicone.ai/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $LLAMA_API_KEY" \
      -H "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      -d '{
        "model": "Llama-4-Maverick-17B-128E-Instruct-FP8",
        "messages": [
          {
            "role": "user",
            "content": "Hello, how are you?"
          }
        ],
        "max_completion_tokens": 1024,
        "temperature": 0.7
      }'
    ```

  </Step>
  <Step title="Verify your requests in Helicone">
    With the above setup, any calls to the Llama API will automatically be logged and monitored by Helicone. Review them in your Helicone dashboard.
  </Step>
</Steps>