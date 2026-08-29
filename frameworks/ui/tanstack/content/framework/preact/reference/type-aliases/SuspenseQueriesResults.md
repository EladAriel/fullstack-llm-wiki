---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/SuspenseQueriesResults.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.379900Z"
---
# Suspensequeriesresults

---
id: SuspenseQueriesResults
title: SuspenseQueriesResults
---

```ts
type SuspenseQueriesResults<T, TResults, TDepth> = TDepth["length"] extends MAXIMUM_DEPTH ? UseSuspenseQueryResult[] : T extends [] ? [] : T extends [infer Head] ? [...TResults, GetUseSuspenseQueryResult<Head>] : T extends [infer Head, ...(infer Tails)] ? SuspenseQueriesResults<[...Tails], [...TResults, GetUseSuspenseQueryResult<Head>], [...TDepth, 1]> : { [K in keyof T]: GetUseSuspenseQueryResult<T[K]> };
```

Defined in: [preact-query/src/useSuspenseQueries.ts:165](https://github.com/TanStack/query/blob/main/packages/preact-query/src/useSuspenseQueries.ts#L165)

The result type returned by `useSuspenseQueries`, when no `combine` is provided. Mirrors
[SuspenseQueriesOptions](SuspenseQueriesOptions.md): each tuple element's result type is inferred individually, up to 20 elements.
A non-tuple array is mapped per-element instead, still inferring each entry individually; only past 20
elements does this fall back to a single homogeneous [UseSuspenseQueryResult](UseSuspenseQueryResult.md) type.

## Type Parameters

### T

`T` *extends* `any`[]

The type of the `queries` array, as inferred by [SuspenseQueriesOptions](SuspenseQueriesOptions.md).

### TResults

`TResults` *extends* `any`[] = \[\]

The internal accumulator that this type builds during recursion. It is not meant
to be set explicitly.

### TDepth

`TDepth` *extends* `ReadonlyArray`\<`number`\> = \[\]

The internal recursion-depth counter, checked against the 20-element limit. It is not
meant to be set explicitly.
