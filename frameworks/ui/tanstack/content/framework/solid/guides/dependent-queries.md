---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/dependent-queries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.393587Z"
---
# Dependent Queries

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
