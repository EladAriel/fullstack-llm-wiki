---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/provideAngularQuery.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.421975Z"
---
# Provideangularquery

---
id: provideAngularQuery
title: provideAngularQuery
---

```ts
function provideAngularQuery(queryClient): Provider[];
```

Defined in: [providers.ts:124](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/providers.ts#L124)

Sets up providers necessary to enable TanStack Query functionality for Angular applications.

Allows configuring a `QueryClient`.

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
