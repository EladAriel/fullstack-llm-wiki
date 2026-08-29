---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/placeholder-query-data.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.417789Z"
---
# Placeholder Query Data

---
id: placeholder-query-data
title: Placeholder Query Data
ref: docs/framework/react/guides/placeholder-query-data.md
---

[//]: # 'ExampleValue'

```ts
class TodosComponent {
  result = injectQuery(() => ({
    queryKey: ['todos'],
    queryFn: () => fetch('/todos'),
    placeholderData: placeholderTodos,
  }))
}
```

[//]: # 'ExampleValue'
[//]: # 'Memoization'
[//]: # 'Memoization'
[//]: # 'ExampleFunction'

```ts
class TodosComponent {
  result = injectQuery(() => ({
    queryKey: ['todos', id()],
    queryFn: () => fetch(`/todos/${id}`),
    placeholderData: (previousData, previousQuery) => previousData,
  }))
}
```

[//]: # 'ExampleFunction'
[//]: # 'ExampleCache'

```ts
export class BlogPostComponent {
  postId = input.required<number>()
  queryClient = inject(QueryClient)

  result = injectQuery(() => ({
    queryKey: ['blogPost', this.postId()],
    queryFn: () => fetch(`/blogPosts/${this.postId()}`),
    placeholderData: () => {
      // Use the smaller/preview version of the blogPost from the 'blogPosts'
      // query as the placeholder data for this blogPost query
      return this.queryClient
        .getQueryData(['blogPosts'])
        ?.find((d) => d.id === this.postId())
    },
  }))
}
```

[//]: # 'ExampleCache'
[//]: # 'Materials'
[//]: # 'Materials'
