---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/IsFetchingAccessor.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
