---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/UnusedSkipTokenOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: UnusedSkipTokenOptions
title: UnusedSkipTokenOptions
---

# Type Alias: UnusedSkipTokenOptions\<TQueryFnData, TError, TData, TQueryKey\>

```ts
type UnusedSkipTokenOptions<TQueryFnData, TError, TData, TQueryKey> = OmitKeyof<QueryObserverOptions<TQueryFnData, TError, TData, TQueryFnData, TQueryKey>, "queryFn"> & object;
```

Defined in: [packages/lit-query/src/queryOptions.ts:34](https://github.com/TanStack/query/blob/main/packages/lit-query/src/queryOptions.ts#L34)

Query options where `queryFn` is present and not a `skipToken`.

## Type Declaration

### queryFn?

```ts
optional queryFn: Exclude<QueryObserverOptions<TQueryFnData, TError, TData, TQueryFnData, TQueryKey>["queryFn"], SkipToken | undefined>;
```

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

### TError

`TError` = `DefaultError`

### TData

`TData` = `TQueryFnData`

### TQueryKey

`TQueryKey` *extends* `QueryKey` = `QueryKey`
