---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/python/instructor/instructor-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.860935Z"
---
---
title: "Instructor Tracing"
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

## Install

```bash
pip install openinference-instrumentation-instructor instructor
```

Be sure you also install the OpenInference library for the underlying model you're using along with Instructor. For example, if you're using OpenAI calls directly, you would also add: `openinference-instrumentation-openai`

## Setup

<RegisterTracerPython projectName="my-llm-app" />

## Run Instructor

From here you can use instructor as normal.

```python expandable
import instructor
from pydantic import BaseModel
from openai import OpenAI


# Define your desired output structure
class UserInfo(BaseModel):
    name: str
    age: int


# Patch the OpenAI client
client = instructor.from_openai(OpenAI())

# Extract structured data from natural language
user_info = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=UserInfo,
    messages=[{"role": "user", "content": "John Doe is 30 years old."}],
)

print(user_info.name)
#> John Doe
print(user_info.age)
#> 30
```

## Observe

Now that you have tracing setup, all invocations of your underlying model (completions, chat completions, embeddings) and instructor triggers will be streamed to your running Phoenix for observability and evaluation.


