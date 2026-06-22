---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/type-aliases/CreateInfiniteQueryOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: CreateInfiniteQueryOptions
title: CreateInfiniteQueryOptions
---

# Type Alias: CreateInfiniteQueryOptions\<TQueryFnData, TError, TData, TQueryKey, TPageParam\>

```ts
type CreateInfiniteQueryOptions<TQueryFnData, TError, TData, TQueryKey, TPageParam> = InfiniteQueryObserverOptions<TQueryFnData, TError, TData, TQueryKey, TPageParam>;
```

Defined in: [packages/svelte-query/src/types.ts:53](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L53)

Options for createInfiniteQuery

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

### TError

`TError` = `DefaultError`

### TData

`TData` = `TQueryFnData`

### TQueryKey

`TQueryKey` *extends* `QueryKey` = `QueryKey`

### TPageParam

`TPageParam` = `unknown`
