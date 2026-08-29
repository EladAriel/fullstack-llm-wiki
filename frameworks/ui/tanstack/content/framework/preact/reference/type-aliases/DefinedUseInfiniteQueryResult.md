---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/DefinedUseInfiniteQueryResult.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.377571Z"
---
# Defineduseinfinitequeryresult

---
id: DefinedUseInfiniteQueryResult
title: DefinedUseInfiniteQueryResult
---

```ts
type DefinedUseInfiniteQueryResult<TData, TError> = DefinedInfiniteQueryObserverResult<TData, TError>;
```

Defined in: [preact-query/src/types.ts:376](https://github.com/TanStack/query/blob/main/packages/preact-query/src/types.ts#L376)

The result of `useInfiniteQuery` when `initialData` is set — `data` is never `undefined`. Re-exports
DefinedInfiniteQueryObserverResult from `@tanstack/query-core`.

## Type Parameters

### TData

`TData` = `unknown`

The type `data` ends up as after `select` runs.

### TError

`TError` = `DefaultError`

The type of errors your `queryFn` may throw.
