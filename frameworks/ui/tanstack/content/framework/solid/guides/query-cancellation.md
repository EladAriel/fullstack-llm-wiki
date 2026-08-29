---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/query-cancellation.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.393111Z"
---
# Query Cancellation

---
id: query-cancellation
title: Query Cancellation
ref: docs/framework/react/guides/query-cancellation.md
replace:
  {
    '@tanstack/react-query': '@tanstack/solid-query',
    'useMutationState[(]': 'useMutationState(() => ',
    'useMutation[(]': 'useMutation(() => ',
    'useQuery[(]': 'useQuery(() => ',
    'useQueries[(]': 'useQueries(() => ',
    'useInfiniteQuery[(]': 'useInfiniteQuery(() => ',
  }
---

[//]: # 'Example'

```tsx
const todosQuery = useQuery(() => ({
  queryKey: ['todos'],
  queryFn: async ({ signal }) => {
    const todosResponse = await fetch('/todos', {
      // Pass the signal to one fetch
      signal,
    })
    const todos = await todosResponse.json()

    const todoDetails = todos.map(async ({ details }) => {
      const response = await fetch(details, {
        // Or pass it to several
        signal,
      })
      return response.json()
    })

    return Promise.all(todoDetails)
  },
}))
```

[//]: # 'Example'
[//]: # 'Example2'

```tsx
import axios from 'axios'

const todosQuery = useQuery(() => ({
  queryKey: ['todos'],
  queryFn: ({ signal }) =>
    axios.get('/todos', {
      // Pass the signal to `axios`
      signal,
    }),
}))
```

[//]: # 'Example2'
[//]: # 'Example3'

```tsx
import axios from 'axios'

const todosQuery = useQuery(() => ({
  queryKey: ['todos'],
  queryFn: ({ signal }) => {
    // Create a new CancelToken source for this request
    const CancelToken = axios.CancelToken
    const source = CancelToken.source()

    const promise = axios.get('/todos', {
      // Pass the source token to your request
      cancelToken: source.token,
    })

    // Cancel the request if TanStack Query signals to abort
    signal?.addEventListener('abort', () => {
      source.cancel('Query was cancelled by TanStack Query')
    })

    return promise
  },
}))
```

[//]: # 'Example3'
[//]: # 'Example4'

```tsx
const todosQuery = useQuery(() => ({
  queryKey: ['todos'],
  queryFn: ({ signal }) => {
    return new Promise((resolve, reject) => {
      var oReq = new XMLHttpRequest()
      oReq.addEventListener('load', () => {
        resolve(JSON.parse(oReq.responseText))
      })
      signal?.addEventListener('abort', () => {
        oReq.abort()
        reject()
      })
      oReq.open('GET', '/todos')
      oReq.send()
    })
  },
}))
```

[//]: # 'Example4'
[//]: # 'Example5'

```tsx
const client = new GraphQLClient(endpoint)

const todosQuery = useQuery(() => ({
  queryKey: ['todos'],
  queryFn: ({ signal }) => {
    client.request({ document: query, signal })
  },
}))
```

[//]: # 'Example5'
[//]: # 'Example6'

```tsx
const todosQuery = useQuery(() => ({
  queryKey: ['todos'],
  queryFn: ({ signal }) => {
    const client = new GraphQLClient(endpoint, {
      signal,
    })
    return client.request(query, variables)
  },
}))
```

[//]: # 'Example6'
[//]: # 'Example7'

```tsx
const todosQuery = useQuery(() => ({
  queryKey: ['todos'],
  queryFn: async ({ signal }) => {
    const resp = await fetch('/todos', { signal })
    return resp.json()
  },
}))

const queryClient = useQueryClient()

return (
  <button
    onClick={(e) => {
      e.preventDefault()
      queryClient.cancelQueries({ queryKey: ['todos'] })
    }}
  >
    Cancel
  </button>
)
```

[//]: # 'Example7'
[//]: # 'Limitations'
[//]: # 'Limitations'
