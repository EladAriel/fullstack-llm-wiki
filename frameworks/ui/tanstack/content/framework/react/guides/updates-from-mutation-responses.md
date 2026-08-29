---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/guides/updates-from-mutation-responses.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.409246Z"
---
# Updates From Mutation Responses

---
id: updates-from-mutation-responses
title: Updates from Mutation Responses
---

When dealing with mutations that **update** objects on the server, it's common for the new object to be automatically returned in the response of the mutation. Instead of refetching any queries for that item and wasting a network call for data we already have, we can take advantage of the object returned by the mutation function and update the existing query with the new data immediately using the [Query Client's `setQueryData`](../../../reference/QueryClient.md#queryclientsetquerydata) method:

[//]: # 'Example'

```tsx
const queryClient = useQueryClient()

const mutation = useMutation({
  mutationFn: editTodo,
  onSuccess: (data) => {
    queryClient.setQueryData(['todo', { id: 5 }], data)
  },
})

mutation.mutate({
  id: 5,
  name: 'Do the laundry',
})

// The query below will be updated with the response from the
// successful mutation
const { status, data, error } = useQuery({
  queryKey: ['todo', { id: 5 }],
  queryFn: fetchTodoById,
})
```

[//]: # 'Example'

You might want to tie the `onSuccess` logic into a reusable mutation, for that you can
create a custom hook like this:

[//]: # 'Example2'

```tsx
const useMutateTodo = () => {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: editTodo,
    // Notice the second argument is the variables object that the `mutate` function receives
    onSuccess: (data, variables) => {
      queryClient.setQueryData(['todo', { id: variables.id }], data)
    },
  })
}
```

[//]: # 'Example2'

## Immutability

Updates via `setQueryData` must be performed in an _immutable_ way. **DO NOT** attempt to write directly to the cache by mutating data (that you retrieved from the cache) in place. It might work at first but can lead to subtle bugs along the way.

[//]: # 'Example3'

```tsx
queryClient.setQueryData(['posts', { id }], (oldData) => {
  if (oldData) {
    // ❌ do not try this
    oldData.title = 'my new post title'
  }
  return oldData
})

queryClient.setQueryData(
  ['posts', { id }],
  // ✅ this is the way
  (oldData) =>
    oldData
      ? {
          ...oldData,
          title: 'my new post title',
        }
      : oldData,
)
```

[//]: # 'Example3'
