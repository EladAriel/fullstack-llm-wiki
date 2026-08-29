---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/QueryControllerOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.391060Z"
---
# Querycontrolleroptions

---
id: QueryControllerOptions
title: QueryControllerOptions
---

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
