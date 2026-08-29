---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/sdk-api-reference/typescript/packages/phoenix-evals/templates.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.816622Z"
---
# Templates

---
title: "Templates"
description: "Template helpers in @arizeai/phoenix-evals"
---

The template helpers make it easier to manage Mustache-style prompt templates separately from evaluator execution.

<section className="hidden" data-agent-context="relevant-source-files" aria-label="Relevant source files">
  <h2>Relevant Source Files</h2>
  <ul>
    <li><code>src/template/applyTemplate.ts</code></li>
    <li><code>src/template/getTemplateVariables.ts</code></li>
  </ul>
</section>

## Render A Template

```ts
import { formatTemplate } from "@arizeai/phoenix-evals";

const prompt = formatTemplate({
  template: [
    {
      role: "user",
      content: "Rate the answer to {{question}}",
    },
  ],
  variables: {
    question: "What is retrieval-augmented generation?",
  },
});
```

## Discover Variables

```ts
import { getTemplateVariables } from "@arizeai/phoenix-evals";

const variables = getTemplateVariables({
  template: "Answer {{question}} using {{context}}",
});
```

<section className="hidden" data-agent-context="source-map" aria-label="Source map">
  <h2>Source Map</h2>
  <ul>
    <li><code>src/template/applyTemplate.ts</code></li>
    <li><code>src/template/getTemplateVariables.ts</code></li>
    <li><code>src/template/createTemplateVariablesProxy.ts</code></li>
    <li><code>src/types/templating.ts</code></li>
  </ul>
</section>
