---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useSuspenseQueries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useSuspenseQueries
title: useSuspenseQueries
---

# Function: useSuspenseQueries()

## Call Signature

```ts
function useSuspenseQueries<T, TCombinedResult>(options, queryClient?): TCombinedResult;
```

Defined in: [preact-query/src/useSuspenseQueries.ts:164](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useSuspenseQueries.ts#L164)

### Type Parameters

#### T

`T` *extends* `any`[]

#### TCombinedResult

`TCombinedResult` = `T` *extends* \[\] ? \[\] : `T` *extends* \[`Head`\] ? \[`GetUseSuspenseQueryResult`\<`Head`\>\] : `T` *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseSuspenseQueryResult`\<`Head`\>, `GetUseSuspenseQueryResult`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseSuspenseQueryResult`\<`Head`\>, `GetUseSuspenseQueryResult`\<`Head`\>, `GetUseSuspenseQueryResult`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...(...)[]`\] *extends* \[\] ? \[\] : ... *extends* ... ? ... : ... : \[`...{ [K in (...)]: (...) }[]`\] : \[...\{ \[K in string \| number \| symbol\]: GetUseSuspenseQueryResult\<Tails\[K\<(...)\>\]\> \}\[\]\] : \{ \[K in string \| number \| symbol\]: GetUseSuspenseQueryResult\<T\[K\<K\>\]\> \}

### Parameters

#### options

##### combine?

(`result`) => `TCombinedResult`

##### queries

  \| readonly \[`T` *extends* \[\] ? \[\] : `T` *extends* \[`Head`\] ? \[`GetUseSuspenseQueryOptions`\<`Head`\>\] : `T` *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseSuspenseQueryOptions`\<`Head`\>, `GetUseSuspenseQueryOptions`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...(...)[]`\] *extends* \[\] ? \[\] : ... *extends* ... ? ... : ... : ...[] *extends* \[`...(...)[]`\] ? \[`...(...)[]`\] : ... *extends* ... ? ... : ... : `unknown`[] *extends* `T` ? `T` : `T` *extends* [`UseSuspenseQueryOptions`](../interfaces/UseSuspenseQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>[] ? [`UseSuspenseQueryOptions`](../interfaces/UseSuspenseQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>[] : [`UseSuspenseQueryOptions`](../interfaces/UseSuspenseQueryOptions.md)\<`unknown`, `Error`, `unknown`, readonly ...[]\>[]\]
  \| readonly \[\{ \[K in string \| number \| symbol\]: GetUseSuspenseQueryOptions\<T\[K\<K\>\]\> \}\]

#### queryClient?

`QueryClient`

### Returns

`TCombinedResult`

## Call Signature

```ts
function useSuspenseQueries<T, TCombinedResult>(options, queryClient?): TCombinedResult;
```

Defined in: [preact-query/src/useSuspenseQueries.ts:177](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useSuspenseQueries.ts#L177)

### Type Parameters

#### T

`T` *extends* `any`[]

#### TCombinedResult

`TCombinedResult` = `T` *extends* \[\] ? \[\] : `T` *extends* \[`Head`\] ? \[`GetUseSuspenseQueryResult`\<`Head`\>\] : `T` *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseSuspenseQueryResult`\<`Head`\>, `GetUseSuspenseQueryResult`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseSuspenseQueryResult`\<`Head`\>, `GetUseSuspenseQueryResult`\<`Head`\>, `GetUseSuspenseQueryResult`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...(...)[]`\] *extends* \[\] ? \[\] : ... *extends* ... ? ... : ... : \[`...{ [K in (...)]: (...) }[]`\] : \[...\{ \[K in string \| number \| symbol\]: GetUseSuspenseQueryResult\<Tails\[K\<(...)\>\]\> \}\[\]\] : \{ \[K in string \| number \| symbol\]: GetUseSuspenseQueryResult\<T\[K\<K\>\]\> \}

### Parameters

#### options

##### combine?

(`result`) => `TCombinedResult`

##### queries

readonly \[`T` *extends* \[\] ? \[\] : `T` *extends* \[`Head`\] ? \[`GetUseSuspenseQueryOptions`\<`Head`\>\] : `T` *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseSuspenseQueryOptions`\<`Head`\>, `GetUseSuspenseQueryOptions`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...(...)[]`\] *extends* \[...\] ? \[..., ..., ...\] : ... *extends* ... ? ... : ... : `unknown`[] *extends* \[`...Tails[]`\] ? \[`...Tails[]`\] : \[`...(...)[]`\] *extends* ...[] ? ...[] : ...[] : `unknown`[] *extends* `T` ? `T` : `T` *extends* [`UseSuspenseQueryOptions`](../interfaces/UseSuspenseQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>[] ? [`UseSuspenseQueryOptions`](../interfaces/UseSuspenseQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>[] : [`UseSuspenseQueryOptions`](../interfaces/UseSuspenseQueryOptions.md)\<`unknown`, `Error`, `unknown`, readonly `unknown`[]\>[]\]

#### queryClient?

`QueryClient`

### Returns

`TCombinedResult`
