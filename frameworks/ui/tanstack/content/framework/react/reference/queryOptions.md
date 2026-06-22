---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/queryOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

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

You can generally pass everything to `queryOptions` that you can also pass to [`useQuery`](./useQuery.md). Some options will have no effect when then forwarded to a function like `queryClient.prefetchQuery`, but TypeScript will still be fine with those excess properties.

- `queryKey: QueryKey`
  - **Required**
  - The query key to generate options for.
- `experimental_prefetchInRender?: boolean`
  - Optional
  - Defaults to `false`
  - When set to `true`, queries will be prefetched during render, which can be useful for certain optimization scenarios
  - Needs to be turned on for the experimental `useQuery().promise` functionality

[//]: # 'Materials'

## Further reading

To learn more about `QueryOptions`, have a look at [this article by TkDodo The Query Options API](https://tkdodo.eu/blog/the-query-options-api).

[//]: # 'Materials'
