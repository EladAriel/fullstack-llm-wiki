---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/vue/guides/placeholder-query-data.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: placeholder-query-data
title: Placeholder Query Data
ref: docs/framework/react/guides/placeholder-query-data.md
---

[//]: # 'ExampleValue'

```tsx
const result = useQuery({
  queryKey: ['todos'],
  queryFn: () => fetch('/todos'),
  placeholderData: placeholderTodos,
})
```

[//]: # 'ExampleValue'
[//]: # 'Memoization'
[//]: # 'Memoization'
[//]: # 'ExampleCache'

```tsx
const result = useQuery({
  queryKey: ['blogPost', blogPostId],
  queryFn: () => fetch(`/blogPosts/${blogPostId}`),
  placeholderData: () => {
    // Use the smaller/preview version of the blogPost from the 'blogPosts'
    // query as the placeholder data for this blogPost query
    return queryClient
      .getQueryData(['blogPosts'])
      ?.find((d) => d.id === blogPostId)
  },
})
```

[//]: # 'ExampleCache'
[//]: # 'Materials'
[//]: # 'Materials'
