---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/type-aliases/QueryFeatures.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: QueryFeatures
title: QueryFeatures
---

# Type Alias: QueryFeatures

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
