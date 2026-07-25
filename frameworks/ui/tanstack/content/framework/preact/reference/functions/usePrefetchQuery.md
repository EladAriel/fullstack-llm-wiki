---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/usePrefetchQuery.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: usePrefetchQuery
title: usePrefetchQuery
---

# Function: usePrefetchQuery()

```ts
function usePrefetchQuery<TQueryFnData, TError, TData, TQueryKey>(options, queryClient?): void;
```

Defined in: [preact-query/src/usePrefetchQuery.tsx:5](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/usePrefetchQuery.tsx#L5)

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

### TError

`TError` = `Error`

### TData

`TData` = `TQueryFnData`

### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

## Parameters

### options

[`UsePrefetchQueryOptions`](../interfaces/UsePrefetchQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>

### queryClient?

`QueryClient`

## Returns

`void`
