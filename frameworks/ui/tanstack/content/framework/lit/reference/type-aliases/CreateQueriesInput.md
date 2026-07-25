---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/CreateQueriesInput.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: CreateQueriesInput
title: CreateQueriesInput
---

# Type Alias: CreateQueriesInput\<TQueryFnData, TError, TData, TQueryKey\>

```ts
type CreateQueriesInput<TQueryFnData, TError, TData, TQueryKey> = QueryObserverOptions<TQueryFnData, TError, TData, TQueryFnData, TQueryKey>;
```

Defined in: [packages/lit-query/src/createQueriesController.ts:30](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L30)

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
