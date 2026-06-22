---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/QueryControllerOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
