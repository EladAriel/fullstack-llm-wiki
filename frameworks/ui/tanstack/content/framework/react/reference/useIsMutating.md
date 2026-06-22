---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/reference/useIsMutating.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useIsMutating
title: useIsMutating
---

`useIsMutating` is an optional hook that returns the `number` of mutations that your application is fetching (useful for app-wide loading indicators).

```tsx
import { useIsMutating } from '@tanstack/react-query'
// How many mutations are fetching?
const isMutating = useIsMutating()
// How many mutations matching the posts prefix are fetching?
const isMutatingPosts = useIsMutating({ mutationKey: ['posts'] })
```

**Options**

- `filters?: MutationFilters`: [Mutation Filters](../guides/filters.md#mutation-filters)
- `queryClient?: QueryClient`
  - Use this to use a custom QueryClient. Otherwise, the one from the nearest context will be used.

**Returns**

- `isMutating: number`
  - Will be the `number` of the mutations that your application is currently fetching.
