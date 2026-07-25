---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/UnusedSkipTokenOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
