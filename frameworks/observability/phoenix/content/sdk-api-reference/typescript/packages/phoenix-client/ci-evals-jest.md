---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/sdk-api-reference/typescript/packages/phoenix-client/ci-evals-jest.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.948495Z"
---
# Ci Evals Jest

---
title: "CI Eval Tests: Jest"
description: "Wire @arizeai/phoenix-client/jest into a Jest project"
---

`@arizeai/phoenix-client/jest` exposes the same API as the Vitest
entrypoint but binds to Jest's globals (`describe`, `test`, `it`,
`beforeAll`, `afterAll`).

## Setup

Create a separate `phoenix.jest.config.cjs`:

```js
module.exports = {
  testMatch: ["**/*.eval.?(c|m)[jt]s"],
  reporters: ["default", "@arizeai/phoenix-client/jest/reporter"],
  setupFiles: ["dotenv/config"],
  testTimeout: 30000,
};
```

- `testMatch` keeps eval suites separate from regular tests.
- `reporters` keeps Jest's default reporter and adds the Phoenix
  summary block at the end of the run.
- `setupFiles: ["dotenv/config"]` loads `PHOENIX_HOST`, `PHOENIX_API_KEY`,
  and other env vars from `.env`.
- `testTimeout` is bumped because LLM calls can be slow.

<Note>
The `jsdom` test environment is not supported. Either omit
`testEnvironment` or set it to `"node"`. For TypeScript or ESM use
`ts-jest` / `@swc/jest` per Jest's docs.
</Note>

Add a script to `package.json`:

```json
{
  "scripts": {
    "eval": "jest --config phoenix.jest.config.cjs"
  }
}
```

## API

```ts
import * as px from "@arizeai/phoenix-client/jest";
```

The exported names match the Vitest entrypoint exactly:

- `describe`, `describe.only`, `describe.skip`
- `test`, `test.only`, `test.skip`, `test.each`
- `it` (alias for `test`)
- `logOutput`, `logAnnotation`, `evaluate`

See [CI Eval Tests: Vitest](./ci-evals-vitest) for the full API reference — the surface is
identical. The only difference is the import path and the underlying
runner.

## Notes

- This module reads Jest globals off `globalThis` at suite-declaration
  time, so importing it outside of a Jest test run will throw with a
  helpful error message.
- Jest's `--bail` flag will short-circuit the experiment; the Phoenix
  reporter still prints a summary for the suites that ran.

<section className="hidden" data-agent-context="source-map" aria-label="Source map">
  <h2>Source Map</h2>
  <ul>
    <li><code>src/jest/index.ts</code></li>
    <li><code>src/jest/reporter.ts</code></li>
    <li><code>src/testing/runner.ts</code></li>
  </ul>
</section>
