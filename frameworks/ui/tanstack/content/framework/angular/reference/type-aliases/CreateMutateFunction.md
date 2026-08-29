---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/CreateMutateFunction.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.424305Z"
---
# Createmutatefunction

---
id: CreateMutateFunction
title: CreateMutateFunction
---

```ts
type CreateMutateFunction<TData, TError, TVariables, TOnMutateResult> = (...args) => void;
```

Defined in: [types.ts:136](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L136)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`

### TVariables

`TVariables` = `void`

### TOnMutateResult

`TOnMutateResult` = `unknown`

## Parameters

### args

...`Parameters`\<`MutateFunction`\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>\>

## Returns

`void`
