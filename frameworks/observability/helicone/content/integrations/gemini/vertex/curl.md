---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/gemini/vertex/curl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.214008Z"
---
# Curl

---
title: "Vertex AI cURL Integration"
sidebarTitle: "cURL"
description: "Use cURL to integrate Vertex AI with Helicone to log your Vertex AI usage."
"twitter:title": "Vertex AI cURL Integration - Helicone OSS LLM Observability"
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
  <Step title="Set API keys as environment variables">
    ```bash
    export HELICONE_API_KEY=<your API key>
    export GCLOUD_API_KEY=<your Google Cloud API key>
    ```
  </Step>
  <Step title="Send a request using CURL">
    Use the following CURL command to send a request to the Vertex AI API through the Helicone proxy:
    ```bash
    curl --request POST \
      --url "https://gateway.helicone.ai/v1/projects/$PROJECT_ID/locations/$LOCATION/publishers/google/models/$MODEL_NAME:streamGenerateContent" \
      --header "Authorization: Bearer $GCLOUD_API_KEY" \
      --header "Content-Type: application/json" \
      --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      --header "Helicone-Target-URL: https://$LOCATION-aiplatform.googleapis.com" \
      --header "User-Agent: curl/7.64.1" \
      --data '{
      "contents": {
        "role": "user",
        "parts": {
          "text": "Which theaters in Mountain View show Barbie movie?"
        }
      },
      "generation_config": {
        "maxOutputTokens": 1
      }
    }'
    ```
  </Step>
</Steps>
