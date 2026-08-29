---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/DefinedUseQueryResult.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.380516Z"
---
# Definedusequeryresult

---
id: DefinedUseQueryResult
title: DefinedUseQueryResult
---

```ts
type DefinedUseQueryResult<TData, TError> = DefinedQueryObserverResult<TData, TError>;
```

Defined in: [preact-query/src/types.ts:352](https://github.com/TanStack/query/blob/main/packages/preact-query/src/types.ts#L352)

The result of `useQuery` when `initialData` is set, or of `useSuspenseQuery` before the `isPlaceholderData`
omission — `data` is never `undefined`. Re-exports DefinedQueryObserverResult from
`@tanstack/query-core`.

## Type Parameters

### TData

`TData` = `unknown`

The type `data` ends up as after `select` runs.

### TError

`TError` = `DefaultError`

The type of errors your `queryFn` may throw.
