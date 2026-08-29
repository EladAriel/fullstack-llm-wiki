---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/CreateMutationOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.390407Z"
---
# Createmutationoptions

---
id: CreateMutationOptions
title: CreateMutationOptions
---

```ts
type CreateMutationOptions<TData, TError, TVariables, TOnMutateResult> = MutationObserverOptions<TData, TError, TVariables, TOnMutateResult>;
```

Defined in: [packages/lit-query/src/createMutationController.ts:25](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createMutationController.ts#L25)

Options accepted by `createMutationController`.

This is the Lit adapter shape for `MutationObserverOptions`. Pass it directly
or through an `Accessor` when the options depend on Lit host state.

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`

### TVariables

`TVariables` = `void`

### TOnMutateResult

`TOnMutateResult` = `unknown`
