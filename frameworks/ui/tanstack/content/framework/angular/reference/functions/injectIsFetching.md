---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectIsFetching.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.423187Z"
---
# Injectisfetching

---
id: injectIsFetching
title: injectIsFetching
---

```ts
function injectIsFetching(filters?, options?): Signal<number>;
```

Defined in: [inject-is-fetching.ts:31](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-is-fetching.ts#L31)

Injects a signal that tracks the number of queries that your application is loading or
fetching in the background.

Can be used for app-wide loading indicators

## Parameters

### filters?

`QueryFilters`\<readonly `unknown`[]\>

The filters to apply to the query.

### options?

[`InjectIsFetchingOptions`](../interfaces/InjectIsFetchingOptions.md)

Additional configuration

## Returns

`Signal`\<`number`\>

signal with number of loading or fetching queries.
