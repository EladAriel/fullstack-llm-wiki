---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationStateOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
