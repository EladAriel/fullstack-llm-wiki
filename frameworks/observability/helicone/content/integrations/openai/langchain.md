---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/openai/langchain.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.204521Z"
---
# Langchain

---
title: "OpenAI with LangChain"
sidebarTitle: "LangChain"
description: "Use LangChain to integrate OpenAI with Helicone to log your OpenAI usage."
"twitter:title": "OpenAI Langchain Integration - Helicone OSS LLM Observability"
icon: "bird"
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
    OPENAI_API_KEY=<your-openai-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
    <CodeGroup>
      ```javascript javascript
      import { OpenAI } from "@langchain/openai";

      const llm = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
        baseURL: "https://oai.helicone.ai/v1",
        defaultHeaders: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`
        }
      });
      ```

      ```python python
      from langchain_openai import OpenAI
      from dotenv import load_dotenv
      import os

      load_dotenv()

      llm = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://oai.helicone.ai/v1",
        default_headers={
          "Helicone-Auth": f"Bearer {os.getenv('HELICONE_API_KEY')}"
        }
      )
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.useTheSDK("LangChain")}>
    <CodeGroup>
      ```javascript javascript
      const response = await llm.invoke("What is the meaning of life?");
      console.log(response);
      ```

      ```python python
      response = llm.invoke("What is the meaning of life?")
      print(response)
      ```
    </CodeGroup>
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
    title="Trace, replay, and debug LLM sessions"
    icon="arrows-rotate"
    href="/guides/cookbooks/replay-llm-sessions"
    iconType="light"
    vertical
  >
    {strings.replayLlmSessionsCookbookDescription}
  </Card>
</CardGroup>
