---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/gemini/api/curl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.214641Z"
---
# Curl

---
title: "Gemini AI cURL Integration"
sidebarTitle: "cURL"
description: "Use cURL to integrate Gemini AI with Helicone to log your Gemini AI usage."
"twitter:title": "Gemini AI cURL Integration - Helicone OSS LLM Observability"
icon: "code"
iconType: "solid"
---

import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## Proxy Integration

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).
  </Step>
  <Step title="Create Google Generative AI API Key">
    Visit the [Google Generative AI API Key](https://aistudio.google.com/app/apikey) page.
    Follow the instructions to create a new API key. Make sure to save the key as you will need it for the next steps.
  </Step>
  <Step title="Set API keys as environment variables">
    ```bash
    export HELICONE_API_KEY=<your Helicone API key>
    export GOOGLE_GENERATIVE_API_KEY=<your Google Generative AI API key>
    ```
  </Step>
  <Step title="Send a request using cURL">
    Use the following cURL command to send a request to the Google Generative AI API through the Helicone proxy:
    ```bash
    curl --request POST \
      --url "https://gateway.helicone.ai/v1beta/models/$MODEL_NAME:generateContent?key=$GOOGLE_GENERATIVE_API_KEY" \
      --header "Content-Type: application/json" \
      --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      --header "Helicone-Target-URL: https://generativelanguage.googleapis.com" \
      --data '{
        "contents": [{
          "parts":[{
            "text": "Write a story about a magic backpack."
          }]
        }]
      }'
    ```
  </Step>
</Steps>
