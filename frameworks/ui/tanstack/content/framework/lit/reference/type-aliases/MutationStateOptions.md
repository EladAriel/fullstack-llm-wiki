---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationStateOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: MutationStateOptions
title: MutationStateOptions
---

# Type Alias: MutationStateOptions\<TResult\>

```ts
type MutationStateOptions<TResult> = object;
```

Defined in: [packages/lit-query/src/useMutationState.ts:19](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L19)

Options accepted by `useMutationState`.

## Type Parameters

### TResult

`TResult`

## Properties

### filters?

```ts
optional filters: Accessor<MutationFilters>;
```

Defined in: [packages/lit-query/src/useMutationState.ts:21](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L21)

Filters used to select mutations from the mutation cache.

***

### select()?

```ts
optional select: (mutation) => TResult;
```

Defined in: [packages/lit-query/src/useMutationState.ts:23](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L23)

Maps each matching mutation to the value returned by the accessor.

#### Parameters

##### mutation

`Mutation`

#### Returns

`TResult`
