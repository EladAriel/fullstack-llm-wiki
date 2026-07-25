---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/provideAngularQuery.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
