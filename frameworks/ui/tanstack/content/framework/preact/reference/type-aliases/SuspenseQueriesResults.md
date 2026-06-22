---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/SuspenseQueriesResults.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: SuspenseQueriesResults
title: SuspenseQueriesResults
---

# Type Alias: SuspenseQueriesResults\<T, TResults, TDepth\>

```ts
type SuspenseQueriesResults<T, TResults, TDepth> = TDepth["length"] extends MAXIMUM_DEPTH ? UseSuspenseQueryResult[] : T extends [] ? [] : T extends [infer Head] ? [...TResults, GetUseSuspenseQueryResult<Head>] : T extends [infer Head, ...(infer Tails)] ? SuspenseQueriesResults<[...Tails], [...TResults, GetUseSuspenseQueryResult<Head>], [...TDepth, 1]> : { [K in keyof T]: GetUseSuspenseQueryResult<T[K]> };
```

Defined in: [preact-query/src/useSuspenseQueries.ts:146](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/useSuspenseQueries.ts#L146)

SuspenseQueriesResults reducer recursively maps type param to results

## Type Parameters

### T

`T` *extends* `any`[]

### TResults

`TResults` *extends* `any`[] = \[\]

### TDepth

`TDepth` *extends* `ReadonlyArray`\<`number`\> = \[\]
