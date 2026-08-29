---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/UnusedSkipTokenOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.377258Z"
---
# Unusedskiptokenoptions

---
id: UnusedSkipTokenOptions
title: UnusedSkipTokenOptions
---

```ts
type UnusedSkipTokenOptions<TQueryFnData, TError, TData, TQueryKey> = OmitKeyof<UseQueryOptions<TQueryFnData, TError, TData, TQueryKey>, "queryFn"> & object;
```

Defined in: [preact-query/src/queryOptions.ts:51](https://github.com/TanStack/query/blob/main/packages/preact-query/src/queryOptions.ts#L51)

The options accepted by the `queryOptions` overload selected when no `initialData` is set and `queryFn` is
not `skipToken` — same as [UndefinedInitialDataOptions](UndefinedInitialDataOptions.md), but `queryFn` may not be `skipToken`.

## Type Declaration

### queryFn?

```ts
optional queryFn: Exclude<UseQueryOptions<TQueryFnData, TError, TData, TQueryKey>["queryFn"], SkipToken | undefined>;
```

`skipToken` is not allowed as a value here — this overload is selected when no `initialData` is set. If
you don't intend to run the query yet, omit `queryFn` or use a default query function instead.

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

The type your `queryFn` resolves to.

### TError

`TError` = `DefaultError`

The type of errors your `queryFn` may throw.

### TData

`TData` = `TQueryFnData`

The type `data` ends up as after `select` runs.

### TQueryKey

`TQueryKey` *extends* `QueryKey` = `QueryKey`

The type of your `queryKey`.
