---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/litellm-openllmetry.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.227670Z"
---
---
title: "LiteLLM Integration with OpenLLmetry"
sidebarTitle: "OpenLLmetry"
description: "Easily log your LiteLLM API calls to Helicone using OpenLLmetry."
"twitter:title": "LiteLLM Integration with OpenLLmetry - Helicone OSS LLM Observability"
---

# Overview

Helicone's OpenLLmetry integration allows you to log your LiteLLM API calls to Helicone without modifying your code.


<Tabs>
  <Tab title="Python">
  <Steps>
  <Step title="Install Helicone Async">
  ```bash
  pip install helicone-async
  ```
  </Step>
  <Step title="Initialize Logger">

```python

from helicone_async import HeliconeAsyncLogger
from openai import OpenAI
from litellm import completion

logger = HeliconeAsyncLogger(
    api_key=HELICONE_API_KEY,
)

logger.init()

client = OpenAI(api_key=OPENAI_API_KEY)

#openai call
response = completion(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "Hi 👋 - i'm openai"}],
  metadata={
    "Helicone-Property-Hello": "World"
  }
)

#cohere call
response = completion(
  model="command-r",
  messages=[{"role": "user", "content": "Hi 👋 - i'm cohere"}],
  metadata={
    "Helicone-Property-Hello": "World"
  }
)
print(response.choices[0])

```

</Step>
</Steps>
</Tab>

</Tabs>

Read more about [OpenLLmetry](/getting-started/integration-method/openllmetry)