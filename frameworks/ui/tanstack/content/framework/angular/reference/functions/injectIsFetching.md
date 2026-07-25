---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectIsFetching.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
