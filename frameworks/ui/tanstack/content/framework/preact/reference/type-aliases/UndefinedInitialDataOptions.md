---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/UndefinedInitialDataOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.379283Z"
---
# Undefinedinitialdataoptions

---
id: UndefinedInitialDataOptions
title: UndefinedInitialDataOptions
---

```ts
type UndefinedInitialDataOptions<TQueryFnData, TError, TData, TQueryKey> = UseQueryOptions<TQueryFnData, TError, TData, TQueryKey> & object;
```

Defined in: [preact-query/src/queryOptions.ts:23](https://github.com/TanStack/query/blob/main/packages/preact-query/src/queryOptions.ts#L23)

The options accepted by the `queryOptions` overload selected when no `initialData` is set — `data` may be
`undefined` while the query is `pending`.

## Type Declaration

### initialData?

```ts
optional initialData: 
  | InitialDataFunction<NonUndefinedGuard<TQueryFnData>>
| NonUndefinedGuard<TQueryFnData>;
```

If set, this value will be used as the initial data for the query cache (as long as the query hasn't been
created or cached yet). If set to a function, the function will be called **once** during the shared/root
query initialization, and be expected to synchronously return the initial data. Initial data is
considered stale by default unless a `staleTime` has been set. `initialData` **is persisted** to the
cache.

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
