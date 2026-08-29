---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectInfiniteQuery.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.423012Z"
---
# Injectinfinitequery

---
id: injectInfiniteQuery
title: injectInfiniteQuery
---

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
