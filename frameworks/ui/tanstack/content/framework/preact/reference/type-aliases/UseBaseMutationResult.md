---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/UseBaseMutationResult.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.380363Z"
---
# Usebasemutationresult

---
id: UseBaseMutationResult
title: UseBaseMutationResult
---

```ts
type UseBaseMutationResult<TData, TError, TVariables, TOnMutateResult> = Override<MutationObserverResult<TData, TError, TVariables, TOnMutateResult>, {
  mutate: UseMutateFunction<TData, TError, TVariables, TOnMutateResult>;
}> & object;
```

Defined in: [preact-query/src/types.ts:470](https://github.com/TanStack/query/blob/main/packages/preact-query/src/types.ts#L470)

The result of `useMutation`. Same as MutationObserverResult from `@tanstack/query-core`, with
`mutate` narrowed to the fire-and-forget [UseMutateFunction](UseMutateFunction.md) signature, plus the added `mutateAsync`.

## Type Declaration

### mutateAsync

```ts
mutateAsync: UseMutateAsyncFunction<TData, TError, TVariables, TOnMutateResult>;
```

Similar to `mutate`, but returns a promise which can be awaited.

## Type Parameters

### TData

`TData` = `unknown`

The type your mutation function resolves to.

### TError

`TError` = `DefaultError`

The type of errors your mutation function may throw.

### TVariables

`TVariables` = `unknown`

The type of the variable passed to `mutate`/`mutateAsync`.

### TOnMutateResult

`TOnMutateResult` = `unknown`

The type returned by `onMutate`, passed to `onSuccess`/`onError`/`onSettled` as
their `onMutateResult` parameter — useful for optimistic-update rollback data.
