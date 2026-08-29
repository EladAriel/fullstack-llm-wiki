---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/placeholder-query-data.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.392957Z"
---
# Placeholder Query Data

---
id: placeholder-query-data
title: Placeholder Query Data
ref: docs/framework/react/guides/placeholder-query-data.md
---

[//]: # 'ExampleValue'

```tsx
function Todos() {
  const todosQuery = useQuery(() => ({
    queryKey: ['todos'],
    queryFn: () => fetch('/todos'),
    placeholderData: placeholderTodos,
  }))
}
```

[//]: # 'ExampleValue'
[//]: # 'Memoization'

### Placeholder Data Memoization

If the process for accessing a query's placeholder data is intensive or just not something you want to perform on every render, you can memoize the value:

```tsx
function Todos() {
  const placeholderData = createMemo(() => generateFakeTodos())
  const todosQuery = useQuery(() => ({
    queryKey: ['todos'],
    queryFn: () => fetch('/todos'),
    placeholderData: placeholderData(),
  }))
}
```

[//]: # 'Memoization'
[//]: # 'ExampleFunction'

```tsx
const todosQuery = useQuery(() => ({
  queryKey: ['todos', id],
  queryFn: () => fetch(`/todos/${id}`),
  placeholderData: (previousData, previousQuery) => previousData,
}))
```

[//]: # 'ExampleFunction'
[//]: # 'ExampleCache'

```tsx
function BlogPost(props) {
  const queryClient = useQueryClient()
  const blogPostQuery = useQuery(() => ({
    queryKey: ['blogPost', props.blogPostId],
    queryFn: () => fetch(`/blogPosts/${props.blogPostId}`),
    placeholderData: () => {
      // Use the smaller/preview version of the blogPost from the 'blogPosts'
      // query as the placeholder data for this blogPost query
      return queryClient
        .getQueryData(['blogPosts'])
        ?.find((d) => d.id === props.blogPostId)
    },
  }))
}
```

[//]: # 'ExampleCache'
