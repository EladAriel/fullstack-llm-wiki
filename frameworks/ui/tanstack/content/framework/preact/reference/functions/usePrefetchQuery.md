---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/usePrefetchQuery.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
