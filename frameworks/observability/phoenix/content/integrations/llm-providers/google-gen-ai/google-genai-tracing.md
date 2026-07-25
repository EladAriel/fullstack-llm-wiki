---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/google-gen-ai/google-genai-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.847144Z"
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


