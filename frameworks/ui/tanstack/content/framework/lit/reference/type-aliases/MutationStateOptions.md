---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationStateOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.389166Z"
---
# Mutationstateoptions

---
id: MutationStateOptions
title: MutationStateOptions
---

```ts
type MutationStateOptions<TResult> = object;
```

Defined in: [packages/lit-query/src/useMutationState.ts:20](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L20)

Options accepted by `useMutationState`.

## Type Parameters

### TResult

`TResult`

## Properties

### filters?

```ts
optional filters: Accessor<MutationFilters>;
```

Defined in: [packages/lit-query/src/useMutationState.ts:22](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L22)

Filters used to select mutations from the mutation cache.

***

### select()?

```ts
optional select: (mutation) => TResult;
```

Defined in: [packages/lit-query/src/useMutationState.ts:24](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L24)

Maps each matching mutation to the value returned by the accessor.

#### Parameters

##### mutation

`Mutation`

#### Returns

`TResult`
