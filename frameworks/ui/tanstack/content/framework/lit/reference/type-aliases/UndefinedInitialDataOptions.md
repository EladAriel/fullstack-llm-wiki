---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/UndefinedInitialDataOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: UndefinedInitialDataOptions
title: UndefinedInitialDataOptions
---

# Type Alias: UndefinedInitialDataOptions\<TQueryFnData, TError, TData, TQueryKey\>

```ts
type UndefinedInitialDataOptions<TQueryFnData, TError, TData, TQueryKey> = QueryObserverOptions<TQueryFnData, TError, TData, TQueryFnData, TQueryKey> & object;
```

Defined in: [packages/lit-query/src/queryOptions.ts:58](https://github.com/TanStack/query/blob/main/packages/lit-query/src/queryOptions.ts#L58)

Query options where `initialData` can be omitted or undefined.

## Type Declaration

### initialData?

```ts
optional initialData:
  | InitialDataFunction<NonUndefinedGuard<TQueryFnData>>
| NonUndefinedGuard<TQueryFnData>;
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
