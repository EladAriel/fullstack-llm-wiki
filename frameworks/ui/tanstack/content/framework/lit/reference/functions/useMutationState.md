---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/useMutationState.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useMutationState
title: useMutationState
---

# Function: useMutationState()

```ts
function useMutationState<TResult>(
   host,
   options,
queryClient?): MutationStateAccessor<TResult>;
```

Defined in: [packages/lit-query/src/useMutationState.ts:187](https://github.com/TanStack/query/blob/main/packages/lit-query/src/useMutationState.ts#L187)

Creates a Lit reactive controller that selects state from matching mutations
in the mutation cache.

When `options.filters` is a function, it is re-read during host updates so
the selection can follow reactive host state. If `queryClient` is omitted,
the controller resolves the client from the nearest connected
`QueryClientProvider`.

## Type Parameters

### TResult

`TResult` = `MutationState`\<`unknown`, `unknown`, `unknown`, `unknown`\>

## Parameters

### host

`ReactiveControllerHost`

The Lit reactive controller host that owns the mutation cache
subscription.

### options

[`MutationStateOptions`](../type-aliases/MutationStateOptions.md)\<`TResult`\> = `{}`

Mutation state filters and optional selector.

### queryClient?

`QueryClient`

Optional explicit query client. Provide this for
controllers that should not resolve a client from Lit context.

## Returns

[`MutationStateAccessor`](../type-aliases/MutationStateAccessor.md)\<`TResult`\>

An accessor for the selected mutation state array.

## Example

```ts
import { LitElement, html } from 'lit'
import { useMutationState } from '@tanstack/lit-query'

class PendingUploads extends LitElement {
  private readonly uploads = useMutationState(this, {
    filters: { mutationKey: ['upload'], status: 'pending' },
    select: (mutation) => mutation.state.variables as File,
  })

  render() {
    return html`<span>${this.uploads().length} uploads pending</span>`
  }
}
```
