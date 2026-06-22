---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/QueriesControllerOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: QueriesControllerOptions
title: QueriesControllerOptions
---

# Type Alias: QueriesControllerOptions\<TQueryOptions, TCombinedResult\>

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
