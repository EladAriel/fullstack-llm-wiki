---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/CreateQueriesControllerOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.389770Z"
---
# Createqueriescontrolleroptions

---
id: CreateQueriesControllerOptions
title: CreateQueriesControllerOptions
---

```ts
type CreateQueriesControllerOptions<TQueryOptions, TCombinedResult> = object;
```

Defined in: [packages/lit-query/src/createQueriesController.ts:195](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L195)

Options accepted by `createQueriesController`.

`queries` can be a static list or a getter that returns the current list.
`combine` can reshape the array of query results into a single value for the
returned accessor.

## Type Parameters

### TQueryOptions

`TQueryOptions` *extends* `any`[] = `any`[]

### TCombinedResult

`TCombinedResult` = `CreateQueriesResults`\<`TQueryOptions`\>

## Properties

### combine()?

```ts
optional combine: (result) => TCombinedResult;
```

Defined in: [packages/lit-query/src/createQueriesController.ts:209](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L209)

Optional function that combines the query result array into one value.

#### Parameters

##### result

`CreateQueriesResults`\<`TQueryOptions`\>

#### Returns

`TCombinedResult`

***

### queries

```ts
queries: Accessor<
  | readonly [...CreateQueriesOptions<TQueryOptions>]
| readonly [...{ [K in keyof TQueryOptions]: GetCreateQueriesInput<TQueryOptions[K]> }]>;
```

Defined in: [packages/lit-query/src/createQueriesController.ts:200](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L200)

Query options to observe, or a getter that returns the current options.
