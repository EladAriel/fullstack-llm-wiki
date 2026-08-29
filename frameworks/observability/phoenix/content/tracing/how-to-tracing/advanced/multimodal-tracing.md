---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/tracing/how-to-tracing/advanced/multimodal-tracing.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.904415Z"
---
---
title: "Capture Multimodal Traces"
description: "Phoenix supports displaying images that are included in LLM traces."
---



<Frame>
      <img src="https://arize.com/wp-content/uploads/2024/08/multimodal_gallery.gif"/>
</Frame>

## To view images in Phoenix

1. [Connect to a Phoenix instance](/docs/phoenix/get-started)

2. Instrument your application

3. Include either a base64 UTF-8 encoded image or an image url in the call made to your LLM

## Example

```bash
pip install -q "arize-phoenix>=4.29.0" openinference-instrumentation-openai openai
```

```python
# Check if PHOENIX_API_KEY is present in the environment variables.
# If it is, we'll connect to that remote instance. If it's not, we'll start a local one.
# See /docs/phoenix/environments for more information.

# Launch Phoenix
import os
if "PHOENIX_API_KEY" in os.environ:
    os.environ["PHOENIX_CLIENT_HEADERS"] = f"api_key={os.environ['PHOENIX_API_KEY']}"
    os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = "https://your-phoenix.example.com"

else:
    import phoenix as px

    px.launch_app().view()

# Connect to Phoenix
from phoenix.otel import register
tracer_provider = register()

# Instrument OpenAI calls in your application
from openinference.instrumentation.openai import OpenAIInstrumentor
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider, skip_dep_check=True)

# Make a call to OpenAI with an image provided
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
```

You should see your image appear in Phoenix:

<Frame>
  <img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/phoenix-docs-images/cd6e069b-image.jpeg" />
</Frame>


