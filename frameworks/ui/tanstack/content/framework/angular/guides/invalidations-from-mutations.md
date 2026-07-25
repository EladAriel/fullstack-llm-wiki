---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/invalidations-from-mutations.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
