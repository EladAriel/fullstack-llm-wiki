---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/CreateMutationOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: CreateMutationOptions
title: CreateMutationOptions
---

# Type Alias: CreateMutationOptions\<TData, TError, TVariables, TOnMutateResult\>

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
