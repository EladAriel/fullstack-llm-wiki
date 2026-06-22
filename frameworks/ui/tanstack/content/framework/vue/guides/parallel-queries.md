---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/vue/guides/parallel-queries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

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
