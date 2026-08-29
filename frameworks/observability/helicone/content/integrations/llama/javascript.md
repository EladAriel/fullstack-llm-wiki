---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/llama/javascript.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.353970Z"
---
# Javascript

---
title: "Llama JavaScript SDK"
sidebarTitle: "JavaScript"
description: "Use the OpenAI JavaScript SDK to integrate with Llama via Helicone to log your Llama usage."
"twitter:title": "Llama JavaScript SDK Integration - Helicone OSS LLM Observability"
icon: "js"
iconType: "solid"
---

import GenerateKey from "/snippets/generate-key.mdx";
import { strings } from "/snippets/strings.mdx";
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    ```javascript
    HELICONE_API_KEY=<your-helicone-api-key>
    LLAMA_API_KEY=<your-llama-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
<CodeGroup>

```javascript Llama SDK
import LlamaAPIClient from 'llama-api-client';

const client = new LlamaAPIClient({
  apiKey: process.env.LLAMA_API_KEY,
  baseURL: "https://llama.helicone.ai/v1",
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`
  }
});

const response = await client.chat.completions.create({
  model: 'Llama-4-Maverick-17B-128E-Instruct-FP8',
  messages: [
    {
      role: 'user', 
      content: 'Hello, how are you?' 
    }
  ],
  max_completion_tokens: 1024,
  temperature: 0.7,
});

console.log(response);
```

```javascript OpenAI SDK
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.LLAMA_API_KEY,
  baseURL: "https://llama.helicone.ai/v1",
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`
  }
});

const response = await openai.chat.completions.create({
  model: "Llama-4-Maverick-17B-128E-Instruct-FP8",
  messages: [{ role: "user", content: "Hello, how are you?" }],
  max_completion_tokens: 1024,
  temperature: 0.7
});

console.log(response);
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