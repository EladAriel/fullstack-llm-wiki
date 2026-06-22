---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectIsFetching.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: injectIsFetching
title: injectIsFetching
---

# Function: injectIsFetching()

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
