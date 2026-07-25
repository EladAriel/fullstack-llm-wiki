---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/InfiniteQueryResultAccessor.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: InfiniteQueryResultAccessor
title: InfiniteQueryResultAccessor
---

# Type Alias: InfiniteQueryResultAccessor\<TData, TError\>

```ts
type InfiniteQueryResultAccessor<TData, TError> = ValueAccessor<InfiniteQueryObserverResult<TData, TError>> & object;
```

Defined in: [packages/lit-query/src/createInfiniteQueryController.ts:48](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createInfiniteQueryController.ts#L48)

Accessor returned by `createInfiniteQueryController`.

Call the accessor or read its `current` property to get the latest infinite
query result. The attached methods delegate to the active infinite query
observer.

## Type Declaration

### destroy()

```ts
destroy: () => void;
```

Removes the controller from its Lit host and unsubscribes observers.

#### Returns

`void`

### fetchNextPage

```ts
fetchNextPage: InfiniteQueryObserverResult<TData, TError>["fetchNextPage"];
```

Fetches the next page for the current infinite query.

### fetchPreviousPage

```ts
fetchPreviousPage: InfiniteQueryObserverResult<TData, TError>["fetchPreviousPage"];
```

Fetches the previous page for the current infinite query.

### refetch

```ts
refetch: InfiniteQueryObserverResult<TData, TError>["refetch"];
```

Refetches the current infinite query.

## Type Parameters

### TData

`TData`

### TError

`TError`
