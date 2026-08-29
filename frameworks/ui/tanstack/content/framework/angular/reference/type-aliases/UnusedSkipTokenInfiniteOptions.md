---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/UnusedSkipTokenInfiniteOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.426656Z"
---
# Unusedskiptokeninfiniteoptions

---
id: UnusedSkipTokenInfiniteOptions
title: UnusedSkipTokenInfiniteOptions
---

```ts
type UnusedSkipTokenInfiniteOptions<TQueryFnData, TError, TData, TQueryKey, TPageParam> = OmitKeyof<CreateInfiniteQueryOptions<TQueryFnData, TError, TData, TQueryKey, TPageParam>, "queryFn"> & object;
```

Defined in: [infinite-query-options.ts:34](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/infinite-query-options.ts#L34)

## Type Declaration

### queryFn?

```ts
optional queryFn: Exclude<CreateInfiniteQueryOptions<TQueryFnData, TError, TData, TQueryKey, TPageParam>["queryFn"], SkipToken | undefined>;
```

## Type Parameters

### TQueryFnData

`TQueryFnData`

### TError

`TError` = `DefaultError`

### TData

`TData` = `InfiniteData`\<`TQueryFnData`\>

### TQueryKey

`TQueryKey` *extends* `QueryKey` = `QueryKey`

### TPageParam

`TPageParam` = `unknown`
