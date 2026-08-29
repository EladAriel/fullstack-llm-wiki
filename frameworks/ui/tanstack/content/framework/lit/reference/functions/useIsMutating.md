---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/useIsMutating.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.385997Z"
---
# Useismutating

---
id: useIsMutating
title: useIsMutating
---

```ts
function useIsMutating(
   host,
   filters,
   queryClient?): IsMutatingAccessor;
```

Defined in: [packages/lit-query/src/useIsMutating.ts:147](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useIsMutating.ts#L147)

Creates a Lit reactive controller that tracks how many matching mutations are
currently pending.

When `filters` is a function, it is re-read during host updates so the count
can follow reactive host state. If `queryClient` is omitted, the controller
resolves the client from the nearest connected `QueryClientProvider`.

## Parameters

### host

`ReactiveControllerHost`

The Lit reactive controller host that owns the cache
subscription.

### filters

[`Accessor`](../type-aliases/Accessor.md)\<`MutationFilters`\<`unknown`, `Error`, `unknown`, `unknown`\>\> = `{}`

Mutation filters, or a getter that returns mutation filters.

### queryClient?

`QueryClient`

Optional explicit query client. Provide this for
controllers that should not resolve a client from Lit context.

## Returns

[`IsMutatingAccessor`](../type-aliases/IsMutatingAccessor.md)

An accessor for the current number of matching pending mutations.

## Example

```ts
import { LitElement, html } from 'lit'
import { useIsMutating } from '@tanstack/lit-query'

class MutationStatus extends LitElement {
  private readonly savesPending = useIsMutating(this, {
    mutationKey: ['save-project'],
  })

  render() {
    return html`<span>${this.savesPending()} saves pending</span>`
  }
}
```
