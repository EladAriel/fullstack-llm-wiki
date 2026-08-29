---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/AnyUseQueryOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.378347Z"
---
# Anyusequeryoptions

---
id: AnyUseQueryOptions
title: AnyUseQueryOptions
---

```ts
type AnyUseQueryOptions = UseQueryOptions<any, any, any, any>;
```

Defined in: [preact-query/src/types.ts:153](https://github.com/TanStack/query/blob/main/packages/preact-query/src/types.ts#L153)

[UseQueryOptions](../interfaces/UseQueryOptions.md) with all type parameters set to `any`, useful when the specific types aren't
relevant, e.g. when accepting options for any query in a helper function.
