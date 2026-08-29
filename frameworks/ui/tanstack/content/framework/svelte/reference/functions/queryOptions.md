---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/functions/queryOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.400115Z"
---
# Queryoptions

---
id: queryOptions
title: queryOptions
---

## Call Signature

```ts
function queryOptions<TQueryFnData, TError, TData, TQueryKey>(options): CreateQueryOptions<TQueryFnData, TError, TData, TQueryKey> & object & QueryKeyWithDataTag<TQueryKey, TQueryFnData, TError>;
```

Defined in: [packages/svelte-query/src/queryOptions.ts:30](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/queryOptions.ts#L30)

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

### Returns

[`CreateQueryOptions`](../type-aliases/CreateQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\> & `object` & `QueryKeyWithDataTag`\<`TQueryKey`, `TQueryFnData`, `TError`\>

## Call Signature

```ts
function queryOptions<TQueryFnData, TError, TData, TQueryKey>(options): CreateQueryOptions<TQueryFnData, TError, TData, TQueryKey> & object & QueryKeyWithDataTag<TQueryKey, TQueryFnData, TError>;
```

Defined in: [packages/svelte-query/src/queryOptions.ts:40](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/queryOptions.ts#L40)

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

### Returns

[`CreateQueryOptions`](../type-aliases/CreateQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\> & `object` & `QueryKeyWithDataTag`\<`TQueryKey`, `TQueryFnData`, `TError`\>
