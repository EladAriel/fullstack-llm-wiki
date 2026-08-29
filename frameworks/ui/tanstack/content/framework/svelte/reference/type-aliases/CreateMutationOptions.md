---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/type-aliases/CreateMutationOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.404585Z"
---
# Createmutationoptions

---
id: CreateMutationOptions
title: CreateMutationOptions
---

```ts
type CreateMutationOptions<TData, TError, TVariables, TOnMutateResult> = OmitKeyof<MutationObserverOptions<TData, TError, TVariables, TOnMutateResult>, "_defaulted">;
```

Defined in: [packages/svelte-query/src/types.ts:86](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L86)

Options for createMutation

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`

### TVariables

`TVariables` = `void`

### TOnMutateResult

`TOnMutateResult` = `unknown`
