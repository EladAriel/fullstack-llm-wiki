---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/interfaces/UseBaseQueryOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: UseBaseQueryOptions
title: UseBaseQueryOptions
---

# Interface: UseBaseQueryOptions\<TQueryFnData, TError, TData, TQueryData, TQueryKey\>

Defined in: [preact-query/src/types.ts:29](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/types.ts#L29)

## Extends

- `QueryObserverOptions`\<`TQueryFnData`, `TError`, `TData`, `TQueryData`, `TQueryKey`\>

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

## Properties

### subscribed?

```ts
optional subscribed: boolean;
```

Defined in: [preact-query/src/types.ts:46](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/types.ts#L46)

Set this to `false` to unsubscribe this observer from updates to the query cache.
Defaults to `true`.
