---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useInfiniteQuery.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useInfiniteQuery
title: useInfiniteQuery
---

# Function: useInfiniteQuery()

## Call Signature

```ts
function useInfiniteQuery<TQueryFnData, TError, TData, TQueryKey, TPageParam>(options, queryClient?): DefinedUseInfiniteQueryResult<TData, TError>;
```

Defined in: [preact-query/src/useInfiniteQuery.ts:20](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useInfiniteQuery.ts#L20)

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

#### options

[`DefinedInitialDataInfiniteOptions`](../type-aliases/DefinedInitialDataInfiniteOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`, `TPageParam`\>

#### queryClient?

`QueryClient`

### Returns

[`DefinedUseInfiniteQueryResult`](../type-aliases/DefinedUseInfiniteQueryResult.md)\<`TData`, `TError`\>

## Call Signature

```ts
function useInfiniteQuery<TQueryFnData, TError, TData, TQueryKey, TPageParam>(options, queryClient?): UseInfiniteQueryResult<TData, TError>;
```

Defined in: [preact-query/src/useInfiniteQuery.ts:37](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useInfiniteQuery.ts#L37)

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

#### options

[`UndefinedInitialDataInfiniteOptions`](../type-aliases/UndefinedInitialDataInfiniteOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`, `TPageParam`\>

#### queryClient?

`QueryClient`

### Returns

[`UseInfiniteQueryResult`](../type-aliases/UseInfiniteQueryResult.md)\<`TData`, `TError`\>

## Call Signature

```ts
function useInfiniteQuery<TQueryFnData, TError, TData, TQueryKey, TPageParam>(options, queryClient?): UseInfiniteQueryResult<TData, TError>;
```

Defined in: [preact-query/src/useInfiniteQuery.ts:54](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useInfiniteQuery.ts#L54)

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

#### options

[`UseInfiniteQueryOptions`](../interfaces/UseInfiniteQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`, `TPageParam`\>

#### queryClient?

`QueryClient`

### Returns

[`UseInfiniteQueryResult`](../type-aliases/UseInfiniteQueryResult.md)\<`TData`, `TError`\>
