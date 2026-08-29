---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/provideQueryClient.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.423339Z"
---
# Providequeryclient

---
id: provideQueryClient
title: provideQueryClient
---

```ts
function provideQueryClient(queryClient): Provider;
```

Defined in: [providers.ts:14](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/providers.ts#L14)

Usually [provideTanStackQuery](provideTanStackQuery.md) is used once to set up TanStack Query and the
[https://tanstack.com/query/latest/docs/reference/QueryClient\|QueryClient](https://tanstack.com/query/latest/docs/reference/QueryClient|QueryClient)
for the entire application. Internally it calls `provideQueryClient`.
You can use `provideQueryClient` to provide a different `QueryClient` instance for a part
of the application or for unit testing purposes.

## Parameters

### queryClient

A `QueryClient` instance, or an `InjectionToken` which provides a `QueryClient`.

`QueryClient` | `InjectionToken`\<`QueryClient`\>

## Returns

`Provider`

a provider object that can be used to provide the `QueryClient` instance.
