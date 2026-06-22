---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/invalidations-from-mutations.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: invalidations-from-mutations
title: Invalidations from Mutations
ref: docs/framework/react/guides/invalidations-from-mutations.md
replace: { 'useMutation': 'injectMutation', 'hook': 'function' }
---

[//]: # 'Example'

```ts
mutation = injectMutation(() => ({
  mutationFn: postTodo,
}))
```

[//]: # 'Example'
[//]: # 'Example2'

```ts
import {
  injectMutation,
  QueryClient,
} from '@tanstack/angular-query-experimental'

export class TodosComponent {
  queryClient = inject(QueryClient)

  // When this mutation succeeds, invalidate any queries with the `todos` or `reminders` query key
  mutation = injectMutation(() => ({
    mutationFn: addTodo,
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['todos'] })
      this.queryClient.invalidateQueries({ queryKey: ['reminders'] })
    },
  }))
}
```

[//]: # 'Example2'

You can wire up your invalidations to happen using any of the callbacks available in the [`injectMutation` function](./mutations.md)
