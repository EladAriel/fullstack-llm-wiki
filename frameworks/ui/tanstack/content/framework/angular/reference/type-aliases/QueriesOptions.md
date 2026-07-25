---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/QueriesOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: QueriesOptions
title: QueriesOptions
---

# Type Alias: QueriesOptions\<T, TResults, TDepth\>

```ts
type QueriesOptions<T, TResults, TDepth> = TDepth["length"] extends MAXIMUM_DEPTH ? QueryObserverOptionsForCreateQueries[] : T extends [] ? [] : T extends [infer Head] ? [...TResults, GetCreateQueryOptionsForCreateQueries<Head>] : T extends [infer Head, ...(infer Tails)] ? QueriesOptions<[...Tails], [...TResults, GetCreateQueryOptionsForCreateQueries<Head>], [...TDepth, 1]> : ReadonlyArray<unknown> extends T ? T : T extends QueryObserverOptionsForCreateQueries<infer TQueryFnData, infer TError, infer TData, infer TQueryKey>[] ? QueryObserverOptionsForCreateQueries<TQueryFnData, TError, TData, TQueryKey>[] : QueryObserverOptionsForCreateQueries[];
```

Defined in: [inject-queries.ts:144](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-queries.ts#L144)

QueriesOptions reducer recursively unwraps function arguments to infer/enforce type param

## Type Parameters

### T

`T` *extends* `any`[]

### TResults

`TResults` *extends* `any`[] = \[\]

### TDepth

`TDepth` *extends* `ReadonlyArray`\<`number`\> = \[\]
