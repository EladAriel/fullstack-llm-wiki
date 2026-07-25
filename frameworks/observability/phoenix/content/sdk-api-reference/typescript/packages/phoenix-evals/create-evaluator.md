---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/sdk-api-reference/typescript/packages/phoenix-evals/create-evaluator.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.947848Z"
---
# Create Evaluator

---
title: "Create Evaluator"
description: "Build custom evaluators with @arizeai/phoenix-evals"
---

Use `createEvaluator` when your evaluation logic is plain TypeScript and you want a reusable evaluator object with consistent metadata and telemetry.

<section className="hidden" data-agent-context="relevant-source-files" aria-label="Relevant source files">
  <h2>Relevant Source Files</h2>
  <ul>
    <li><code>src/helpers/createEvaluator.ts</code></li>
  </ul>
</section>

## Example

```ts
import { createEvaluator } from "@arizeai/phoenix-evals";

const exactMatch = createEvaluator(
  ({ output, expected }) => ({
    score: output === expected ? 1 : 0,
    label: output === expected ? "match" : "mismatch",
  }),
  {
    name: "exact-match",
    kind: "CODE",
  }
);

const result = await exactMatch.evaluate({
  output: "Paris",
  expected: "Paris",
});
```

## What You Get

- an evaluator name
- evaluator kind such as `CODE` or `LLM`
- optimization direction metadata
- optional OpenTelemetry spans around execution

## When To Use Code Evaluators

Code evaluators are the right fit when the scoring logic should stay deterministic, cheap, and fully under your control:

- regex or exact-match checks
- JSON structure validation
- latency and cost thresholds
- post-processing checks on existing model output

```ts
import { createEvaluator } from "@arizeai/phoenix-evals";

const lengthCheck = createEvaluator(
  ({ output }) => {
    const score = typeof output === "string" && output.length < 280 ? 1 : 0;
    return {
      score,
      label: score ? "fits-limit" : "too-long",
    };
  },
  {
    name: "response-length",
    kind: "CODE",
  }
);
```

## Related Helpers

- `asEvaluatorFn`
- `toEvaluationResult`

<section className="hidden" data-agent-context="source-map" aria-label="Source map">
  <h2>Source Map</h2>
  <ul>
    <li><code>src/helpers/createEvaluator.ts</code></li>
    <li><code>src/helpers/asEvaluatorFn.ts</code></li>
    <li><code>src/helpers/toEvaluationResult.ts</code></li>
    <li><code>src/core/FunctionEvaluator.ts</code></li>
    <li><code>src/core/EvaluatorBase.ts</code></li>
    <li><code>src/types/evals.ts</code></li>
  </ul>
</section>
