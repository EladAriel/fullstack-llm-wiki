---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/query-invalidation.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: query-invalidation
title: Query Invalidation
ref: docs/framework/react/guides/query-invalidation.md
replace: { 'useQuery': 'injectQuery', 'hooks': 'functions' }
---

[//]: # 'Example2'

```ts
import { injectQuery, QueryClient } from '@tanstack/angular-query-experimental'

class QueryInvalidationExample {
  queryClient = inject(QueryClient)

  invalidateQueries() {
    this.queryClient.invalidateQueries({ queryKey: ['todos'] })
  }

  // Both queries below will be invalidated
  todoListQuery = injectQuery(() => ({
    queryKey: ['todos'],
    queryFn: fetchTodoList,
  }))
  todoListQuery = injectQuery(() => ({
    queryKey: ['todos', { page: 1 }],
    queryFn: fetchTodoList,
  }))
}
```

[//]: # 'Example2'

You can even invalidate queries with specific variables by passing a more specific query key to the `invalidateQueries` method:

[//]: # 'Example3'

```ts
queryClient.invalidateQueries({
  queryKey: ['todos', { type: 'done' }],
})

// The query below will be invalidated
todoListQuery = injectQuery(() => ({
  queryKey: ['todos', { type: 'done' }],
  queryFn: fetchTodoList,
}))

// However, the following query below will NOT be invalidated
todoListQuery = injectQuery(() => ({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
}))
```

[//]: # 'Example3'

The `invalidateQueries` API is very flexible, so even if you want to **only** invalidate `todos` queries that don't have any more variables or subkeys, you can pass an `exact: true` option to the `invalidateQueries` method:

[//]: # 'Example4'

```ts
queryClient.invalidateQueries({
  queryKey: ['todos'],
  exact: true,
})

// The query below will be invalidated
todoListQuery = injectQuery(() => ({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
}))

// However, the following query below will NOT be invalidated
const todoListQuery = injectQuery(() => ({
  queryKey: ['todos', { type: 'done' }],
  queryFn: fetchTodoList,
}))
```

[//]: # 'Example4'

If you find yourself wanting **even more** granularity, you can pass a predicate function to the `invalidateQueries` method. This function will receive each `Query` instance from the query cache and allow you to return `true` or `false` for whether you want to invalidate that query:

[//]: # 'Example5'

```ts
queryClient.invalidateQueries({
  predicate: (query) =>
    query.queryKey[0] === 'todos' && query.queryKey[1]?.version >= 10,
})

// The query below will be invalidated
todoListQuery = injectQuery(() => ({
  queryKey: ['todos', { version: 20 }],
  queryFn: fetchTodoList,
}))

// The query below will be invalidated
todoListQuery = injectQuery(() => ({
  queryKey: ['todos', { version: 10 }],
  queryFn: fetchTodoList,
}))

// However, the following query below will NOT be invalidated
todoListQuery = injectQuery(() => ({
  queryKey: ['todos', { version: 5 }],
  queryFn: fetchTodoList,
}))
```

[//]: # 'Example5'
