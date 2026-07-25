---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/CreateInfiniteQueryResult.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: CreateInfiniteQueryResult
title: CreateInfiniteQueryResult
---

# Type Alias: CreateInfiniteQueryResult\<TData, TError\>

```ts
type CreateInfiniteQueryResult<TData, TError> = BaseQueryNarrowing<TData, TError> & MapToSignals<InfiniteQueryObserverResult<TData, TError>>;
```

Defined in: [types.ts:117](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L117)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`
