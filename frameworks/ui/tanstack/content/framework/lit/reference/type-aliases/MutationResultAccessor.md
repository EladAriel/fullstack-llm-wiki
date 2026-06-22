---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationResultAccessor.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: MutationResultAccessor
title: MutationResultAccessor
---

# Type Alias: MutationResultAccessor\<TData, TError, TVariables, TOnMutateResult\>

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
mutate: (variables, options?) => void;
```

Starts the mutation and swallows the returned promise.

Throws synchronously if no `QueryClient` can be resolved.

#### Parameters

##### variables

`TVariables`

##### options?

`MutateOptions`\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>

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
