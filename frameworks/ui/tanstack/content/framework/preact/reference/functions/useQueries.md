---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useQueries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useQueries
title: useQueries
---

# Function: useQueries()

```ts
function useQueries<T, TCombinedResult>(__namedParameters, queryClient?): TCombinedResult;
```

Defined in: [preact-query/src/useQueries.ts:207](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useQueries.ts#L207)

## Type Parameters

### T

`T` *extends* `any`[]

### TCombinedResult

`TCombinedResult` = `T` *extends* \[\] ? \[\] : `T` *extends* \[`Head`\] ? \[`GetUseQueryResult`\<`Head`\>\] : `T` *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseQueryResult`\<`Head`\>, `GetUseQueryResult`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseQueryResult`\<`Head`\>, `GetUseQueryResult`\<`Head`\>, `GetUseQueryResult`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...(...)[]`\] *extends* \[\] ? \[\] : ... *extends* ... ? ... : ... : \[`...{ [K in (...)]: (...) }[]`\] : \[...\{ \[K in string \| number \| symbol\]: GetUseQueryResult\<Tails\[K\<(...)\>\]\> \}\[\]\] : \{ \[K in string \| number \| symbol\]: GetUseQueryResult\<T\[K\<K\>\]\> \}

## Parameters

### \_\_namedParameters

#### combine?

(`result`) => `TCombinedResult`

#### queries

  \| readonly \[`T` *extends* \[\] ? \[\] : `T` *extends* \[`Head`\] ? \[`GetUseQueryOptionsForUseQueries`\<`Head`\>\] : `T` *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetUseQueryOptionsForUseQueries`\<`Head`\>, `GetUseQueryOptionsForUseQueries`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...(...)[]`\] *extends* \[\] ? \[\] : ... *extends* ... ? ... : ... : readonly ...[] *extends* \[`...(...)[]`\] ? \[`...(...)[]`\] : ... *extends* ... ? ... : ... : readonly `unknown`[] *extends* `T` ? `T` : `T` *extends* `UseQueryOptionsForUseQueries`\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>[] ? `UseQueryOptionsForUseQueries`\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`\>[] : `UseQueryOptionsForUseQueries`\<`unknown`, `Error`, `unknown`, readonly ...[]\>[]\]
  \| readonly \[\{ \[K in string \| number \| symbol\]: GetUseQueryOptionsForUseQueries\<T\[K\<K\>\]\> \}\]

#### subscribed?

`boolean`

### queryClient?

`QueryClient`

## Returns

`TCombinedResult`
