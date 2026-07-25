---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/QueriesControllerOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
