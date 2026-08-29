---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/functions/createMutation.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.399963Z"
---
# Createmutation

---
id: createMutation
title: createMutation
---

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
