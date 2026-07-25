---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/mutationOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
