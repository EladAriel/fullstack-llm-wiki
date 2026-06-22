---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/MutationStateAccessor.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
