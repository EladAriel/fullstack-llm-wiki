---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationResultAccessor.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.387624Z"
---
# Mutationresultaccessor

---
id: MutationResultAccessor
title: MutationResultAccessor
---

```ts
type MutationResultAccessor<TData, TError, TVariables, TOnMutateResult> = ValueAccessor<MutationObserverResult<TData, TError, TVariables, TOnMutateResult>> & object;
```

Defined in: [packages/lit-query/src/createMutationController.ts:38](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createMutationController.ts#L38)

Accessor returned by `createMutationController`.

Call the accessor or read its `current` property to get the latest mutation
result. The attached methods delegate to the active mutation observer.

## Type Declaration

### destroy()

```ts
destroy: () => void;
```

Removes the controller from its Lit host and unsubscribes observers.

#### Returns

`void`

### mutate()

```ts
mutate: (...args) => void;
```

Starts the mutation and swallows the returned promise.

Throws synchronously if no `QueryClient` can be resolved.

#### Parameters

##### args

...`Parameters`\<`MutateFunction`\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>\>

#### Returns

`void`

### mutateAsync

```ts
mutateAsync: MutationObserverResult<TData, TError, TVariables, TOnMutateResult>["mutate"];
```

Starts the mutation and returns the observer promise.

Rejects if no `QueryClient` can be resolved.

### reset

```ts
reset: MutationObserverResult<TData, TError, TVariables, TOnMutateResult>["reset"];
```

Resets the mutation observer to its idle state.

## Type Parameters

### TData

`TData`

### TError

`TError`

### TVariables

`TVariables`

### TOnMutateResult

`TOnMutateResult`
