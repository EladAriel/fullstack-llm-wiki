---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/infiniteQueryOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: infiniteQueryOptions
title: infiniteQueryOptions
---

```tsx
infiniteQueryOptions({
  queryKey,
  ...options,
})
```

**Options**

You can generally pass everything to `infiniteQueryOptions` that you can also pass to [`useInfiniteQuery`](./useInfiniteQuery.md). Some options will have no effect when then forwarded to a function like `queryClient.prefetchInfiniteQuery`, but TypeScript will still be fine with those excess properties.

- `queryKey: QueryKey`
  - **Required**
  - The query key to generate options for.

See [useInfiniteQuery](./useInfiniteQuery.md) for more information.
