---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/polling.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: polling
title: Polling
ref: docs/framework/react/guides/polling.md
replace: { '@tanstack/react-query': '@tanstack/solid-query' }
---

[//]: # 'Example1'

```tsx
useQuery(() => ({
  queryKey: ['prices'],
  queryFn: fetchPrices,
  refetchInterval: 5_000, // every 5 seconds
}))
```

[//]: # 'Example1'
[//]: # 'Example2'

```tsx
useQuery(() => ({
  queryKey: ['job', jobId],
  queryFn: () => fetchJobStatus(jobId),
  refetchInterval: (query) => {
    // Stop polling once the job finishes
    if (query.state.data?.status === 'complete') return false
    return 2_000
  },
}))
```

[//]: # 'Example2'
[//]: # 'Example3'

```tsx
useQuery(() => ({
  queryKey: ['portfolio'],
  queryFn: fetchPortfolio,
  refetchInterval: 30_000,
  refetchIntervalInBackground: true,
}))
```

[//]: # 'Example3'
[//]: # 'Example4'

```tsx
useQuery(() => ({
  queryKey: ['prices', tokenAddress],
  queryFn: () => fetchPrice(tokenAddress),
  refetchInterval: () => {
    if (!tokenAddress || isPaused) return false
    return 15_000
  },
}))
```

[//]: # 'Example4'
[//]: # 'Example5'

```tsx
useQuery(() => ({
  queryKey: ['chainStatus'],
  queryFn: fetchChainStatus,
  refetchInterval: 10_000,
  networkMode: 'always',
}))
```

[//]: # 'Example5'
[//]: # 'ReactNative'
[//]: # 'ReactNative'
