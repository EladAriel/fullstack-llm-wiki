---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/parallel-queries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: parallel-queries
title: Parallel Queries
ref: docs/framework/react/guides/parallel-queries.md
replace:
  {
    '@tanstack/react-query': '@tanstack/solid-query',
    'useMutationState[(]': 'useMutationState(() => ',
    'useMutation[(]': 'useMutation(() => ',
    'useQuery[(]': 'useQuery(() => ',
    'useQueries[(]': 'useQueries(() => ',
    'useInfiniteQuery[(]': 'useInfiniteQuery(() => ',
    'hooks': 'functions',
  }
---

[//]: # 'Example'

```tsx
function App () {
  // The following queries will execute in parallel
  const usersQuery = useQuery(() => ({ queryKey: ['users'], queryFn: fetchUsers }))
  const teamsQuery = useQuery(() => ({ queryKey: ['teams'], queryFn: fetchTeams }))
  const projectsQuery = useQuery(() => ({ queryKey: ['projects'], queryFn: fetchProjects }))
  ...
}
```

[//]: # 'Example'
[//]: # 'Info'
[//]: # 'Info'
[//]: # 'DynamicParallelIntro'

If the number of queries you need to execute changes, you cannot use manual querying since that would break reactivity. Instead, TanStack Query provides a `useQueries` function, which you can use to dynamically execute as many queries in parallel as you'd like.

[//]: # 'DynamicParallelIntro'
[//]: # 'DynamicParallelDescription'

`useQueries` accepts an **accessor that returns an options object** with a **queries key** whose value is an **array of query objects**. It returns an **array of query results**:

[//]: # 'DynamicParallelDescription'
[//]: # 'Example2'

```tsx
function App(props) {
  const userQueries = useQueries(() => ({
    queries: props.users.map((user) => {
      return {
        queryKey: ['user', user.id],
        queryFn: () => fetchUserById(user.id),
      }
    }),
  }))
}
```

[//]: # 'Example2'
