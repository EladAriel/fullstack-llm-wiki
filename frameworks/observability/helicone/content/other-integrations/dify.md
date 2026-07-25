---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/other-integrations/dify.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.198733Z"
---
# Dify

---
title: "Dify"
sidebarTitle: "Dify"
description: "Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. Here is how to get Observability and logs for your dify instance."
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## Introduction

Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production.

## Integration Steps

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).

    <Note>
      Make sure to generate a [write only API key](helicone-headers/helicone-auth).
    </Note>

  </Step>
  <Step title="Configure API Base in Dify to use Helicone">

Choose whichever provider you are using that is [supported by Helicone](/getting-started/integration-method/gateway#approved-domains). Here is an example using OpenAI.

<Frame caption="Set your API base to the Helicone API URL with your API key in the path.">
  <img src="/images/integrations/dify.png" alt="dify example" />
</Frame>

It's that simple!

  </Step>

</Steps>

Check out the [Open Devin GitHub repository](https://github.com/OpenDevin/OpenDevin) for more information and examples.
