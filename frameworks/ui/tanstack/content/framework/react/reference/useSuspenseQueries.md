---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/useSuspenseQueries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useSuspenseQueries
title: useSuspenseQueries
---

```tsx
const result = useSuspenseQueries(options)
```

**Options**

The same as for [useQueries](./useQueries.md), except that each `query` can't have:

- `suspense`
- `throwOnError`
- `enabled`
- `placeholderData`

**Returns**

Same structure as [useQueries](./useQueries.md), except that for each `query`:

- `data` is guaranteed to be defined
- `isPlaceholderData` is missing
- `status` is either `success` or `error`
  - the derived flags are set accordingly.

**Caveats**

Keep in mind that the component will only re-mount after **all queries** have finished loading. Hence, if a query has gone stale in the time it took for all the queries to complete, it will be fetched again at re-mount. To avoid this, make sure to set a high enough `staleTime`.

[Cancellation](../guides/query-cancellation.md) does not work.
