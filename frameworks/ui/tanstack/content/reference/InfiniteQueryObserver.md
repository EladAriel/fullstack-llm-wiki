---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/reference/InfiniteQueryObserver.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.356753Z"
---
# Infinitequeryobserver

---
id: InfiniteQueryObserver
title: InfiniteQueryObserver
---

The `InfiniteQueryObserver` can be used to observe and switch between infinite queries.

```tsx
const observer = new InfiniteQueryObserver(queryClient, {
  queryKey: ['posts'],
  queryFn: fetchPosts,
  getNextPageParam: (lastPage, allPages) => lastPage.nextCursor,
  getPreviousPageParam: (firstPage, allPages) => firstPage.prevCursor,
})

const unsubscribe = observer.subscribe((result) => {
  console.log(result)
  unsubscribe()
})
```

**Options**

The options for the `InfiniteQueryObserver` are exactly the same as those of [`useInfiniteQuery`](../framework/react/reference/useInfiniteQuery).
