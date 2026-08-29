---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/vue/guides/infinite-queries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.430322Z"
---
# Infinite Queries

---
id: infinite-queries
title: Infinite Queries
ref: docs/framework/react/guides/infinite-queries.md
---

[//]: # 'Example'

```vue
<script setup>
import { useInfiniteQuery } from '@tanstack/vue-query'

const fetchProjects = async ({ pageParam }) => {
  const res = await fetch('/api/projects?cursor=' + pageParam)
  return res.json()
}

const {
  data,
  error,
  fetchNextPage,
  hasNextPage,
  isFetching,
  isFetchingNextPage,
  isPending,
  isError,
} = useInfiniteQuery({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  initialPageParam: 0,
  getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
})
</script>

<template>
  <span v-if="isPending">Loading...</span>
  <span v-else-if="isError">Error: {{ error.message }}</span>
  <div v-else-if="data">
    <span v-if="isFetching && !isFetchingNextPage">Fetching...</span>
    <ul v-for="(group, index) in data.pages" :key="index">
      <li v-for="project in group.projects" :key="project.id">
        {{ project.name }}
      </li>
    </ul>
    <button
      @click="() => fetchNextPage()"
      :disabled="!hasNextPage || isFetchingNextPage"
    >
      <span v-if="isFetchingNextPage">Loading more...</span>
      <span v-else-if="hasNextPage">Load More</span>
      <span v-else>Nothing more to load</span>
    </button>
  </div>
</template>
```

[//]: # 'Example'
