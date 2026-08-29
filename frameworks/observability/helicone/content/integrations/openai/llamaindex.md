---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/openai/llamaindex.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.352852Z"
---
# Llamaindex

---
title: "OpenAI with LlamaIndex"
sidebarTitle: "LlamaIndex"
description: "Use LlamaIndex to integrate with Helicone to log your LlamaIndex usage."
"twitter:title": "LlamaIndex Integration - Helicone OSS LLM Observability"
icon: "horse"
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

   <Step title={strings.setApiKey}>
    ```python
    HELICONE_API_KEY=<your-helicone-api-key>
    OPENAI_API_KEY=<your-openai-api-key>
    ```
  </Step>

  <Step title={strings.setUpToolBaseUrl("OpenAI")}>
    <CodeGroup>
      ```python python
      import os
      from dotenv import load_dotenv
      from llama_index.core import Settings
      from llama_index.llms.openai import OpenAI

      load_dotenv()

      helicone_api_key = os.getenv("HELICONE_API_KEY")
      openai_api_key = os.getenv("OPENAI_API_KEY")

      Settings.llm = OpenAI(
        base_url="https://oai.helicone.ai/v1",
        api_key=openai_api_key,
        default_headers={
          "Helicone-Auth": f"Bearer {helicone_api_key}"
        }
      )
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.useTheSDK("LlamaIndex")}>
    ```python python
      response = OpenAI().complete("What is the meaning of life?")
      print(response)
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
    title="LLM Tracking with multiple environments"
    icon="viruses"
    href="/guides/cookbooks/environment-tracking"
    iconType="light"
    vertical
  >
    {strings.environmentTrackingCookbookDescription}
    </Card>
</CardGroup>
