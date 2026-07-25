---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/sdk-api-reference/typescript/packages/phoenix-client/prompts.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.951228Z"
---
# Prompts

---
title: "Prompts"
description: "Manage prompts with @arizeai/phoenix-client"
---

The prompts module lets you create prompt versions in Phoenix, fetch them back by selector, list prompts, and adapt prompt versions to supported provider SDKs.

<section className="hidden" data-agent-context="relevant-source-files" aria-label="Relevant source files">
  <h2>Relevant Source Files</h2>
  <ul>
    <li><code>src/prompts/getPrompt.ts</code> for the exact selector shape</li>
  </ul>
</section>

## Create A Prompt

```ts
import {
  createPrompt,
  promptVersion,
} from "@arizeai/phoenix-client/prompts";

await createPrompt({
  name: "support-response",
  description: "Customer support reply prompt",
  version: promptVersion({
    modelProvider: "OPENAI",
    modelName: "gpt-4o-mini",
    template: [{ role: "user", content: "Reply to {{question}}" }],
  }),
});
```

## Fetch By Selector

```ts
import { getPrompt } from "@arizeai/phoenix-client/prompts";

const prompt = await getPrompt({
  prompt: { name: "support-response", tag: "production" },
});
```

`prompt` can be selected by `{ name }`, `{ name, tag }`, or `{ versionId }`.

## Convert To Another SDK

```ts
import { toSDK } from "@arizeai/phoenix-client/prompts";

const promptAsAI = toSDK({
  sdk: "ai",
  prompt,
  variables: { question: "Where is my order?" },
});
```

Supported `sdk` targets:

- `ai`
- `openai`
- `anthropic`

<section className="hidden" data-agent-context="source-map" aria-label="Source map">
  <h2>Source Map</h2>
  <ul>
    <li><code>src/prompts/createPrompt.ts</code></li>
    <li><code>src/prompts/getPrompt.ts</code></li>
    <li><code>src/prompts/listPrompts.ts</code></li>
    <li><code>src/prompts/sdks/toSDK.ts</code></li>
    <li><code>src/types/prompts.ts</code></li>
  </ul>
</section>
