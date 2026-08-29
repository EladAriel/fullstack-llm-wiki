---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/vue/guides/parallel-queries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.434171Z"
---
# Parallel Queries

---
id: parallel-queries
title: Parallel Queries
ref: docs/framework/react/guides/parallel-queries.md
---

[//]: # 'Example'

```vue
<script setup lang="ts">
// The following queries will execute in parallel
const usersQuery = useQuery({ queryKey: ['users'], queryFn: fetchUsers })
const teamsQuery = useQuery({ queryKey: ['teams'], queryFn: fetchTeams })
const projectsQuery = useQuery({
  queryKey: ['projects'],
  queryFn: fetchProjects,
})
</script>
```

[//]: # 'Example'
[//]: # 'Info'
[//]: # 'Info'
[//]: # 'Example2'

```js
const users = computed(...)
const queries = computed(() => users.value.map(user => {
    return {
      queryKey: ['user', user.id],
      queryFn: () => fetchUserById(user.id),
    }
  })
);
const userQueries = useQueries({queries: queries})
```

[//]: # 'Example2'
