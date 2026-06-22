---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/vue/guides/dependent-queries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: dependent-queries
title: Dependent Queries
ref: docs/framework/react/guides/dependent-queries.md
---

[//]: # 'Example'

```js
// Get the user
const { data: user } = useQuery({
  queryKey: ['user', email],
  queryFn: () => getUserByEmail(email.value),
})

const userId = computed(() => user.value?.id)
const enabled = computed(() => !!user.value?.id)

// Then get the user's projects
const { isIdle, data: projects } = useQuery({
  queryKey: ['projects', userId],
  queryFn: () => getProjectsByUser(userId.value),
  enabled, // The query will not execute until `enabled == true`
})
```

[//]: # 'Example'
[//]: # 'Example2'

```tsx
// Get the users ids
const { data: userIds } = useQuery({
  queryKey: ['users'],
  queryFn: getUsersData,
  select: (users) => users.map((user) => user.id),
})

const queries = computed(() => {
  return userIds.value.length
    ? userIds.value.map((id) => {
        return {
          queryKey: ['messages', id],
          queryFn: () => getMessagesByUsers(id),
        }
      })
    : []
})

// Then get the users messages
const usersMessages = useQueries({
  queries, // if userIds.value is undefined or has no items, an empty array will be returned
})
```

[//]: # 'Example2'
