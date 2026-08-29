---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/UseQueryResult.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.377884Z"
---
# Usequeryresult

---
id: UseQueryResult
title: UseQueryResult
---

```ts
type UseQueryResult<TData, TError> = UseBaseQueryResult<TData, TError>;
```

Defined in: [preact-query/src/types.ts:324](https://github.com/TanStack/query/blob/main/packages/preact-query/src/types.ts#L324)

The result of `useQuery`. Same as [UseBaseQueryResult](UseBaseQueryResult.md).

## Type Parameters

### TData

`TData` = `unknown`

The type `data` ends up as after `select` runs.

### TError

`TError` = `DefaultError`

The type of errors your `queryFn` may throw.
