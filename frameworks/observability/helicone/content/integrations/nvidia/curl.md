---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/nvidia/curl.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.351350Z"
---
# Curl

---
title: "Nvidia NIM cURL Integration"
sidebarTitle: "cURL"
description: "Use cURL to integrate Nvidia NIM with Helicone to log your Nvidia LLM usage."
"twitter:title": "Nvidia NIM cURL Integration - Helicone OSS LLM Observability"
icon: "code"
iconType: "solid"
---

import { strings } from "/snippets/strings.mdx";
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

This integration is used to log usage with the [Nvidia NIM](https://build.nvidia.com/) API. For other Nvidia inference providers that are OpenAI-compatible, such as Dynamo, see [here](/integrations/nvidia/dynamo).

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
      <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>
<Step title={strings.modifyBasePath}>

    ```bash
    curl -X POST https://nvidia.helicone.ai/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $NVIDIA_API_KEY" \
      -H "Helicone-Auth: Bearer $HELICONE_API_KEY" \
      -d '{
        "model": "nvidia/llama-3.1-nemotron-70b-instruct",
        "messages": [
          {
            "role": "user",
            "content": "Hello, how are you?"
          }
        ],
        "max_tokens": 1024,
        "temperature": 0.7
      }'
    ```

  </Step>
  
  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Nvidia NIM") }} />
  </Step>
</Steps> 