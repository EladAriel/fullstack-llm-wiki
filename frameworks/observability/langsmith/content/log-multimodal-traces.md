---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/log-multimodal-traces.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1df"
source_commit_date: "2026-07-25T00:27:23+00:00"
generated_at: "2026-07-25T19:08:33.382864Z"
---
# Log Multimodal Traces

---
title: Log multimodal traces
sidebarTitle: Log multimodal traces
---

LangSmith supports logging and rendering images as part of traces. This is currently supported for multimodal LLM runs.

In order to log images, use `wrap_openai`/ `wrapOpenAI` in Python or TypeScript respectively and pass an image URL or base64 encoded image as part of the input.

<CodeGroup>

```python Python
from openai import OpenAI
from langsmith.wrappers import wrap_openai
client = wrap_openai(OpenAI())
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What's in this image?"},
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
          },
        ],
      }
    ],
)
print(response.choices[0])
```

```typescript TypeScript
import OpenAI from "openai";
import { wrapOpenAI } from "langsmith/wrappers";
// Wrap the OpenAI client to automatically log traces
const wrappedClient = wrapOpenAI(new OpenAI());
const response = await wrappedClient.chat.completions.create({
  model: "gpt-4-turbo",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What's in this image?" },
        {
          type: "image_url",
          image_url: {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    },
  ],
});
console.log(response.choices[0]);
```

</CodeGroup>

The image will be rendered as part of the trace in the[ LangSmith UI](https://smith.langchain.com).
