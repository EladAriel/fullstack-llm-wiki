---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/queryOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.414168Z"
---
# Queryoptions

---
id: queryOptions
title: queryOptions
---

```tsx
queryOptions({
  queryKey,
  ...options,
})
```

**Options**

You can generally pass everything to `queryOptions` that you can also pass to [`useQuery`](./useQuery.md). These options can be shared across hooks and imperative APIs such as `queryClient.query`.

- `queryKey: QueryKey`
  - **Required**
  - The query key to generate options for.
[//]: # 'Materials'

## Further reading

To learn more about `QueryOptions`, have a look at [this article by TkDodo The Query Options API](https://tkdodo.eu/blog/the-query-options-api).

[//]: # 'Materials'
