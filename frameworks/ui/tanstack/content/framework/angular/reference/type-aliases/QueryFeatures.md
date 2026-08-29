---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/QueryFeatures.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.425720Z"
---
# Queryfeatures

---
id: QueryFeatures
title: QueryFeatures
---

```ts
type QueryFeatures = 
  | DevtoolsFeature
  | PersistQueryClientFeature;
```

Defined in: [providers.ts:173](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/providers.ts#L173)

A type alias that represents all Query features available for use with `provideTanStackQuery`.
Features can be enabled by adding special functions to the `provideTanStackQuery` call.
See documentation for each symbol to find corresponding function name. See also `provideTanStackQuery`
documentation on how to use those functions.

## See

[provideTanStackQuery](../functions/provideTanStackQuery.md)
