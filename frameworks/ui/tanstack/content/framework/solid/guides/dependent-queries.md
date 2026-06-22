---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/dependent-queries.md"
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

```tsx
// Get the user
const userQuery = useQuery(() => ({
  queryKey: ['user', email],
  queryFn: getUserByEmail,
}))

const userId = () => userQuery.data?.id

// Then get the user's projects
const projectsQuery = useQuery(() => ({
  queryKey: ['projects', userId()],
  queryFn: getProjectsByUser,
  // The query will not execute until the userId exists
  enabled: !!userId(),
}))
```

[//]: # 'Example'
[//]: # 'Example2'

```tsx
// Get the users ids
const usersQuery = useQuery(() => ({
  queryKey: ['users'],
  queryFn: getUsersData,
  select: (users) => users.map((user) => user.id),
}))

// Then get the users messages
const usersMessages = useQueries(() => ({
  queries: usersQuery.data
    ? usersQuery.data.map((id) => {
        return {
          queryKey: ['messages', id],
          queryFn: () => getMessagesByUsers(id),
        }
      })
    : [], // if usersQuery.data is undefined, an empty array will be returned
}))
```

[//]: # 'Example2'
