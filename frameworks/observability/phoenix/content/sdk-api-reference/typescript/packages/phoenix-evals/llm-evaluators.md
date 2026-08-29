---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/sdk-api-reference/typescript/packages/phoenix-evals/llm-evaluators.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.815592Z"
---
# Llm Evaluators

---
title: "LLM Evaluators"
description: "Use LLM-backed evaluators in @arizeai/phoenix-evals"
---

The `llm` entrypoint provides reusable evaluator factories that call an AI SDK model and return structured evaluation results.

<section className="hidden" data-agent-context="relevant-source-files" aria-label="Relevant source files">
  <h2>Relevant Source Files</h2>
  <ul>
    <li><code>src/llm/index.ts</code></li>
  </ul>
</section>

## Example

```ts
import { openai } from "@ai-sdk/openai";
import { createFaithfulnessEvaluator } from "@arizeai/phoenix-evals";

const faithfulness = createFaithfulnessEvaluator({
  model: openai("gpt-4o-mini"),
});

const result = await faithfulness.evaluate({
  input: "What is the capital of France?",
  context: "France is a country in Europe. Paris is its capital city.",
  output: "The capital of France is Paris.",
});
```

## Built-In Evaluator Factories

- `createConcisenessEvaluator`
- `createCorrectnessEvaluator`
- `createRetrievalRelevanceEvaluator`
- `createFaithfulnessEvaluator`
- `createRefusalEvaluator`
- `createClassificationEvaluator`
- `createToolSelectionEvaluator`
- `createToolInvocationEvaluator`
- `createToolResponseHandlingEvaluator`

```ts
import { openai } from "@ai-sdk/openai";
import {
  createCorrectnessEvaluator,
  createRefusalEvaluator,
} from "@arizeai/phoenix-evals";

const model = openai("gpt-4o-mini");

const correctness = createCorrectnessEvaluator({ model });
const refusal = createRefusalEvaluator({ model });
```

<section className="hidden" data-agent-context="source-map" aria-label="Source map">
  <h2>Source Map</h2>
  <ul>
    <li><code>src/llm/createClassificationEvaluator.ts</code></li>
    <li><code>src/llm/ClassificationEvaluator.ts</code></li>
    <li><code>src/llm/LLMEvaluator.ts</code></li>
    <li><code>src/llm/createFaithfulnessEvaluator.ts</code></li>
    <li><code>src/types/evals.ts</code></li>
  </ul>
</section>
