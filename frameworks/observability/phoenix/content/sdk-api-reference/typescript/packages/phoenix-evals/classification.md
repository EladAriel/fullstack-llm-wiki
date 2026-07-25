---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/sdk-api-reference/typescript/packages/phoenix-evals/classification.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.947655Z"
---
# Classification

---
title: "Classification"
description: "Classification helpers in @arizeai/phoenix-evals"
---

Use the classification helpers when you want an LLM to choose from a fixed set of labels and return a structured explanation.

## Create A Classifier Function

```ts
import { openai } from "@ai-sdk/openai";
import { createClassifierFn } from "@arizeai/phoenix-evals";

const classify = createClassifierFn({
  model: openai("gpt-4o-mini"),
  choices: { relevant: 1, irrelevant: 0 },
  promptTemplate:
    "Question: {{input}}\nContext: {{context}}\nAnswer: {{output}}\nLabel as relevant or irrelevant.",
});

const result = await classify({
  input: "What is Phoenix?",
  context: "Phoenix is an AI observability platform.",
  output: "Phoenix helps teams inspect traces and experiments.",
});
```

## Lower-Level API

Use `generateClassification` directly when you already have a rendered prompt and only need structured label generation.

<section className="hidden" data-agent-context="source-map" aria-label="Source map">
  <h2>Source Map</h2>
  <ul>
    <li><code>src/llm/createClassifierFn.ts</code></li>
    <li><code>src/llm/createClassificationEvaluator.ts</code></li>
    <li><code>src/llm/generateClassification.ts</code></li>
    <li><code>src/types/evals.ts</code></li>
  </ul>
</section>
