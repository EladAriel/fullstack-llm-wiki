---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/useSuspenseInfiniteQuery.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: useSuspenseInfiniteQuery
title: useSuspenseInfiniteQuery
---

```tsx
const result = useSuspenseInfiniteQuery(options)
```

**Options**

The same as for [useInfiniteQuery](./useInfiniteQuery.md), except for:

- `suspense`
- `throwOnError`
- `enabled`
- `placeholderData`

**Returns**

Same object as [useInfiniteQuery](./useInfiniteQuery.md), except that:

- `data` is guaranteed to be defined
- `isPlaceholderData` is missing
- `status` is either `success` or `error`
  - the derived flags are set accordingly.

**Caveat**

[Cancellation](../guides/query-cancellation.md) does not work.
