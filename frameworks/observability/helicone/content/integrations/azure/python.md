---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/azure/python.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.348739Z"
---
# Python

---
title: "Azure OpenAI with Python"
sidebarTitle: "Python"
description: "Use Python to integrate Azure OpenAI with Helicone to log your Azure OpenAI usage."
"twitter:title": "Azure OpenAI Python Integration - Helicone OSS LLM Observability"
icon: "python"
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
    ```python
    HELICONE_API_KEY=<YOUR_HELICONE_API_KEY>
    AZURE_OPENAI_API_KEY=<YOUR_AZURE_OPENAI_API_KEY>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
    <IncludeApiVersion />
    <CodeGroup>
    ```python AzureOpenAI
    from openai import AzureOpenAI
    from dotenv import load_dotenv
    import os

    load_dotenv()

    helicone_api_key = os.getenv("HELICONE_API_KEY")
    azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")

    client = AzureOpenAI(
        api_version="[API_VERSION]" # "2024-12-01-preview",
        azure_endpoint="https://[AZURE_DOMAIN].openai.azure.com/",
        api_key=azure_openai_api_key,
        default_headers={
            "Helicone-Auth": f"Bearer {helicone_api_key}",
            "Helicone-OpenAI-Api-Base": "https://[AZURE_DOMAIN].openai.azure.com",
            "Helicone-Model-Override": "[MODEL_NAME]",
            "api-key": azure_openai_api_key
        }
    )
    ```

    ```python OpenAI v1+
    from openai import OpenAI
    from dotenv import load_dotenv
    import os

    load_dotenv()

    helicone_api_key = os.getenv("HELICONE_API_KEY")
    azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")

    azure_openai = OpenAI(
      api_key=azure_openai_api_key,
      base_url="https://oai.helicone.ai/openai/deployments/[DEPLOYMENT_NAME]",
      default_headers={
        "Helicone-OpenAI-Api-Base": "https://[AZURE_DOMAIN].openai.azure.com",
        "Helicone-Auth": f"Bearer {helicone_api_key}",
        "Helicone-Model-Override": "[MODEL_NAME]"
      },
      default_query={
        "api-version": "[API_VERSION]" # "2023-03-15-preview"
      }
    )
    ```
    </CodeGroup>
    <ModelOverride />
  </Step>

  <Step title={strings.startUsing("Azure OpenAI")}>
    ```python
    response = azure_openai.chat.completions.create(
      model="[MODEL_NAME]",
      messages=[{"role": "User", "content": "What is the meaning of life?"}]
    )

    print(response)
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
    icon="sitemap"
    href="/guides/cookbooks/environment-tracking"
    iconType="light"
    vertical
  >
    {strings.environmentTrackingCookbookDescription}
  </Card>
  <Card
    title="Getting User Requests"
    icon="user"
    href="/guides/cookbooks/getting-user-requests"
    iconType="light"
    vertical
  >
    {strings.gettingUserRequestsCookbookDescription}
  </Card>
</CardGroup>
