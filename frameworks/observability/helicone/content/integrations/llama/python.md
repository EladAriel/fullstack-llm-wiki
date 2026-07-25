---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/llama/python.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.213139Z"
---
---
title: "Llama Python SDK"
sidebarTitle: "Python"
description: "Use the OpenAI Python SDK to integrate with Llama via Helicone to log your Llama usage."
"twitter:title": "Llama Python SDK Integration - Helicone OSS LLM Observability"
icon: "python"
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
    ```bash
    HELICONE_API_KEY=<your-helicone-api-key>
    LLAMA_API_KEY=<your-llama-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
<CodeGroup>

```python Llama SDK
import os
from llama_api_client import LlamaAPIClient

# Load environment variables
helicone_api_key = os.getenv("HELICONE_API_KEY")
llama_api_key = os.getenv("LLAMA_API_KEY")

client = LlamaAPIClient(
    api_key=llama_api_key,
    base_url="https://llama.helicone.ai/v1",
    default_headers={
        "Helicone-Auth": f"Bearer {helicone_api_key}"
    }
)

completion = client.chat.completions.create(
    model="Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[
        {
            "role": "user",
            "content": "What is the moon made of?",
        }
    ],
)

print(completion.completion_message.content.text)
```

```python OpenAI SDK
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

helicone_api_key = os.getenv("HELICONE_API_KEY")
llama_api_key = os.getenv("LLAMA_API_KEY")

client = OpenAI(
  api_key=llama_api_key,
  base_url="https://llama.helicone.ai/v1",
  default_headers={
    "Helicone-Auth": f"Bearer {helicone_api_key}"
  }
)

chat_completion = client.chat.completions.create(
  model="Llama-4-Maverick-17B-128E-Instruct-FP8",
  messages=[{"role": "user", "content": "Hello, how are you?"}],
  max_completion_tokens=1024,
  temperature=0.7
)

print(chat_completion)
```

</CodeGroup>
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Llama") }} />
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