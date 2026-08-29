---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/CreateQueriesInput.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.389600Z"
---
# Createqueriesinput

---
id: CreateQueriesInput
title: CreateQueriesInput
---

```ts
type CreateQueriesInput<TQueryFnData, TError, TData, TQueryKey> = QueryObserverOptions<TQueryFnData, TError, TData, TQueryFnData, TQueryKey>;
```

Defined in: [packages/lit-query/src/createQueriesController.ts:31](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L31)

Options for one query inside `createQueriesController`.

This mirrors `QueryObserverOptions` and is used by the tuple inference that
maps each input query to its corresponding result.

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

### TError

`TError` = `DefaultError`

### TData

`TData` = `TQueryFnData`

### TQueryKey

`TQueryKey` *extends* `QueryKey` = `QueryKey`
