---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/useSuspenseQuery.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useSuspenseQuery
title: useSuspenseQuery
---

```tsx
const result = useSuspenseQuery(options)
```

**Options**

The same as for [useQuery](./useQuery.md), except for:

- `throwOnError`
- `enabled`
- `placeholderData`

**Returns**

Same object as [useQuery](./useQuery.md), except that:

- `data` is guaranteed to be defined
- `isPlaceholderData` is missing
- `status` is either `success` or `error`
  - the derived flags are set accordingly.

**Caveat**

[Cancellation](../guides/query-cancellation.md) does not work.
