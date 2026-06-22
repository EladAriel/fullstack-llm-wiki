---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/vue/guides/query-retries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: query-retries
title: Query Retries
ref: docs/framework/react/guides/query-retries.md
replace: { 'Provider': 'Plugin' }
---

[//]: # 'Example'

```tsx
import { useQuery } from '@tanstack/vue-query'

// Make a specific query retry a certain number of times
const result = useQuery({
  queryKey: ['todos', 1],
  queryFn: fetchTodoListPage,
  retry: 10, // Will retry failed requests 10 times before displaying an error
})
```

[//]: # 'Example'
[//]: # 'Example2'

```ts
import { VueQueryPlugin } from '@tanstack/vue-query'

const vueQueryPluginOptions = {
  queryClientConfig: {
    defaultOptions: {
      queries: {
        retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),
      },
    },
  },
}
app.use(VueQueryPlugin, vueQueryPluginOptions)
```

[//]: # 'Example2'
