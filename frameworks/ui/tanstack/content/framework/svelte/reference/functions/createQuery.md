---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/functions/createQuery.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: createQuery
title: createQuery
---

# Function: createQuery()

## Call Signature

```ts
function createQuery<TQueryFnData, TError, TData, TQueryKey>(options, queryClient?): CreateQueryResult<TData, TError>;
```

Defined in: [packages/svelte-query/src/createQuery.ts:15](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/createQuery.ts#L15)

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

[`Accessor`](../type-aliases/Accessor.md)\<[`UndefinedInitialDataOptions`](../type-aliases/UndefinedInitialDataOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>\>

#### queryClient?

[`Accessor`](../type-aliases/Accessor.md)\<`QueryClient`\>

### Returns

[`CreateQueryResult`](../type-aliases/CreateQueryResult.md)\<`TData`, `TError`\>

## Call Signature

```ts
function createQuery<TQueryFnData, TError, TData, TQueryKey>(options, queryClient?): DefinedCreateQueryResult<TData, TError>;
```

Defined in: [packages/svelte-query/src/createQuery.ts:27](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/createQuery.ts#L27)

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

[`Accessor`](../type-aliases/Accessor.md)\<[`DefinedInitialDataOptions`](../type-aliases/DefinedInitialDataOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>\>

#### queryClient?

[`Accessor`](../type-aliases/Accessor.md)\<`QueryClient`\>

### Returns

[`DefinedCreateQueryResult`](../type-aliases/DefinedCreateQueryResult.md)\<`TData`, `TError`\>

## Call Signature

```ts
function createQuery<TQueryFnData, TError, TData, TQueryKey>(options, queryClient?): CreateQueryResult<TData, TError>;
```

Defined in: [packages/svelte-query/src/createQuery.ts:39](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/createQuery.ts#L39)

### Type Parameters

#### TQueryFnData

`TQueryFnData`

#### TError

`TError` = `Error`

#### TData

`TData` = `TQueryFnData`

#### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

### Parameters

#### options

[`Accessor`](../type-aliases/Accessor.md)\<[`CreateQueryOptions`](../type-aliases/CreateQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>\>

#### queryClient?

[`Accessor`](../type-aliases/Accessor.md)\<`QueryClient`\>

### Returns

[`CreateQueryResult`](../type-aliases/CreateQueryResult.md)\<`TData`, `TError`\>
