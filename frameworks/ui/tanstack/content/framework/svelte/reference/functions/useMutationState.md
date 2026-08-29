---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/functions/useMutationState.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.400888Z"
---
# Usemutationstate

---
id: useMutationState
title: useMutationState
---

```ts
function useMutationState<TResult, TMutation>(options, queryClient?): TResult[];
```

Defined in: [packages/svelte-query/src/useMutationState.svelte.ts:29](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/useMutationState.svelte.ts#L29)

## Type Parameters

### TResult

`TResult` = `MutationState`\<`unknown`, `Error`, `unknown`, `unknown`\>

### TMutation

`TMutation` *extends* `Mutation`\<`any`, `any`, `any`, `any`\> = [`MutationTypeFromResult`](../type-aliases/MutationTypeFromResult.md)\<`TResult`\>

## Parameters

### options

[`MutationStateOptions`](../type-aliases/MutationStateOptions.md)\<`TResult`, `TMutation`\> = `{}`

### queryClient?

`QueryClient`

## Returns

`TResult`[]
