---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/InfiniteQueryControllerOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: InfiniteQueryControllerOptions
title: InfiniteQueryControllerOptions
---

# Type Alias: InfiniteQueryControllerOptions\<TQueryFnData, TError, TData, TQueryKey, TPageParam\>

```ts
type InfiniteQueryControllerOptions<TQueryFnData, TError, TData, TQueryKey, TPageParam> = Accessor<CreateInfiniteQueryOptions<TQueryFnData, TError, TData, TQueryKey, TPageParam>>;
```

Defined in: [packages/lit-query/src/types.ts:41](https://github.com/TanStack/query/blob/main/packages/lit-query/src/types.ts#L41)

Accessor-wrapped options accepted by `createInfiniteQueryController`.

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

### TError

`TError` = `DefaultError`

### TData

`TData` = `InfiniteData`\<`TQueryFnData`\>

### TQueryKey

`TQueryKey` *extends* `QueryKey` = `QueryKey`

### TPageParam

`TPageParam` = `unknown`
