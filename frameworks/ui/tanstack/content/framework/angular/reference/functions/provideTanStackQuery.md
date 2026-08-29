---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/provideTanStackQuery.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.422458Z"
---
# Providetanstackquery

---
id: provideTanStackQuery
title: provideTanStackQuery
---

```ts
function provideTanStackQuery(queryClient, ...features): Provider[];
```

Defined in: [providers.ts:105](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/providers.ts#L105)

Sets up providers necessary to enable TanStack Query functionality for Angular applications.

Allows configuring a `QueryClient` and optional features such as developer tools.

**Example - standalone**

```ts
import {
  provideTanStackQuery,
  QueryClient,
} from '@tanstack/angular-query-experimental'

bootstrapApplication(AppComponent, {
  providers: [provideTanStackQuery(new QueryClient())],
})
```

**Example - NgModule-based**

```ts
import {
  provideTanStackQuery,
  QueryClient,
} from '@tanstack/angular-query-experimental'

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  providers: [provideTanStackQuery(new QueryClient())],
  bootstrap: [AppComponent],
})
export class AppModule {}
```

You can also enable optional developer tools by adding `withDevtools`. By
default the tools will then be loaded when your app is in development mode.
```ts
import {
  provideTanStackQuery,
  withDevtools
  QueryClient,
} from '@tanstack/angular-query-experimental'

bootstrapApplication(AppComponent,
  {
    providers: [
      provideTanStackQuery(new QueryClient(), withDevtools())
    ]
  }
)
```

**Example: using an InjectionToken**

```ts
export const MY_QUERY_CLIENT = new InjectionToken('', {
  factory: () => new QueryClient(),
})

// In a lazy loaded route or lazy loaded component's providers array:
providers: [provideTanStackQuery(MY_QUERY_CLIENT)]
```
Using an InjectionToken for the QueryClient is an advanced optimization which allows TanStack Query to be absent from the main application bundle.
This can be beneficial if you want to include TanStack Query on lazy loaded routes only while still sharing a `QueryClient`.

Note that this is a small optimization and for most applications it's preferable to provide the `QueryClient` in the main application config.

## Parameters

### queryClient

A `QueryClient` instance, or an `InjectionToken` which provides a `QueryClient`.

`QueryClient` | `InjectionToken`\<`QueryClient`\>

### features

...[`QueryFeatures`](../type-aliases/QueryFeatures.md)[]

Optional features to configure additional Query functionality.

## Returns

`Provider`[]

A set of providers to set up TanStack Query.

## See

 - https://tanstack.com/query/v5/docs/framework/angular/quick-start
 - withDevtools
