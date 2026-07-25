---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/openai/javascript.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.204981Z"
---
# Javascript

---
title: "OpenAI JavaScript SDK"
sidebarTitle: "JavaScript"
description: "Use OpenAI's JavaScript SDK to integrate with Helicone to log your OpenAI usage."
"twitter:title": "OpenAI JavaScript SDK Integration - Helicone OSS LLM Observability"
icon: "js"
iconType: "solid"
---

import { strings } from "/snippets/strings.mdx";
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## {strings.howToIntegrate}

<video width="100%" controls autoplay loop>
  <source
    src="https://marketing-assets-helicone.s3.us-west-2.amazonaws.com/Helicone+Tutorial+Video.mp4"
    type="video/mp4"
  />
  Your browser does not support the video tag.
</video>

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    ```javascript
    HELICONE_API_KEY=<your-helicone-api-key>
    OPENAI_API_KEY=<your-openai-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
    <CodeGroup>
      ```javascript OpenAI v4+
      import OpenAI from "openai";

      const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
        baseURL: "https://oai.helicone.ai/v1",
        defaultHeaders: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`
        }
      });
      ```

      ```javascript OpenAI v1
      import { Configuration, OpenAIApi } from "openai";

      const configuration = new Configuration({
        apiKey: process.env.OPENAI_API_KEY,
        basePath: "https://oai.helicone.ai/v1",
        baseOptions: {
          headers: {
            "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`
          }
        }
      });

      const openai = new OpenAIApi(configuration);
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.useTheSDK("OpenAI")}>
    ```javascript
    const response = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: "What is the meaning of life?" }]
    });

    console.log(response);
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
    title="How to Prompt Thinking Models Effectively"
    icon="arrows-rotate"
    href="/guides/cookbooks/prompt-thinking-models"
    iconType="light"
    vertical
  >
    {strings.howToPromptThinkingModelsCookbookDescription}
  </Card>
</CardGroup>
