---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/vue/guides/queries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: queries
title: Queries
ref: docs/framework/react/guides/queries.md
---

[//]: # 'Example'

```ts
import { useQuery } from '@tanstack/vue-query'

const result = useQuery({ queryKey: ['todos'], queryFn: fetchTodoList })
```

[//]: # 'Example'
[//]: # 'Example3'

```vue
<script setup>
import { useQuery } from '@tanstack/vue-query'

const { isPending, isError, data, error } = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
})
</script>

<template>
  <span v-if="isPending">Loading...</span>
  <span v-else-if="isError">Error: {{ error.message }}</span>
  <!-- We can assume by this point that `isSuccess === true` -->
  <ul v-else-if="data">
    <li v-for="todo in data" :key="todo.id">{{ todo.title }}</li>
  </ul>
</template>
```

[//]: # 'Example3'
[//]: # 'Example4'

```vue
<script setup>
import { useQuery } from '@tanstack/vue-query'

const { status, data, error } = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
})
</script>

<template>
  <span v-if="status === 'pending'">Loading...</span>
  <span v-else-if="status === 'error'">Error: {{ error.message }}</span>
  <!-- also status === 'success', but "else" logic works, too -->
  <ul v-else-if="data">
    <li v-for="todo in data" :key="todo.id">{{ todo.title }}</li>
  </ul>
</template>
```

[//]: # 'Example4'
[//]: # 'Materials'
[//]: # 'Materials'
