---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/InfiniteQueryResultAccessor.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.388558Z"
---
# Infinitequeryresultaccessor

---
id: InfiniteQueryResultAccessor
title: InfiniteQueryResultAccessor
---

```ts
type InfiniteQueryResultAccessor<TData, TError> = ValueAccessor<InfiniteQueryObserverResult<TData, TError>> & object;
```

Defined in: [packages/lit-query/src/createInfiniteQueryController.ts:49](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createInfiniteQueryController.ts#L49)

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
