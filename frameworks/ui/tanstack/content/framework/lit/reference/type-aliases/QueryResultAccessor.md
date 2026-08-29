---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/QueryResultAccessor.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.390715Z"
---
# Queryresultaccessor

---
id: QueryResultAccessor
title: QueryResultAccessor
---

```ts
type QueryResultAccessor<TData, TError> = ValueAccessor<QueryObserverResult<TData, TError>> & object;
```

Defined in: [packages/lit-query/src/createQueryController.ts:42](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueryController.ts#L42)

Accessor returned by `createQueryController`.

Call the accessor or read its `current` property to get the latest query
result. The attached methods delegate to the active query observer.

## Type Declaration

### destroy()

```ts
destroy: () => void;
```

Removes the controller from its Lit host and unsubscribes observers.

#### Returns

`void`

### refetch

```ts
refetch: QueryObserverResult<TData, TError>["refetch"];
```

Refetches the current query.

### suspense()

```ts
suspense: () => Promise<QueryObserverResult<TData, TError>>;
```

Resolves with an optimistic query result, fetching first when needed.

#### Returns

`Promise`\<`QueryObserverResult`\<`TData`, `TError`\>\>

## Type Parameters

### TData

`TData`

### TError

`TError`
