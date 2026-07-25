---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/CreateQueriesControllerOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: CreateQueriesControllerOptions
title: CreateQueriesControllerOptions
---

# Type Alias: CreateQueriesControllerOptions\<TQueryOptions, TCombinedResult\>

```ts
type CreateQueriesControllerOptions<TQueryOptions, TCombinedResult> = object;
```

Defined in: [packages/lit-query/src/createQueriesController.ts:194](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L194)

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

Defined in: [packages/lit-query/src/createQueriesController.ts:208](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L208)

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

Defined in: [packages/lit-query/src/createQueriesController.ts:199](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L199)

Query options to observe, or a getter that returns the current options.
