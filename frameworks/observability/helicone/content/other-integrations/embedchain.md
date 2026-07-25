---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/other-integrations/embedchain.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.199299Z"
---
---
title: "Mem0 Embedchain Integration"
sidebarTitle: "Mem0 Embedchain"
description: "Integrate Helicone with Embedchain, an Open Source Framework for personalizing LLM responses. Monitor interactions across different LLMs in AI applications."
"twitter:title": "Mem0 Embedchain Integration - Helicone OSS LLM Observability"
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

## Introduction

Mem0 Embedchain is an Open Source Framework for personalizing LLM responses. It makes it easy to create and deploy personalized AI apps.

Integrating Helicone with Mem0 Embedchain allows you to monitor interactions across different LLMs in AI applications.

## Integration Steps

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [Helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).

    <Note>
      Make sure to generate a [write only API key](helicone-headers/helicone-auth).
    </Note>

  </Step>
  <Step title="Set base_url in the your code">
You can configure your base_url and OpenAI API key in your codebase
  <CodeGroup>

```python main.py
import os
from embedchain import App

# Modify the base path and add a Helicone URL
os.environ["OPENAI_API_BASE"] = "https://oai.helicone.ai/{YOUR_HELICONE_API_KEY}/v1"
# Add your OpenAI API Key
os.environ["OPENAI_API_KEY"] = "{YOUR_OPENAI_API_KEY}"

app = App()

# Add data to your app
app.add("https://en.wikipedia.org/wiki/Elon_Musk")

# Query your app
print(app.query("How many companies did Elon found? Which companies?"))
```

</CodeGroup>

  </Step>
  <Step title="Now you can see all passing requests through Embedchain in Helicone">
    <img src="/images/helicone-embedchain.png" alt="Embedchain requests" />
  </Step>
</Steps>

Check out the [Embedchain](https://github.com/embedchain/embedchain) GitHub repository for more information and examples.
