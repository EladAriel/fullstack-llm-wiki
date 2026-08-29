---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/query-functions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.419929Z"
---
# Query Functions

---
id: query-functions
title: Query Functions
ref: docs/framework/react/guides/query-functions.md
---

[//]: # 'Example'

```ts
injectQuery(() => ({ queryKey: ['todos'], queryFn: fetchAllTodos }))
injectQuery(() => ({
  queryKey: ['todos', todoId],
  queryFn: () => fetchTodoById(todoId),
}))
injectQuery(() => ({
  queryKey: ['todos', todoId],
  queryFn: async () => {
    const data = await fetchTodoById(todoId)
    return data
  },
}))
injectQuery(() => ({
  queryKey: ['todos', todoId],
  queryFn: ({ queryKey }) => fetchTodoById(queryKey[1]),
}))
```

[//]: # 'Example'
[//]: # 'Example2'

```ts
todos = injectQuery(() => ({
  queryKey: ['todos', todoId()],
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

```ts
todos = injectQuery(() => ({
  queryKey: ['todos', todoId()],
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

```ts
result = injectQuery(() => ({
  queryKey: ['todos', { status: status(), page: page() }],
  queryFn: fetchTodoList,
}))

// Access the key, status and page variables in your query function!
function fetchTodoList({ queryKey }) {
  const [_key, { status, page }] = queryKey
  return new Promise()
}
```

[//]: # 'Example4'
