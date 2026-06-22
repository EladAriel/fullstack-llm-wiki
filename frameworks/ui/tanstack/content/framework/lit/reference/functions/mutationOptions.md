---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/mutationOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: mutationOptions
title: mutationOptions
---

# Function: mutationOptions()

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
