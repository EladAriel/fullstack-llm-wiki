---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/DefinedCreateInfiniteQueryResult.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: DefinedCreateInfiniteQueryResult
title: DefinedCreateInfiniteQueryResult
---

# Type Alias: DefinedCreateInfiniteQueryResult\<TData, TError, TDefinedInfiniteQueryObserver\>

```ts
type DefinedCreateInfiniteQueryResult<TData, TError, TDefinedInfiniteQueryObserver> = MapToSignals<TDefinedInfiniteQueryObserver>;
```

Defined in: [types.ts:123](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L123)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`

### TDefinedInfiniteQueryObserver

`TDefinedInfiniteQueryObserver` = `DefinedInfiniteQueryObserverResult`\<`TData`, `TError`\>
