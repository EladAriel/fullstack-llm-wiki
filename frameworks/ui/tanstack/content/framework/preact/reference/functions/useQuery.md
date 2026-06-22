---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useQuery.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useQuery
title: useQuery
---

# Function: useQuery()

## Call Signature

```ts
function useQuery<TQueryFnData, TError, TData, TQueryKey>(options, queryClient?): DefinedUseQueryResult<NoInfer<TData>, TError>;
```

Defined in: [preact-query/src/useQuery.ts:19](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useQuery.ts#L19)

### Type Parameters

#### TQueryFnData

`TQueryFnData` = `unknown`

#### TError

`TError` = `Error`

#### TData

`TData` = `TQueryFnData`

#### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

### Parameters

#### options

[`DefinedInitialDataOptions`](../type-aliases/DefinedInitialDataOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>

#### queryClient?

`QueryClient`

### Returns

[`DefinedUseQueryResult`](../type-aliases/DefinedUseQueryResult.md)\<`NoInfer`\<`TData`\>, `TError`\>

## Call Signature

```ts
function useQuery<TQueryFnData, TError, TData, TQueryKey>(options, queryClient?): UseQueryResult<NoInfer<TData>, TError>;
```

Defined in: [preact-query/src/useQuery.ts:29](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useQuery.ts#L29)

### Type Parameters

#### TQueryFnData

`TQueryFnData` = `unknown`

#### TError

`TError` = `Error`

#### TData

`TData` = `TQueryFnData`

#### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

### Parameters

#### options

[`UndefinedInitialDataOptions`](../type-aliases/UndefinedInitialDataOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>

#### queryClient?

`QueryClient`

### Returns

[`UseQueryResult`](../type-aliases/UseQueryResult.md)\<`NoInfer`\<`TData`\>, `TError`\>

## Call Signature

```ts
function useQuery<TQueryFnData, TError, TData, TQueryKey>(options, queryClient?): UseQueryResult<NoInfer<TData>, TError>;
```

Defined in: [preact-query/src/useQuery.ts:39](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useQuery.ts#L39)

### Type Parameters

#### TQueryFnData

`TQueryFnData` = `unknown`

#### TError

`TError` = `Error`

#### TData

`TData` = `TQueryFnData`

#### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

### Parameters

#### options

[`UseQueryOptions`](../interfaces/UseQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>

#### queryClient?

`QueryClient`

### Returns

[`UseQueryResult`](../type-aliases/UseQueryResult.md)\<`NoInfer`\<`TData`\>, `TError`\>
