---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/azure/javascript.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.211034Z"
---
# Javascript

---
title: "Azure OpenAI with JavaScript"
sidebarTitle: "JavaScript"
description: "Use JavaScript to integrate Azure OpenAI with Helicone to log your Azure OpenAI usage."
"twitter:title": "Azure OpenAI JavaScript Integration - Helicone OSS LLM Observability"
icon: "js"
iconType: "solid"
---

import IncludeApiVersion from "/snippets/include-api-version.mdx";
import ModelOverride from "/snippets/model-override.mdx";
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
    HELICONE_API_KEY=<YOUR_HELICONE_API_KEY>
    AZURE_OPENAI_API_KEY=<YOUR_AZURE_OPENAI_API_KEY>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
    <IncludeApiVersion />
    <CodeGroup>
    ```javascript
    const client = new OpenAI({
      baseURL: "https://oai.helicone.ai/openai/deployments/[DEPLOYMENT_NAME]",
      defaultHeaders: {
        "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
        "Helicone-OpenAI-API-Base": "https://[DOMAIN_NAME].azure.com/",
        "api-key": process.env.AZURE_OPENAI_API_KEY
      },
      defaultQuery: {
        "api-version": "[API_VERSION]"
      },
    });
    ```
    </CodeGroup>
    <ModelOverride />
  </Step>

  <Step title={strings.startUsing("Azure OpenAI")}>
    ```javascript
    const response = await client.chat.completions.create({
      model: "[MODEL_NAME]",
      messages: [{ role: "user", content: "What is the meaning of life?" }]
    });

    console.log(response);
    ```
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Azure OpenAI") }} />
  </Step>
</Steps>

<div dangerouslySetInnerHTML={{ __html: strings.azureOpenAIDocs }} />

## {strings.relatedGuides}

<CardGroup cols={2}>
  <Card
    title="Environment Tracking"
    icon="viruses"
    href="/guides/cookbooks/environment-tracking"
    iconType="light"
    vertical
  >
    {strings.environmentTrackingCookbookDescription}
  </Card>
  <Card
    title="Integration with GitHub Actions"
    icon="github"
    href="/guides/cookbooks/github-actions"
    iconType="light"
    vertical
  >
    {strings.githubActionsCookbookDescription}
  </Card>
</CardGroup>
