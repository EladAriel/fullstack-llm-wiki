---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/nvidia/python.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.212285Z"
---
# Python

---
title: "Nvidia NIM Python SDK"
sidebarTitle: "Python"
description: "Use the OpenAI Python SDK to integrate with Nvidia NIM via Helicone to log your Nvidia usage."
"twitter:title": "Nvidia NIM Python SDK Integration - Helicone OSS LLM Observability"
icon: "python"
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

  <Step title={strings.setApiKey}>
    ```bash
    HELICONE_API_KEY=<your-helicone-api-key>
    NVIDIA_API_KEY=<your-nvidia-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>

    ```python OpenAI SDK
    from openai import OpenAI
    from dotenv import load_dotenv
    import os

    load_dotenv()

    helicone_api_key = os.getenv("HELICONE_API_KEY")
    nvidia_api_key = os.getenv("NVIDIA_API_KEY")

    client = OpenAI(
      api_key=nvidia_api_key,
      base_url="https://nvidia.helicone.ai/v1",
      default_headers={
        "Helicone-Auth": f"Bearer {helicone_api_key}"
      }
    )

    chat_completion = client.chat.completions.create(
      model="nvidia/llama-3.1-nemotron-70b-instruct",
      messages=[{"role": "user", "content": "Hello, how are you?"}],
      max_tokens=1024,
      temperature=0.7
    )

    print(chat_completion)
    ```

  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Nvidia") }} />
  </Step>
</Steps>

## {strings.relatedGuides}

<CardGroup cols={2}>
  <Card
    title="Building a chatbot with structured outputs"
    icon="lightbulb"
    href="/guides/cookbooks/openai-structured-outputs"
    iconType="light"
    vertical
  >
    {strings.chatbotCookbookDescription}
  </Card>
  <Card
    title="How to Prompt Thinking Models Effectively"
    icon="arrows-rotate"
    href="/guides/cookbooks/prompt-thinking-models"
    iconType="light"
    vertical
  >
    {strings.howToPromptThinkingModelsCookbookDescription}
  </Card>
</CardGroup> 