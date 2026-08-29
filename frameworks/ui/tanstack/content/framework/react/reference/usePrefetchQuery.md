---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/usePrefetchQuery.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.414625Z"
---
# Useprefetchquery

---
id: usePrefetchQuery
title: usePrefetchQuery
---

```tsx
usePrefetchQuery(options)
```

**Options**

You can pass everything to `usePrefetchQuery` that you can pass to [`queryClient.query`](../../../reference/QueryClient.md#queryclient-query). Remember that some of them are required as below:

- `queryKey: QueryKey`
  - **Required**
  - The query key to prefetch during render

- `queryFn: (context: QueryFunctionContext<TQueryKey>) => TQueryFnData | Promise<TQueryFnData>`
  - **Required, but only if no default query function has been defined** See [Default Query Function](../guides/default-query-function.md) for more information.

**Returns**

The `usePrefetchQuery` does not return anything, it should be used just to fire a prefetch during render, before a suspense boundary that wraps a component that uses [`useSuspenseQuery`](./useSuspenseQuery.md).
