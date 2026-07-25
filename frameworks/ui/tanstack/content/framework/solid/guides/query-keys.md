---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/query-keys.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: query-keys
title: Query Keys
ref: docs/framework/react/guides/query-keys.md
replace:
  {
    '@tanstack/react-query': '@tanstack/solid-query',
    'useMutationState[(]': 'useMutationState(() => ',
    'useMutation[(]': 'useMutation(() => ',
    'useQuery[(]': 'useQuery(() => ',
    'useQueries[(]': 'useQueries(() => ',
    'useInfiniteQuery[(]': 'useInfiniteQuery(() => ',
    'React Query Keys': 'TanStack Query Keys',
  }
---

[//]: # 'Example'

```tsx
// A list of todos
useQuery(() => ({ queryKey: ['todos'], ... }))

// Something else, whatever!
useQuery(() => ({ queryKey: ['something', 'special'], ... }))
```

[//]: # 'Example'
[//]: # 'Example2'

```tsx
// An individual todo
useQuery(() => ({ queryKey: ['todo', 5], ... }))

// An individual todo in a "preview" format
useQuery(() => ({ queryKey: ['todo', 5, { preview: true }], ...}))

// A list of todos that are "done"
useQuery(() => ({ queryKey: ['todos', { type: 'done' }], ... }))
```

[//]: # 'Example2'
[//]: # 'Example3'

```tsx
useQuery(() => ({ queryKey: ['todos', { status, page }], ... }))
useQuery(() => ({ queryKey: ['todos', { page, status }], ...}))
useQuery(() => ({ queryKey: ['todos', { page, status, other: undefined }], ... }))
```

[//]: # 'Example3'
[//]: # 'Example4'

```tsx
useQuery(() => ({ queryKey: ['todos', status, page], ... }))
useQuery(() => ({ queryKey: ['todos', page, status], ...}))
useQuery(() => ({ queryKey: ['todos', undefined, page, status], ...}))
```

[//]: # 'Example4'
[//]: # 'Example5'

```tsx
function Todos(props) {
  const todosQuery = useQuery(() => ({
    queryKey: ['todos', props.todoId],
    queryFn: () => fetchTodoById(props.todoId),
  }))
}
```

[//]: # 'Example5'
