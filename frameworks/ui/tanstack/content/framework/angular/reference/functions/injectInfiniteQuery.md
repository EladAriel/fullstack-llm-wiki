---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectInfiniteQuery.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: injectInfiniteQuery
title: injectInfiniteQuery
---

# Function: injectInfiniteQuery()

Injects an infinite query: a declarative dependency on an asynchronous source of data that is tied to a unique key.
Infinite queries can additively "load more" data onto an existing set of data or "infinite scroll"

## Param

A function that returns infinite query options.

## Param

Additional configuration.

## Call Signature

```ts
function injectInfiniteQuery<TQueryFnData, TError, TData, TQueryKey, TPageParam>(injectInfiniteQueryFn, options?): DefinedCreateInfiniteQueryResult<TData, TError>;
```

Defined in: [inject-infinite-query.ts:41](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-infinite-query.ts#L41)

Injects an infinite query: a declarative dependency on an asynchronous source of data that is tied to a unique key.
Infinite queries can additively "load more" data onto an existing set of data or "infinite scroll"

### Type Parameters

#### TQueryFnData

`TQueryFnData`

#### TError

`TError` = `Error`

#### TData

`TData` = `InfiniteData`\<`TQueryFnData`, `unknown`\>

#### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

#### TPageParam

`TPageParam` = `unknown`

### Parameters

#### injectInfiniteQueryFn

() => [`DefinedInitialDataInfiniteOptions`](../type-aliases/DefinedInitialDataInfiniteOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`, `TPageParam`\>

A function that returns infinite query options.

#### options?

[`InjectInfiniteQueryOptions`](../interfaces/InjectInfiniteQueryOptions.md)

Additional configuration.

### Returns

[`DefinedCreateInfiniteQueryResult`](../type-aliases/DefinedCreateInfiniteQueryResult.md)\<`TData`, `TError`\>

The infinite query result.

## Call Signature

```ts
function injectInfiniteQuery<TQueryFnData, TError, TData, TQueryKey, TPageParam>(injectInfiniteQueryFn, options?): CreateInfiniteQueryResult<TData, TError>;
```

Defined in: [inject-infinite-query.ts:65](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-infinite-query.ts#L65)

Injects an infinite query: a declarative dependency on an asynchronous source of data that is tied to a unique key.
Infinite queries can additively "load more" data onto an existing set of data or "infinite scroll"

### Type Parameters

#### TQueryFnData

`TQueryFnData`

#### TError

`TError` = `Error`

#### TData

`TData` = `InfiniteData`\<`TQueryFnData`, `unknown`\>

#### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

#### TPageParam

`TPageParam` = `unknown`

### Parameters

#### injectInfiniteQueryFn

() => [`UndefinedInitialDataInfiniteOptions`](../type-aliases/UndefinedInitialDataInfiniteOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`, `TPageParam`\>

A function that returns infinite query options.

#### options?

[`InjectInfiniteQueryOptions`](../interfaces/InjectInfiniteQueryOptions.md)

Additional configuration.

### Returns

[`CreateInfiniteQueryResult`](../type-aliases/CreateInfiniteQueryResult.md)\<`TData`, `TError`\>

The infinite query result.

## Call Signature

```ts
function injectInfiniteQuery<TQueryFnData, TError, TData, TQueryKey, TPageParam>(injectInfiniteQueryFn, options?): CreateInfiniteQueryResult<TData, TError>;
```

Defined in: [inject-infinite-query.ts:89](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-infinite-query.ts#L89)

Injects an infinite query: a declarative dependency on an asynchronous source of data that is tied to a unique key.
Infinite queries can additively "load more" data onto an existing set of data or "infinite scroll"

### Type Parameters

#### TQueryFnData

`TQueryFnData`

#### TError

`TError` = `Error`

#### TData

`TData` = `InfiniteData`\<`TQueryFnData`, `unknown`\>

#### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

#### TPageParam

`TPageParam` = `unknown`

### Parameters

#### injectInfiniteQueryFn

() => [`CreateInfiniteQueryOptions`](../interfaces/CreateInfiniteQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`, `TPageParam`\>

A function that returns infinite query options.

#### options?

[`InjectInfiniteQueryOptions`](../interfaces/InjectInfiniteQueryOptions.md)

Additional configuration.

### Returns

[`CreateInfiniteQueryResult`](../type-aliases/CreateInfiniteQueryResult.md)\<`TData`, `TError`\>

The infinite query result.
