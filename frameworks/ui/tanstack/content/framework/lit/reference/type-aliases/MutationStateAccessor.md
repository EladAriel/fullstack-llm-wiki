---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationStateAccessor.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: MutationStateAccessor
title: MutationStateAccessor
---

# Type Alias: MutationStateAccessor\<TResult\>

```ts
type MutationStateAccessor<TResult> = ValueAccessor<TResult[]> & object;
```

Defined in: [packages/lit-query/src/useMutationState.ts:32](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L32)

Accessor returned by `useMutationState`.

Call the accessor or read its `current` property to get the selected state for
matching mutations.

## Type Declaration

### destroy()

```ts
destroy: () => void;
```

Removes the controller from its Lit host and unsubscribes observers.

#### Returns

`void`

## Type Parameters

### TResult

`TResult`
