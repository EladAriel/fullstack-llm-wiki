---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/python/haystack/haystack-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.861176Z"
---
---
title: "Haystack Tracing"
description: Instrument LLM applications built with Haystack
---

import RegisterTracerPython from "../../../../snippets/register-tracer-python.mdx";

<Frame>
<iframe src="https://cdn.iframe.ly/RoYojEs" className="w-full h-full aspect-video"></iframe>
</Frame>

Phoenix provides auto-instrumentation for [Haystack](https://haystack.deepset.ai/)

## Install

```bash
pip install openinference-instrumentation-haystack haystack-ai
```

## Setup

<RegisterTracerPython projectName="my-llm-app" />

## Run Haystack

<Info>
Phoenix's auto-instrumentor collects any traces from **Haystack Pipelines**. If you are using Haystack but not using Pipelines, you won't see traces appearing in Phoenix automatically.

If you don't want to use Haystack pipelines but still want tracing in Phoenix, you can use instead of this auto-instrumentor.

</Info>

From here, you can set up your Haystack app as normal:

```python expandable
from haystack import Pipeline
from haystack.components.generators import OpenAIGenerator
from haystack.components.builders.prompt_builder import PromptBuilder

prompt_template = """
Answer the following question.
Question: {{question}}
Answer:
"""

# Initialize the pipeline
pipeline = Pipeline()

# Initialize the OpenAI generator component
llm = OpenAIGenerator(model="gpt-3.5-turbo")
prompt_builder = PromptBuilder(template=prompt_template)

# Add the generator component to the pipeline
pipeline.add_component("prompt_builder", prompt_builder)
pipeline.add_component("llm", llm)
pipeline.connect("prompt_builder", "llm")

# Define the question
question = "What is the location of the Hanging Gardens of Babylon?"
```

## Observe

Now that you have tracing setup, all invocations of pipelines will be streamed to your running Phoenix for observability and evaluation.

## Resources:

* [Example notebook](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-haystack/examples/qa_rag_pipeline.py)

* [OpenInference package](https://github.com/Arize-ai/openinference/blob/main/python/instrumentation/openinference-instrumentation-haystack)

* [Working examples](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-haystack/examples)


