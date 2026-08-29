---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/QueriesControllerOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.388861Z"
---
# Queriescontrolleroptions

---
id: QueriesControllerOptions
title: QueriesControllerOptions
---

```ts
type QueriesControllerOptions<TQueryOptions, TCombinedResult> = Accessor<CreateQueriesControllerOptions<TQueryOptions, TCombinedResult>>;
```

Defined in: [packages/lit-query/src/types.ts:74](https://github.com/TanStack/query/blob/main/packages/lit-query/src/types.ts#L74)

Accessor-wrapped options accepted by `createQueriesController`.

## Type Parameters

### TQueryOptions

`TQueryOptions` *extends* `any`[] = `any`[]

### TCombinedResult

`TCombinedResult` = `CreateQueriesResults`\<`TQueryOptions`\>
