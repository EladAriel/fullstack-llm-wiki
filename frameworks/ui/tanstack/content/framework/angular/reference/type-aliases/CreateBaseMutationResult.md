---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/CreateBaseMutationResult.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.424623Z"
---
# Createbasemutationresult

---
id: CreateBaseMutationResult
title: CreateBaseMutationResult
---

```ts
type CreateBaseMutationResult<TData, TError, TVariables, TOnMutateResult> = Override<MutationObserverResult<TData, TError, TVariables, TOnMutateResult>, {
  mutate: CreateMutateFunction<TData, TError, TVariables, TOnMutateResult>;
}> & object;
```

Defined in: [types.ts:154](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L154)

## Type Declaration

### mutateAsync

```ts
mutateAsync: CreateMutateAsyncFunction<TData, TError, TVariables, TOnMutateResult>;
```

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`

### TVariables

`TVariables` = `unknown`

### TOnMutateResult

`TOnMutateResult` = `unknown`
