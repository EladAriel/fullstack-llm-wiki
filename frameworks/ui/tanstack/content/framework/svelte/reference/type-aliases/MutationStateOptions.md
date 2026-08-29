---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/type-aliases/MutationStateOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.403695Z"
---
# Mutationstateoptions

---
id: MutationStateOptions
title: MutationStateOptions
---

```ts
type MutationStateOptions<TResult, TMutation> = object;
```

Defined in: [packages/svelte-query/src/types.ts:151](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L151)

Options for useMutationState

## Type Parameters

### TResult

`TResult` = `MutationState`

### TMutation

`TMutation` *extends* `Mutation`\<`any`, `any`, `any`, `any`\> = [`MutationTypeFromResult`](MutationTypeFromResult.md)\<`TResult`\>

## Properties

### filters?

```ts
optional filters: MutationFilters;
```

Defined in: [packages/svelte-query/src/types.ts:156](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L156)

***

### select()?

```ts
optional select: (mutation) => TResult;
```

Defined in: [packages/svelte-query/src/types.ts:157](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L157)

#### Parameters

##### mutation

`TMutation`

#### Returns

`TResult`
