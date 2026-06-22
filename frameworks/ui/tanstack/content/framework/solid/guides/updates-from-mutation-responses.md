---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/updates-from-mutation-responses.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
