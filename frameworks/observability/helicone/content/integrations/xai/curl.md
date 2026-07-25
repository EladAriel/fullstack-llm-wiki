---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/xai/curl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.209081Z"
---
# Curl

---
title: "xAI cURL Integration"
sidebarTitle: "cURL"
description: "Use cURL to integrate xAI with Helicone to log your xAI LLM usage."
"twitter:title": "xAI cURL Integration - Helicone OSS LLM Observability"
icon: "code"
iconType: "solid"
---

import { strings } from "/snippets/strings.mdx";
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

This integration is used to log usage with the [xAI](https://x.ai) API.

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
      <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>
<Step title={strings.modifyBasePath}>

    ```bash
    curl -X POST https://x.helicone.ai/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $XAI_API_KEY" \
      -H "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      -d '{
        "model": "grok-4-latest",
        "messages": [
          {
            "role": "user",
            "content": "Hello, how are you?"
          }
        ],
        "max_tokens": 50,
        "temperature": 0.7
      }'
    ```

  </Step>
  
  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("xAI") }} />
  </Step>
</Steps> 