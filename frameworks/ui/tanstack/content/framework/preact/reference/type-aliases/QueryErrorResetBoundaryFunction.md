---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/QueryErrorResetBoundaryFunction.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.377722Z"
---
# Queryerrorresetboundaryfunction

---
id: QueryErrorResetBoundaryFunction
title: QueryErrorResetBoundaryFunction
---

```ts
type QueryErrorResetBoundaryFunction = (value) => ComponentChildren;
```

Defined in: [preact-query/src/QueryErrorResetBoundary.tsx:96](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryErrorResetBoundary.tsx#L96)

A render-prop function usable as `children` on `QueryErrorResetBoundary`.

## Parameters

### value

`QueryErrorResetBoundaryValue`

The boundary's QueryErrorResetBoundaryValue.

## Returns

`ComponentChildren`

The children to render.
