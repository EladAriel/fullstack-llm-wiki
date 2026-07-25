---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/dependent-queries.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: dependent-queries
title: Dependent Queries
ref: docs/framework/react/guides/dependent-queries.md
replace: { 'useQuery': 'injectQuery', 'useQueries': 'injectQueries' }
---

[//]: # 'Example'

```ts
// Get the user
userQuery = injectQuery(() => ({
  queryKey: ['user', email],
  queryFn: getUserByEmail,
}))

// Then get the user's projects
projectsQuery = injectQuery(() => ({
  queryKey: ['projects', this.userQuery.data()?.id],
  queryFn: getProjectsByUser,
  // The query will not execute until the user id exists
  enabled: !!this.userQuery.data()?.id,
}))
```

[//]: # 'Example'
[//]: # 'Example2'

```ts
// injectQueries is under development for Angular Query
```

[//]: # 'Example2'
