---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/guides/query-functions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.383997Z"
---
# Query Functions

---
id: query-functions
title: Query Functions
---

A query function can be any function that returns a promise. The promise should resolve data or throw an error.

```ts
createQueryController(this, {
  queryKey: ['todos'],
  queryFn: fetchTodos,
})

createQueryController(this, () => ({
  queryKey: ['todo', this.todoId],
  queryFn: () => fetchTodo(this.todoId),
}))
```

## Handling Errors

TanStack Query needs failed query functions to throw or return a rejected promise. Some clients do that automatically. The browser `fetch` API does not, so check `response.ok` yourself:

```ts
async function fetchTodos(): Promise<Todo[]> {
  const response = await fetch('/api/todos')

  if (!response.ok) {
    throw new Error('Failed to fetch todos')
  }

  return response.json() as Promise<Todo[]>
}
```

The thrown error is available on the query result:

```ts
const query = this.todos()

if (query.isError) {
  return html`Error: ${query.error.message}`
}
```

## Query Function Context

TanStack Query passes a context object to every query function. It includes:

- `queryKey`: the current query key
- `client`: the `QueryClient`
- `signal`: an `AbortSignal` for cancellation
- `meta`: optional query metadata

```ts
createQueryController(this, {
  queryKey: ['todos', { status: 'open' }],
  queryFn: async ({ queryKey, signal }) => {
    const [, filters] = queryKey
    const response = await fetch(`/api/todos?status=${filters.status}`, {
      signal,
    })
    if (!response.ok) throw new Error('Failed to fetch todos')
    return response.json() as Promise<Todo[]>
  },
})
```

Infinite query functions also receive `pageParam`:

```ts
createInfiniteQueryController(this, {
  queryKey: ['projects'],
  queryFn: ({ pageParam }) => fetchProjectsPage(pageParam),
  initialPageParam: 1,
  getNextPageParam: (lastPage) =>
    lastPage.hasMore ? lastPage.page + 1 : undefined,
})
```

See [Infinite Queries](./infinite-queries.md) for the controller-specific behavior.
