---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/functions/createQueries.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: createQueries
title: createQueries
---

# Function: createQueries()

```ts
function createQueries<T, TCombinedResult>(createQueriesOptions, queryClient?): TCombinedResult;
```

Defined in: [packages/svelte-query/src/createQueries.svelte.ts:189](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/createQueries.svelte.ts#L189)

## Type Parameters

### T

`T` *extends* `any`[]

### TCombinedResult

`TCombinedResult` = `T` *extends* \[\] ? \[\] : `T` *extends* \[`Head`\] ? \[`GetCreateQueryResult`\<`Head`\>\] : `T` *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetCreateQueryResult`\<`Head`\>, `GetCreateQueryResult`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetCreateQueryResult`\<`Head`\>, `GetCreateQueryResult`\<`Head`\>, `GetCreateQueryResult`\<`Head`\>\] : \[`...Tails[]`\] *extends* \[`Head`, `...Tails[]`\] ? \[`...(...)[]`\] *extends* \[\] ? \[\] : ... *extends* ... ? ... : ... : \[`...{ [K in (...)]: (...) }[]`\] : \[...\{ \[K in string \| number \| symbol\]: GetCreateQueryResult\<Tails\[K\<(...)\>\]\> \}\[\]\] : \{ \[K in string \| number \| symbol\]: GetCreateQueryResult\<T\[K\<K\>\]\> \}

## Parameters

### createQueriesOptions

[`Accessor`](../type-aliases/Accessor.md)\<\{
  `combine?`: (`result`) => `TCombinedResult`;
  `queries`:   \| readonly \[`T` *extends* \[\] ? \[\] : `T` *extends* \[`Head`\] ? \[`GetCreateQueryOptionsForCreateQueries`\<`Head`\>\] : `T` *extends* \[`Head`, `...Tails[]`\] ? \[`...Tails[]`\] *extends* \[\] ? \[\] : \[`...Tails[]`\] *extends* \[`Head`\] ? \[`GetCreateQueryOptionsForCreateQueries`\<...\>, `GetCreateQueryOptionsForCreateQueries`\<...\>\] : \[`...(...)[]`\] *extends* \[..., `...(...)[]`\] ? ... *extends* ... ? ... : ... : ... *extends* ... ? ... : ... : readonly `unknown`[] *extends* `T` ? `T` : `T` *extends* `CreateQueryOptionsForCreateQueries`\<..., ..., ..., ...\>[] ? `CreateQueryOptionsForCreateQueries`\<..., ..., ..., ...\>[] : `CreateQueryOptionsForCreateQueries`\<..., ..., ..., ...\>[]\]
     \| readonly \[\{ \[K in string \| number \| symbol\]: GetCreateQueryOptionsForCreateQueries\<T\[K\<K\>\]\> \}\];
\}\>

### queryClient?

[`Accessor`](../type-aliases/Accessor.md)\<`QueryClient`\>

## Returns

`TCombinedResult`
