---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/useIsFetching.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useIsFetching
title: useIsFetching
---

`useIsFetching` is an optional hook that returns the `number` of the queries that your application is loading or fetching in the background (useful for app-wide loading indicators).

```tsx
import { useIsFetching } from '@tanstack/react-query'
// How many queries are fetching?
const isFetching = useIsFetching()
// How many queries matching the posts prefix are fetching?
const isFetchingPosts = useIsFetching({ queryKey: ['posts'] })
```

**Options**

- `filters?: QueryFilters`: [Query Filters](../guides/filters.md#query-filters)
- `queryClient?: QueryClient`
  - Use this to use a custom QueryClient. Otherwise, the one from the nearest context will be used.

**Returns**

- `isFetching: number`
  - Will be the `number` of the queries that your application is currently loading or fetching in the background.
