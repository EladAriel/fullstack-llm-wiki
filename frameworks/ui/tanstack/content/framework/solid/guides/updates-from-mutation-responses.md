---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/updates-from-mutation-responses.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: updates-from-mutation-responses
title: Updates from Mutation Responses
ref: docs/framework/react/guides/updates-from-mutation-responses.md
replace: { 'hook': 'function' }
---

[//]: # 'Example'

```tsx
const queryClient = useQueryClient()

const mutation = useMutation(() => ({
  mutationFn: editTodo,
  onSuccess: (data) => {
    queryClient.setQueryData(['todo', { id: 5 }], data)
  },
}))

mutation.mutate({
  id: 5,
  name: 'Do the laundry',
})

// The query below will be updated with the response from the
// successful mutation
const todoQuery = useQuery(() => ({
  queryKey: ['todo', { id: 5 }],
  queryFn: fetchTodoById,
}))
```

[//]: # 'Example'
[//]: # 'Example2'

```tsx
const useMutateTodo = () => {
  const queryClient = useQueryClient()

  return useMutation(() => ({
    mutationFn: editTodo,
    // Notice the second argument is the variables object that the `mutate` function receives
    onSuccess: (data, variables) => {
      queryClient.setQueryData(['todo', { id: variables.id }], data)
    },
  }))
}
```

[//]: # 'Example2'
