---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/type-aliases/CreateBaseMutationResult.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: CreateBaseMutationResult
title: CreateBaseMutationResult
---

# Type Alias: CreateBaseMutationResult\<TData, TError, TVariables, TOnMutateResult\>

```ts
type CreateBaseMutationResult<TData, TError, TVariables, TOnMutateResult> = Override<MutationObserverResult<TData, TError, TVariables, TOnMutateResult>, {
  mutate: CreateMutateFunction<TData, TError, TVariables, TOnMutateResult>;
}> & object;
```

Defined in: [packages/svelte-query/src/types.ts:114](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L114)

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
