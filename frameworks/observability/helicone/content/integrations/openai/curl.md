---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/openai/curl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.205764Z"
---
# Curl

---
title: "OpenAI with cURL"
sidebarTitle: "cURL"
description: "Use cURL to integrate OpenAI with Helicone to log your OpenAI usage."
"twitter:title": "OpenAI cURL Integration - Helicone OSS LLM Observability"
icon: "code"
iconType: "solid"
---

import { strings } from "/snippets/strings.mdx";
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.modifyBasePath}>
    ```bash
    curl --request POST \
        --url https://oai.helicone.ai/v1/chat/completions \
        --header "Authorization: Bearer $OPENAI_API_KEY" \
        --header "Content-Type: application/json" \
        --header "Helicone-Auth: Bearer $HELICONE_API_KEY" \
        --data '{
            "model": "gpt-4o-mini",
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
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("OpenAI") }} />
  </Step>
</Steps>

## {strings.relatedGuides}

<CardGroup cols={2}>
  <Card
    title="Building a chatbot with OpenAI structured outputs"
    icon="lightbulb"
    href="/guides/cookbooks/openai-structured-outputs"
    iconType="light"
    vertical
  >
    {strings.chatbotCookbookDescription}
  </Card>
  <Card
    title="How to Prompt Thinking Models"
    icon="brain"
    href="/guides/cookbooks/prompt-thinking-models"
    iconType="light"
    vertical
  >
    {strings.howToPromptThinkingModelsCookbookDescription}
  </Card>
</CardGroup>
