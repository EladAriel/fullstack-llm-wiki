---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectMutation.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: injectMutation
title: injectMutation
---

# Function: injectMutation()

```ts
function injectMutation<TData, TError, TVariables, TOnMutateResult>(injectMutationFn, options?): CreateMutationResult<TData, TError, TVariables, TOnMutateResult>;
```

Defined in: [inject-mutation.ts:45](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-mutation.ts#L45)

Injects a mutation: an imperative function that can be invoked which typically performs server side effects.

Unlike queries, mutations are not run automatically.

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `Error`

### TVariables

`TVariables` = `void`

### TOnMutateResult

`TOnMutateResult` = `unknown`

## Parameters

### injectMutationFn

() => [`CreateMutationOptions`](../interfaces/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>

A function that returns mutation options.

### options?

[`InjectMutationOptions`](../interfaces/InjectMutationOptions.md)

Additional configuration

## Returns

[`CreateMutationResult`](../type-aliases/CreateMutationResult.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>

The mutation.
