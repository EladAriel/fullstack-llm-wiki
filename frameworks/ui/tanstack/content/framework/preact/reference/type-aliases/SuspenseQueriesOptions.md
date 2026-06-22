---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/SuspenseQueriesOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: SuspenseQueriesOptions
title: SuspenseQueriesOptions
---

# Type Alias: SuspenseQueriesOptions\<T, TResults, TDepth\>

```ts
type SuspenseQueriesOptions<T, TResults, TDepth> = TDepth["length"] extends MAXIMUM_DEPTH ? UseSuspenseQueryOptions[] : T extends [] ? [] : T extends [infer Head] ? [...TResults, GetUseSuspenseQueryOptions<Head>] : T extends [infer Head, ...(infer Tails)] ? SuspenseQueriesOptions<[...Tails], [...TResults, GetUseSuspenseQueryOptions<Head>], [...TDepth, 1]> : unknown[] extends T ? T : T extends UseSuspenseQueryOptions<infer TQueryFnData, infer TError, infer TData, infer TQueryKey>[] ? UseSuspenseQueryOptions<TQueryFnData, TError, TData, TQueryKey>[] : UseSuspenseQueryOptions[];
```

Defined in: [preact-query/src/useSuspenseQueries.ts:109](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useSuspenseQueries.ts#L109)

SuspenseQueriesOptions reducer recursively unwraps function arguments to infer/enforce type param

## Type Parameters

### T

`T` *extends* `any`[]

### TResults

`TResults` *extends* `any`[] = \[\]

### TDepth

`TDepth` *extends* `ReadonlyArray`\<`number`\> = \[\]
