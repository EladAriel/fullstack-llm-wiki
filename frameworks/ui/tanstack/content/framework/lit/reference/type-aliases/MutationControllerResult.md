---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationControllerResult.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: MutationControllerResult
title: MutationControllerResult
---

# Type Alias: MutationControllerResult\<TData, TError, TVariables, TOnMutateResult\>

```ts
type MutationControllerResult<TData, TError, TVariables, TOnMutateResult> = MutationObserverResult<TData, TError, TVariables, TOnMutateResult>;
```

Defined in: [packages/lit-query/src/types.ts:64](https://github.com/TanStack/query/blob/main/packages/lit-query/src/types.ts#L64)

Result object produced by a Lit mutation controller.

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`

### TVariables

`TVariables` = `void`

### TOnMutateResult

`TOnMutateResult` = `unknown`
