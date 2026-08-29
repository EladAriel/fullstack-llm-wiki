---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/HydrationBoundary.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.375704Z"
---
# Hydrationboundary

---
id: HydrationBoundary
title: HydrationBoundary
---

```ts
function HydrationBoundary(__namedParameters): Element;
```

Defined in: [preact-query/src/HydrationBoundary.tsx:87](https://github.com/TanStack/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L87)

`HydrationBoundary` adds a previously dehydrated state into the `queryClient` that would be returned by
`useQueryClient()`. If the client already contains data, the new queries will be intelligently merged based on
update timestamp.

Note: Only `queries` can be dehydrated with an `HydrationBoundary`.

## Parameters

### \_\_namedParameters

[`HydrationBoundaryProps`](../interfaces/HydrationBoundaryProps.md)

## Returns

`Element`

The provided `children`, rendered unconditionally. New queries in `state` are hydrated into the
cache during render; for queries already in the cache, only newer dehydrated data is hydrated, in an effect
after commit.

## Examples

```tsx
import { HydrationBoundary } from '@tanstack/preact-query'

function App() {
  return <HydrationBoundary state={dehydratedState}>...</HydrationBoundary>
}
```

Server-side prefetch handed off to the client via `dehydrate`:
```tsx
import { HydrationBoundary, dehydrate, noop } from '@tanstack/preact-query'

async function ServerComponent() {
  const queryClient = getQueryClient()

  await queryClient
    .query({
      queryKey: ['posts'],
      queryFn: fetchPosts,
    })
    .catch(noop)

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Posts />
    </HydrationBoundary>
  )
}
```
