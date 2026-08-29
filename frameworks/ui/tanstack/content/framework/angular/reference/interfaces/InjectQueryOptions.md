---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/interfaces/InjectQueryOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.429223Z"
---
# Injectqueryoptions

---
id: InjectQueryOptions
title: InjectQueryOptions
---

Defined in: [inject-query.ts:20](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-query.ts#L20)

## Properties

### injector?

```ts
optional injector: Injector;
```

Defined in: [inject-query.ts:26](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-query.ts#L26)

The `Injector` in which to create the query.

If this is not provided, the current injection context will be used instead (via `inject`).
