---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/query-functions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: query-functions
title: Query Functions
ref: docs/framework/react/guides/query-functions.md
---

[//]: # 'Example'

```tsx
useQuery(() => ({ queryKey: ['todos'], queryFn: fetchAllTodos }))
useQuery(() => ({
  queryKey: ['todos', todoId],
  queryFn: () => fetchTodoById(todoId),
}))
useQuery(() => ({
  queryKey: ['todos', todoId],
  queryFn: async () => {
    const data = await fetchTodoById(todoId)
    return data
  },
}))
useQuery(() => ({
  queryKey: ['todos', todoId],
  queryFn: ({ queryKey }) => fetchTodoById(queryKey[1]),
}))
```

[//]: # 'Example'
[//]: # 'Example2'

```tsx
const todosQuery = useQuery(() => ({
  queryKey: ['todos', todoId],
  queryFn: async () => {
    if (somethingGoesWrong) {
      throw new Error('Oh no!')
    }
    if (somethingElseGoesWrong) {
      return Promise.reject(new Error('Oh no!'))
    }

    return data
  },
}))
```

[//]: # 'Example2'
[//]: # 'Example3'

```tsx
useQuery(() => ({
  queryKey: ['todos', todoId],
  queryFn: async () => {
    const response = await fetch('/todos/' + todoId)
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
    return response.json()
  },
}))
```

[//]: # 'Example3'
[//]: # 'Example4'

```tsx
function Todos(props) {
  const todosQuery = useQuery(() => ({
    queryKey: ['todos', { status: props.status, page: props.page }],
    queryFn: fetchTodoList,
  }))
}

// Access the key, status and page variables in your query function!
function fetchTodoList({ queryKey }) {
  const [_key, { status, page }] = queryKey
  return new Promise()
}
```

[//]: # 'Example4'
