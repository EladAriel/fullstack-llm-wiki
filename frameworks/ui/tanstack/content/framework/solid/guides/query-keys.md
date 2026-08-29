---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/query-keys.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.396303Z"
---
# Query Keys

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
