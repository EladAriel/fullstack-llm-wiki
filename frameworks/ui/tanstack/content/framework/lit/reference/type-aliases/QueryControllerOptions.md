---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/QueryControllerOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: QueryControllerOptions
title: QueryControllerOptions
---

# Type Alias: QueryControllerOptions\<TQueryFnData, TError, TData, TQueryData, TQueryKey\>

```ts
type QueryControllerOptions<TQueryFnData, TError, TData, TQueryData, TQueryKey> = Accessor<CreateQueryOptions<TQueryFnData, TError, TData, TQueryData, TQueryKey>>;
```

Defined in: [packages/lit-query/src/types.ts:20](https://github.com/TanStack/query/blob/main/packages/lit-query/src/types.ts#L20)

Accessor-wrapped options accepted by `createQueryController`.

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

### TError

`TError` = `DefaultError`

### TData

`TData` = `TQueryFnData`

### TQueryData

`TQueryData` = `TQueryFnData`

### TQueryKey

`TQueryKey` *extends* `QueryKey` = `QueryKey`
