---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/classes/QueryClientProvider.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.387422Z"
---
# Queryclientprovider

---
id: QueryClientProvider
title: QueryClientProvider
---

Defined in: [packages/lit-query/src/QueryClientProvider.ts:64](https://github.com/TanStack/query/blob/main/packages/lit-query/src/QueryClientProvider.ts#L64)

Lit element that provides a `QueryClient` to descendant Lit Query
controllers through Lit context.

The `client` is a property, not an attribute. When rendering this element in
a Lit template, bind it with property binding: `.client=${queryClient}`.
The provider throws if it connects without a client, or if an already
connected provider has its client cleared.

This class is not registered as a custom element by the package. Applications
must register either a subclass or the class itself with
`customElements.define`.

## Examples

```ts
import { html, LitElement } from 'lit'
import { QueryClient, QueryClientProvider } from '@tanstack/lit-query'

const queryClient = new QueryClient()

class AppQueryProvider extends QueryClientProvider {
  constructor() {
    super()
    this.client = queryClient
  }
}

customElements.define('app-query-provider', AppQueryProvider)

class AppRoot extends LitElement {
  render() {
    return html`<app-query-provider><todos-view></todos-view></app-query-provider>`
  }
}
```

```ts
import { html } from 'lit'
import { QueryClient, QueryClientProvider } from '@tanstack/lit-query'

const queryClient = new QueryClient()

customElements.define('query-client-provider', QueryClientProvider)

const view = html`
  <query-client-provider .client=${queryClient}>
    <todos-view></todos-view>
  </query-client-provider>
`
```

## Extends

- `LitElement`

## Constructors

### Constructor

```ts
new QueryClientProvider(): QueryClientProvider;
```

Defined in: [packages/lit-query/src/QueryClientProvider.ts:82](https://github.com/TanStack/query/blob/main/packages/lit-query/src/QueryClientProvider.ts#L82)

#### Returns

`QueryClientProvider`

#### Overrides

```ts
LitElement.constructor
```

## Properties

### client

```ts
client: QueryClient;
```

Defined in: [packages/lit-query/src/QueryClientProvider.ts:76](https://github.com/TanStack/query/blob/main/packages/lit-query/src/QueryClientProvider.ts#L76)

The `QueryClient` provided to descendant controllers and global fallback
helpers while this provider is connected.

Bind this as a property in Lit templates with `.client=${queryClient}`.
