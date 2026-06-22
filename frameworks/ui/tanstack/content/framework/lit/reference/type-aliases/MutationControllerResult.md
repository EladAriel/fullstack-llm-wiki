---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationControllerResult.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
