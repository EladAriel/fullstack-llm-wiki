---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/interfaces/QueryErrorResetBoundaryProps.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.382719Z"
---
# Queryerrorresetboundaryprops

---
id: QueryErrorResetBoundaryProps
title: QueryErrorResetBoundaryProps
---

Defined in: [preact-query/src/QueryErrorResetBoundary.tsx:103](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryErrorResetBoundary.tsx#L103)

The props accepted by `QueryErrorResetBoundary`.

## Properties

### children

```ts
children: 
  | ComponentChildren
  | QueryErrorResetBoundaryFunction;
```

Defined in: [preact-query/src/QueryErrorResetBoundary.tsx:108](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryErrorResetBoundary.tsx#L108)

Either a plain node, or a function that receives the boundary's QueryErrorResetBoundaryValue and
returns a node.
