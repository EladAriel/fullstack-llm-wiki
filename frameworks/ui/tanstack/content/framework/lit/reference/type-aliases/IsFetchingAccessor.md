---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/IsFetchingAccessor.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: IsFetchingAccessor
title: IsFetchingAccessor
---

# Type Alias: IsFetchingAccessor

```ts
type IsFetchingAccessor = ValueAccessor<number> & object;
```

Defined in: [packages/lit-query/src/useIsFetching.ts:17](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useIsFetching.ts#L17)

Accessor returned by `useIsFetching`.

Call the accessor or read its `current` property to get the number of
currently fetching queries that match the filters.

## Type Declaration

### destroy()

```ts
destroy: () => void;
```

#### Returns

`void`
