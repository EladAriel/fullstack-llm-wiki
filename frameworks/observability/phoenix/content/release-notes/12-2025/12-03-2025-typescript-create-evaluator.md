---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/12-2025/12-03-2025-typescript-create-evaluator.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.908286Z"
---
# 12 03 2025 Typescript Create Evaluator

---
title: "12.03.2025: TypeScript createEvaluator"
description: Available in @arizeai/phoenix-evals 2.0+
---

## TypeScript createEvaluator

The `createEvaluator` utility in `@arizeai/phoenix-evals` provides a type-safe way to build custom code evaluators for experiments in TypeScript. Define evaluators with full type inference for inputs, outputs, and expected values.

### Basic Usage

Create simple evaluators that validate experiment outputs:

```typescript
import { createEvaluator } from "@arizeai/phoenix-evals";

const inBounds = createEvaluator<{ output: number }>(
  ({ output }) => {
    return 1 <= output && output <= 100 ? 1 : 0;
  },
  { name: "in_bounds" }
);
```

### Multiple Parameters

Access `input`, `output`, `expected`, and `metadata` in your evaluator:

```typescript
import { createEvaluator } from "@arizeai/phoenix-evals";
import { distance } from "fastest-levenshtein";

const editDistance = createEvaluator<{ output: string; expected: string }>(
  ({ output, expected }) => distance(output, expected),
  { name: "edit_distance" }
);
```

### Evaluator Options

Customize display properties for better integration with the Experiments UI:

```typescript
const containsLink = createEvaluator<{ output: string }>(
  ({ output }) => /https?:\/\/[^\s]+/.test(output) ? 1 : 0,
  { name: "contains_link", kind: "CODE" }
);
```

### Running in Experiments

Pass evaluators directly to `runExperiment`:

```typescript
import { runExperiment } from "@arizeai/phoenix-client/experiments";
import { createEvaluator } from "@arizeai/phoenix-evals";

const hasGreeting = createEvaluator<{ output: string }>(
  ({ output }) => 
    ["hello", "hi", "hey"].some(w => output.toLowerCase().includes(w)) ? 1 : 0,
  { name: "has_greeting", kind: "CODE" }
);

const exactMatch = createEvaluator<{ output: string; expected: string }>(
  ({ output, expected }) => output.trim() === expected.trim() ? 1 : 0,
  { name: "exact_match", kind: "CODE" }
);

const experiment = await runExperiment({
  dataset: myDataset,
  task: myTask,
  evaluators: [hasGreeting, exactMatch],
});
```

#### More Information:

<Card title="Using Evaluators Documentation" icon="book" href="/docs/phoenix/datasets-and-experiments/how-to-experiments/using-evaluators" horizontal description="Evaluator usage guide"/>

