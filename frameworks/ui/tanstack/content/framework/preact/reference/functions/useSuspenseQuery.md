---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useSuspenseQuery.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useSuspenseQuery
title: useSuspenseQuery
---

# Function: useSuspenseQuery()

```ts
function useSuspenseQuery<TQueryFnData, TError, TData, TQueryKey>(options, queryClient?): UseSuspenseQueryResult<TData, TError>;
```

Defined in: [preact-query/src/useSuspenseQuery.ts:7](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useSuspenseQuery.ts#L7)

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

[`UseSuspenseQueryOptions`](../interfaces/UseSuspenseQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>

### queryClient?

`QueryClient`

## Returns

[`UseSuspenseQueryResult`](../type-aliases/UseSuspenseQueryResult.md)\<`TData`, `TError`\>
