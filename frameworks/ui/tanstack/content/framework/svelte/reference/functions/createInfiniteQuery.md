---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/functions/createInfiniteQuery.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.401184Z"
---
# Createinfinitequery

---
id: createInfiniteQuery
title: createInfiniteQuery
---

```ts
function createInfiniteQuery<TQueryFnData, TError, TData, TQueryKey, TPageParam>(options, queryClient?): CreateInfiniteQueryResult<TData, TError>;
```

Defined in: [packages/svelte-query/src/createInfiniteQuery.ts:16](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/createInfiniteQuery.ts#L16)

## Type Parameters

### TQueryFnData

`TQueryFnData`

### TError

`TError` = `Error`

### TData

`TData` = `InfiniteData`\<`TQueryFnData`, `unknown`\>

### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

### TPageParam

`TPageParam` = `unknown`

## Parameters

### options

[`Accessor`](../type-aliases/Accessor.md)\<[`CreateInfiniteQueryOptions`](../type-aliases/CreateInfiniteQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`, `TPageParam`\>\>

### queryClient?

[`Accessor`](../type-aliases/Accessor.md)\<`QueryClient`\>

## Returns

[`CreateInfiniteQueryResult`](../type-aliases/CreateInfiniteQueryResult.md)\<`TData`, `TError`\>
