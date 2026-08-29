---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/google-gen-ai/google-genai-tracing.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.947093Z"
---
# Google Genai Tracing

---
title: "Google Gen AI Tracing"
description: Instrument LLM calls made using the Google Gen AI Python SDK
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

### Install

```bash
pip install openinference-instrumentation-google-genai google-genai
```

### Setup

Set the `GEMINI_API_KEY` environment variable. To use the Gen AI SDK with Vertex AI instead of the Developer API, refer to Google's [guide](https://cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview) on setting the required environment variables.

```javascript
export GEMINI_API_KEY=[your_key_here]
```

<RegisterTracerPython projectName="my-llm-app" />

### Observe

Now that you have tracing setup, all Gen AI SDK requests will be streamed to Phoenix for observability and evaluation.

```python
import os
from google import genai

def send_message_multi_turn() -> tuple[str, str]:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    chat = client.chats.create(model="gemini-2.0-flash-001")
    response1 = chat.send_message("What is the capital of France?")
    response2 = chat.send_message("Why is the sky blue?")

    return response1.text or "", response2.text or ""
```

<Info>
This instrumentation will support tool calling soon. Refer to [this page](https://pypi.org/project/openinference-instrumentation-google-genai/#description) for the status.

</Info>


