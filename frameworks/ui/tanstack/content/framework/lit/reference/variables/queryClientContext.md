---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/variables/queryClientContext.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
