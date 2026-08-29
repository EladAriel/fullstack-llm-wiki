---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/IsMutatingAccessor.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.389012Z"
---
# Ismutatingaccessor

---
id: IsMutatingAccessor
title: IsMutatingAccessor
---

```ts
type IsMutatingAccessor = ValueAccessor<number> & object;
```

Defined in: [packages/lit-query/src/useIsMutating.ts:17](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useIsMutating.ts#L17)

Accessor returned by `useIsMutating`.

Call the accessor or read its `current` property to get the number of
currently pending mutations that match the filters.

## Type Declaration

### destroy()

```ts
destroy: () => void;
```

#### Returns

`void`
