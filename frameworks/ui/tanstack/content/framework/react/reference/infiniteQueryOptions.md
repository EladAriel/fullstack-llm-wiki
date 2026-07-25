---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/infiniteQueryOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
