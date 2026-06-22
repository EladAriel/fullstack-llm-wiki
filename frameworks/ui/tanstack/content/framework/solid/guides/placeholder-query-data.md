---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/placeholder-query-data.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

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
