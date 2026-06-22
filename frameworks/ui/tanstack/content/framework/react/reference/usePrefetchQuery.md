---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/usePrefetchQuery.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: usePrefetchQuery
title: usePrefetchQuery
---

```tsx
usePrefetchQuery(options)
```

**Options**

You can pass everything to `usePrefetchQuery` that you can pass to [`queryClient.prefetchQuery`](../../../reference/QueryClient.md#queryclientprefetchquery). Remember that some of them are required as below:

- `queryKey: QueryKey`
  - **Required**
  - The query key to prefetch during render

- `queryFn: (context: QueryFunctionContext) => Promise<TData>`
  - **Required, but only if no default query function has been defined** See [Default Query Function](../guides/default-query-function.md) for more information.

**Returns**

The `usePrefetchQuery` does not return anything, it should be used just to fire a prefetch during render, before a suspense boundary that wraps a component that uses [`useSuspenseQuery`](./useSuspenseQuery.md).
