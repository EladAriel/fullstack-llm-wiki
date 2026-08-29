---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/getting-started/integration-method/litellm.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.322843Z"
---
---
title: "LiteLLM Integration with Callbacks"
sidebarTitle: "LiteLLM"
description: "Connect Helicone with LiteLLM using callbacks to log and monitor API calls across various AI models."
"twitter:title": "LiteLLM Integration with Callbacks - Helicone OSS LLM Observability"
---
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

[LiteLLM](https://github.com/BerriAI/litellm) is a model I/O library to standardize API calls to Azure, Anthropic, OpenAI, etc. Here's how you can log your LLM API calls to Helicone from LiteLLM using callbacks.

<Note>
  **Note:** [Custom
  Properties](https://docs.helicone.ai/features/advanced-usage/custom-properties)
  are available in `metadata` starting with LiteLLM version `1.41.23`.
</Note>

<Warning>
  **System Instructions Limitation:** When using LiteLLM callbacks, system instructions for Gemini and Claude may not appear as `"role": "system"` messages in Helicone logs. This is because LiteLLM processes the request before sending it to Helicone.

  For full system instruction support, consider using [proxy-based integration](/getting-started/integration-method/litellm-proxy) instead.
</Warning>

## 1 line integration

Add `HELICONE_API_KEY` to your environment variables.

```bash
export HELICONE_API_KEY=sk-<your-api-key>
# You can also set it in your code (See below)
```

Tell LiteLLM you want to log your data to Helicone

```python
litellm.success_callback=["helicone"]
```

## Complete code

```python
from litellm import completion
import os

## set env variables
os.environ["HELICONE_API_KEY"] = "your-helicone-key"
os.environ["OPENAI_API_KEY"], os.environ["COHERE_API_KEY"] = "", ""

# set callbacks
litellm.success_callback=["helicone"]

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

print(response)
```

Feel free to [check it out](https://github.com/BerriAI/litellm) and tell us what you think 👋

For proxy-based integration with LiteLLM, see our [LiteLLM Proxy Integration](/getting-started/integration-method/litellm-proxy) guide.
