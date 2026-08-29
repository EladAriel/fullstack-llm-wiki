---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/query-retries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.420979Z"
---
# Query Retries

---
id: query-retries
title: Query Retries
ref: docs/framework/react/guides/query-retries.md
replace:
  {
    'Provider': 'Plugin',
    'useQuery': 'injectQuery',
    'useMutation': 'injectMutation',
  }
---

[//]: # 'Info'
[//]: # 'Info'
[//]: # 'Example'

```ts
import { injectQuery } from '@tanstack/angular-query-experimental'

// Make a specific query retry a certain number of times
const result = injectQuery(() => ({
  queryKey: ['todos', 1],
  queryFn: fetchTodoListPage,
  retry: 10, // Will retry failed requests 10 times before displaying an error
}))
```

[//]: # 'Example'
[//]: # 'Example2'

```ts
// Configure for all queries
import {
  QueryCache,
  QueryClient,
  provideTanStackQuery,
} from '@tanstack/angular-query-experimental'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),
    },
  },
})

bootstrapApplication(AppComponent, {
  providers: [provideTanStackQuery(queryClient)],
})
```

[//]: # 'Example2'

Though it is not recommended, you can obviously override the `retryDelay` function/integer in both the Provider and individual query options. If set to an integer instead of a function the delay will always be the same amount of time:

[//]: # 'Example3'

```ts
const result = injectQuery(() => ({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
  retryDelay: 1000, // Will always wait 1000ms to retry, regardless of how many retries
}))
```

[//]: # 'Example3'
