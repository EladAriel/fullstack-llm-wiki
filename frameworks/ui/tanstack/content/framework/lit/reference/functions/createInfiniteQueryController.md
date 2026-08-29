---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/createInfiniteQueryController.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.386795Z"
---
# Createinfinitequerycontroller

---
id: createInfiniteQueryController
title: createInfiniteQueryController
---

```ts
function createInfiniteQueryController<TQueryFnData, TError, TData, TQueryKey, TPageParam>(
   host,
   options,
queryClient?): InfiniteQueryResultAccessor<TData, TError>;
```

Defined in: [packages/lit-query/src/createInfiniteQueryController.ts:402](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createInfiniteQueryController.ts#L402)

Creates a Lit reactive controller that subscribes the host to an infinite
query.

The returned accessor is callable and also exposes `current`, `refetch`,
`fetchNextPage`, `fetchPreviousPage`, and `destroy`. When `options` is a
function, it is re-read during host updates so query keys and options can
follow reactive host state.

If `queryClient` is omitted, the controller resolves the client from the
nearest connected `QueryClientProvider`.

## Type Parameters

### TQueryFnData

`TQueryFnData` = `unknown`

### TError

`TError` = `Error`

### TData

`TData` = `InfiniteData`\<`TQueryFnData`, `unknown`\>

### TQueryKey

`TQueryKey` *extends* readonly `unknown`[] = readonly `unknown`[]

### TPageParam

`TPageParam` = `unknown`

## Parameters

### host

`ReactiveControllerHost`

The Lit reactive controller host that owns the infinite query
subscription.

### options

[`Accessor`](../type-aliases/Accessor.md)\<[`CreateInfiniteQueryOptions`](../type-aliases/CreateInfiniteQueryOptions.md)\<`TQueryFnData`, `TError`, `TData`, `TQueryKey`, `TPageParam`\>\>

Infinite query observer options, or a getter that returns
options.

### queryClient?

`QueryClient`

Optional explicit query client. Provide this for
controllers that should not resolve a client from Lit context.

## Returns

[`InfiniteQueryResultAccessor`](../type-aliases/InfiniteQueryResultAccessor.md)\<`TData`, `TError`\>

An accessor for the latest infinite query result with page helper
methods.

## Example

```ts
import { LitElement, html } from 'lit'
import { createInfiniteQueryController } from '@tanstack/lit-query'

class ProjectsView extends LitElement {
  private readonly projects = createInfiniteQueryController(this, {
    queryKey: ['projects'],
    queryFn: ({ pageParam }) => fetchProjects(pageParam),
    initialPageParam: 0,
    getNextPageParam: (lastPage) => lastPage.nextCursor,
  })

  render() {
    const query = this.projects()

    return html`
      <button ?disabled=${!query.hasNextPage} @click=${() => this.projects.fetchNextPage()}>
        Load more
      </button>
    `
  }
}
```
