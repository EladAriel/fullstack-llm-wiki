---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/useSuspenseQueries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.413851Z"
---
# Usesuspensequeries

---
id: useSuspenseQueries
title: useSuspenseQueries
---

```tsx
const result = useSuspenseQueries(options)
```

**Options**

The same as for [useQueries](./useQueries.md), except that each `query` can't have:

- `throwOnError`
- `enabled`
- `placeholderData`

> The [`select` typing caveat](./useQueries.md#typescript-typing-the-select-option) for `useQueries` applies here as well: annotate the `select` parameter or use the [`queryOptions`](./queryOptions.md) helper to keep type inference.

**Returns**

Same structure as [useQueries](./useQueries.md), except that for each `query`:

- `data` is guaranteed to be defined
- `isPlaceholderData` is missing
- `status` is either `success` or `error`
  - the derived flags are set accordingly.

**Caveats**

Keep in mind that the component will only re-mount after **all queries** have finished loading. Hence, if a query has gone stale in the time it took for all the queries to complete, it will be fetched again at re-mount. To avoid this, make sure to set a high enough `staleTime`.

[Cancellation](../guides/query-cancellation.md) does not work.
