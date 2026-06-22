---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/variables/queryClientContext.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: queryClientContext
title: queryClientContext
---

# Variable: queryClientContext

```ts
const queryClientContext: object;
```

Defined in: [packages/lit-query/src/context.ts:11](https://github.com/TanStack/query/blob/main/packages/lit-query/src/context.ts#L11)

Lit context key used by `QueryClientProvider` and host-bound APIs to share a
`QueryClient` through the DOM tree.

Most applications use `QueryClientProvider` instead of interacting with this
context directly.
