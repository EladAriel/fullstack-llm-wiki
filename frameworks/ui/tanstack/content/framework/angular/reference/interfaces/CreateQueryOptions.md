---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/interfaces/CreateQueryOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: CreateQueryOptions
title: CreateQueryOptions
---

# Interface: CreateQueryOptions\<TQueryFnData, TError, TData, TQueryKey\>

Defined in: [types.ts:35](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L35)

## Extends

- `OmitKeyof`\<[`CreateBaseQueryOptions`](CreateBaseQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryFnData`, `TQueryKey`\>, `"suspense"`\>

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

### TError

`TError` = `DefaultError`

### TData

`TData` = `TQueryFnData`

### TQueryKey

`TQueryKey` *extends* `QueryKey` = `QueryKey`
