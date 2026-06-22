---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/InfiniteQueryResultAccessor.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
