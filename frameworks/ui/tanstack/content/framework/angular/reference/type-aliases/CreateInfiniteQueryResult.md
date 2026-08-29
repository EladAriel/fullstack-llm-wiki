---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/CreateInfiniteQueryResult.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.426485Z"
---
# Createinfinitequeryresult

---
id: CreateInfiniteQueryResult
title: CreateInfiniteQueryResult
---

```ts
type CreateInfiniteQueryResult<TData, TError> = BaseQueryNarrowing<TData, TError> & MapToSignals<InfiniteQueryObserverResult<TData, TError>>;
```

Defined in: [types.ts:111](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L111)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`
