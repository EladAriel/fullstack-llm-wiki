---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectIsMutating.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.422620Z"
---
# Injectismutating

---
id: injectIsMutating
title: injectIsMutating
---

```ts
function injectIsMutating(filters?, options?): Signal<number>;
```

Defined in: [inject-is-mutating.ts:30](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-is-mutating.ts#L30)

Injects a signal that tracks the number of mutations that your application is fetching.

Can be used for app-wide loading indicators

## Parameters

### filters?

`MutationFilters`\<`unknown`, `Error`, `unknown`, `unknown`\>

The filters to apply to the query.

### options?

[`InjectIsMutatingOptions`](../interfaces/InjectIsMutatingOptions.md)

Additional configuration

## Returns

`Signal`\<`number`\>

A read-only signal with the number of fetching mutations.
