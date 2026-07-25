---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/type-aliases/MutationStateOptions.md"
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

Defined in: [packages/svelte-query/src/types.ts:140](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L140)

Options for useMutationState

## Type Parameters

### TResult

`TResult` = `MutationState`

## Properties

### filters?

```ts
optional filters: MutationFilters;
```

Defined in: [packages/svelte-query/src/types.ts:141](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L141)

***

### select()?

```ts
optional select: (mutation) => TResult;
```

Defined in: [packages/svelte-query/src/types.ts:142](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/types.ts#L142)

#### Parameters

##### mutation

`Mutation`\<`unknown`, `DefaultError`, `unknown`, `unknown`\>

#### Returns

`TResult`
