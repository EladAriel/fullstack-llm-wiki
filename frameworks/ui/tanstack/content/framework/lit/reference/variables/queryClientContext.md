---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/variables/queryClientContext.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.387211Z"
---
# Queryclientcontext

---
id: queryClientContext
title: queryClientContext
---

```ts
const queryClientContext: object;
```

Defined in: [packages/lit-query/src/context.ts:11](https://github.com/TanStack/query/blob/main/packages/lit-query/src/context.ts#L11)

Lit context key used by `QueryClientProvider` and host-bound APIs to share a
`QueryClient` through the DOM tree.

Most applications use `QueryClientProvider` instead of interacting with this
context directly.
