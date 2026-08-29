---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/guides/query-keys.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.384301Z"
---
# Query Keys

---
id: query-keys
title: Query Keys
---

TanStack Query manages caching by query key. Query keys must be arrays at the top level, and they should uniquely describe the data returned by the query function.

## Simple Keys

Use simple keys for list resources or non-hierarchical data:

```ts
createQueryController(this, {
  queryKey: ['todos'],
  queryFn: fetchTodos,
})

createQueryController(this, {
  queryKey: ['settings'],
  queryFn: fetchSettings,
})
```

## Keys with Variables

Include variables when they change what the query fetches:

```ts
createQueryController(this, () => ({
  queryKey: ['todo', this.todoId],
  queryFn: () => fetchTodo(this.todoId),
}))

createQueryController(this, () => ({
  queryKey: ['projects', { page: this.page, filter: this.filter }],
  queryFn: () => fetchProjects({ page: this.page, filter: this.filter }),
}))
```

The pagination example uses a key shaped like this:

```ts
type ProjectsQueryKey = readonly ['projects', number, number, boolean]

function projectsQueryKey(
  page: number,
  delayMs: number,
  forceError: boolean,
): ProjectsQueryKey {
  return ['projects', page, delayMs, forceError] as const
}
```

## Deterministic Hashing

Object key order does not matter inside a query key:

```ts
const keyA = ['todos', { status, page }]
const keyB = ['todos', { page, status }]
```

Array item order does matter:

```ts
const keyA = ['todos', status, page]
const keyB = ['todos', page, status]
```

## Query Keys as Dependencies

If your query function reads a reactive host property, include that value in the query key:

```ts
class UserTodos extends LitElement {
  userId = ''

  private readonly todos = createQueryController(this, () => ({
    queryKey: ['todos', this.userId],
    queryFn: () => fetchTodos(this.userId),
  }))
}
```

This lets Lit Query cache each user's todos separately and refetch when the host state changes.
