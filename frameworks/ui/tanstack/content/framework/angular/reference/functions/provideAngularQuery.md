---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/provideAngularQuery.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: provideAngularQuery
title: provideAngularQuery
---

# ~~Function: provideAngularQuery()~~

```ts
function provideAngularQuery(queryClient): Provider[];
```

Defined in: [providers.ts:124](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/providers.ts#L124)

Sets up providers necessary to enable TanStack Query functionality for Angular applications.

Allows to configure a `QueryClient`.

## Parameters

### queryClient

`QueryClient`

A `QueryClient` instance.

## Returns

`Provider`[]

A set of providers to set up TanStack Query.

## See

https://tanstack.com/query/v5/docs/framework/angular/quick-start

## Deprecated

Use `provideTanStackQuery` instead.
