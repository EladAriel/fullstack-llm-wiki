---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationStateAccessor.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.390561Z"
---
# Mutationstateaccessor

---
id: MutationStateAccessor
title: MutationStateAccessor
---

```ts
type MutationStateAccessor<TResult> = ValueAccessor<TResult[]> & object;
```

Defined in: [packages/lit-query/src/useMutationState.ts:33](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L33)

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
