---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/dependent-queries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.418098Z"
---
# Dependent Queries

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
