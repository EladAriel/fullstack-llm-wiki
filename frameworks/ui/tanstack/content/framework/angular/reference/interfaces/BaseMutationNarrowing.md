---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/interfaces/BaseMutationNarrowing.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.428596Z"
---
# Basemutationnarrowing

---
id: BaseMutationNarrowing
title: BaseMutationNarrowing
---

Defined in: [types.ts:184](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L184)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`

### TVariables

`TVariables` = `unknown`

### TOnMutateResult

`TOnMutateResult` = `unknown`

## Properties

### isError

```ts
isError: SignalFunction<(this) => this is CreateMutationResult<TData, TError, TVariables, TOnMutateResult, Override<MutationObserverErrorResult<TData, TError, TVariables, TOnMutateResult>, { mutate: CreateMutateFunction<TData, TError, TVariables, TOnMutateResult> }> & { mutateAsync: CreateMutateAsyncFunction<TData, TError, TVariables, TOnMutateResult> }>>;
```

Defined in: [types.ts:207](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L207)

***

### isIdle

```ts
isIdle: SignalFunction<(this) => this is CreateMutationResult<TData, TError, TVariables, TOnMutateResult, Override<MutationObserverIdleResult<TData, TError, TVariables, TOnMutateResult>, { mutate: CreateMutateFunction<TData, TError, TVariables, TOnMutateResult> }> & { mutateAsync: CreateMutateAsyncFunction<TData, TError, TVariables, TOnMutateResult> }>>;
```

Defined in: [types.ts:241](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L241)

***

### isPending

```ts
isPending: SignalFunction<(this) => this is CreateMutationResult<TData, TError, TVariables, TOnMutateResult, Override<MutationObserverLoadingResult<TData, TError, TVariables, TOnMutateResult>, { mutate: CreateMutateFunction<TData, TError, TVariables, TOnMutateResult> }> & { mutateAsync: CreateMutateAsyncFunction<TData, TError, TVariables, TOnMutateResult> }>>;
```

Defined in: [types.ts:224](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L224)

***

### isSuccess

```ts
isSuccess: SignalFunction<(this) => this is CreateMutationResult<TData, TError, TVariables, TOnMutateResult, Override<MutationObserverSuccessResult<TData, TError, TVariables, TOnMutateResult>, { mutate: CreateMutateFunction<TData, TError, TVariables, TOnMutateResult> }> & { mutateAsync: CreateMutateAsyncFunction<TData, TError, TVariables, TOnMutateResult> }>>;
```

Defined in: [types.ts:190](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L190)
