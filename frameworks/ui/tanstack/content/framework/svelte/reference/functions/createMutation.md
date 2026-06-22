---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/functions/createMutation.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: createMutation
title: createMutation
---

# Function: createMutation()

```ts
function createMutation<TData, TError, TVariables, TContext>(options, queryClient?): CreateMutationResult<TData, TError, TVariables, TContext>;
```

Defined in: [packages/svelte-query/src/createMutation.svelte.ts:17](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/createMutation.svelte.ts#L17)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `Error`

### TVariables

`TVariables` = `void`

### TContext

`TContext` = `unknown`

## Parameters

### options

[`Accessor`](../type-aliases/Accessor.md)\<[`CreateMutationOptions`](../type-aliases/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TContext`\>\>

A function that returns mutation options

### queryClient?

[`Accessor`](../type-aliases/Accessor.md)\<`QueryClient`\>

Custom query client which overrides provider

## Returns

[`CreateMutationResult`](../type-aliases/CreateMutationResult.md)\<`TData`, `TError`, `TVariables`, `TContext`\>
