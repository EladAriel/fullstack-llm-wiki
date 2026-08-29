---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/QueryErrorResetFunction.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.378646Z"
---
# Queryerrorresetfunction

---
id: QueryErrorResetFunction
title: QueryErrorResetFunction
---

```ts
type QueryErrorResetFunction = () => void;
```

Defined in: [preact-query/src/QueryErrorResetBoundary.tsx:10](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryErrorResetBoundary.tsx#L10)

Resets any query errors within the boundary, so queries know they can try again.

## Returns

`void`
