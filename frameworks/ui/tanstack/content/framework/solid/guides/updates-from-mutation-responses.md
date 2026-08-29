---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/updates-from-mutation-responses.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.393882Z"
---
# Updates From Mutation Responses

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
