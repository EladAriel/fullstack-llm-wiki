---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/parallel-queries.md"
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
    'If the number of queries you need to execute is changing from render to render, you cannot use manual querying since that would violate the rules of hooks. Instead, ': '',
    'hook': 'function',
    'React': 'Angular',
    'hooks': 'functions',
    'useQuery': 'injectQuery',
    'useInfiniteQuery': 'injectInfiniteQuery',
    'useQueries': 'injectQueries',
  }
---

[//]: # 'Example'

```ts
export class AppComponent {
  // The following queries will execute in parallel
  usersQuery = injectQuery(() => ({ queryKey: ['users'], queryFn: fetchUsers }))
  teamsQuery = injectQuery(() => ({ queryKey: ['teams'], queryFn: fetchTeams }))
  projectsQuery = injectQuery(() => ({
    queryKey: ['projects'],
    queryFn: fetchProjects,
  }))
}
```

[//]: # 'Example'
[//]: # 'Info'
[//]: # 'Info'
[//]: # 'DynamicParallelIntro'

TanStack Query provides `injectQueries`, which you can use to dynamically execute as many queries in parallel as you'd like.

[//]: # 'DynamicParallelIntro'
[//]: # 'Example2'

```ts
export class AppComponent {
  users = signal<Array<User>>([])

  // Please note injectQueries is under development and this code does not work yet
  userQueries = injectQueries(() => ({
    queries: users().map((user) => {
      return {
        queryKey: ['user', user.id],
        queryFn: () => fetchUserById(user.id),
      }
    }),
  }))
}
```

[//]: # 'Example2'
