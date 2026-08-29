---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/query-keys.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.420380Z"
---
# Query Keys

---
id: query-keys
title: Query Keys
ref: docs/framework/react/guides/query-keys.md
#todo: exhaustive-deps is at least for now React-only
---

[//]: # 'Example'

```ts
// A list of todos
injectQuery(() => ({ queryKey: ['todos'], ... }))

// Something else, whatever!
injectQuery(() => ({ queryKey: ['something', 'special'], ... }))
```

[//]: # 'Example'
[//]: # 'Example2'

```ts
// An individual todo
injectQuery(() => ({queryKey: ['todo', 5], ...}))

// An individual todo in a "preview" format
injectQuery(() => ({queryKey: ['todo', 5, {preview: true}], ...}))

// A list of todos that are "done"
injectQuery(() => ({queryKey: ['todos', {type: 'done'}], ...}))
```

[//]: # 'Example2'
[//]: # 'Example3'

```ts
injectQuery(() => ({ queryKey: ['todos', { status, page }], ... }))
injectQuery(() => ({ queryKey: ['todos', { page, status }], ...}))
injectQuery(() => ({ queryKey: ['todos', { page, status, other: undefined }], ... }))
```

[//]: # 'Example3'
[//]: # 'Example4'

```ts
injectQuery(() => ({ queryKey: ['todos', status, page], ... }))
injectQuery(() => ({ queryKey: ['todos', page, status], ...}))
injectQuery(() => ({ queryKey: ['todos', undefined, page, status], ...}))
```

[//]: # 'Example4'
[//]: # 'Example5'

```ts
todoId = signal(-1)

injectQuery(() => ({
  enabled: todoId() > 0,
  queryKey: ['todos', todoId()],
  queryFn: () => fetchTodoById(todoId()),
}))
```

[//]: # 'Example5'
[//]: # 'Materials'
[//]: # 'Materials'
