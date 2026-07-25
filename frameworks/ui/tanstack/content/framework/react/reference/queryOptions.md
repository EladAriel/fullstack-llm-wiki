---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/queryOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
