---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/mutationOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.384725Z"
---
# Mutationoptions

---
id: mutationOptions
title: mutationOptions
---

```ts
function mutationOptions<TData, TError, TVariables, TOnMutateResult>(options): MutationObserverOptions<TData, TError, TVariables, TOnMutateResult>;
```

Defined in: [packages/lit-query/src/mutationOptions.ts:22](https://github.com/TanStack/query/blob/main/packages/lit-query/src/mutationOptions.ts#L22)

Preserves and types mutation options for reuse across Lit Query APIs.

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

### options

`MutationObserverOptions`\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>

Mutation options to preserve.

## Returns

`MutationObserverOptions`\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>

The same options object.

## Example

```ts
import { mutationOptions } from '@tanstack/lit-query'

const addTodoOptions = mutationOptions({
  mutationKey: ['add-todo'],
  mutationFn: (title: string) => addTodo(title),
})
```
