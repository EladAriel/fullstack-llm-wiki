---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useIsFetching.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.374841Z"
---
# Useisfetching

---
id: useIsFetching
title: useIsFetching
---

```ts
function useIsFetching(filters?, queryClient?): number;
```

Defined in: [preact-query/src/useIsFetching.ts:42](https://github.com/TanStack/query/blob/main/packages/preact-query/src/useIsFetching.ts#L42)

`useIsFetching` is an optional hook that returns the `number` of the queries that your application is loading or
fetching in the background (useful for app-wide loading indicators).

## Parameters

### filters?

`QueryFilters`\<readonly `unknown`[]\>

The QueryFilters to narrow down the matched queries.

### queryClient?

`QueryClient`

Use this to use a custom `QueryClient`. Otherwise, the one from the nearest context will
be used.

## Returns

`number`

Will be the `number` of the queries that your application is currently loading or fetching in the
background.

## Examples

```tsx
import { useIsFetching } from '@tanstack/preact-query'

// How many queries are fetching?
const isFetching = useIsFetching()
// How many queries matching the posts prefix are fetching?
const isFetchingPosts = useIsFetching({ queryKey: ['posts'] })
```

A global loading indicator for any query fetching in the background, not just the ones on screen:
```tsx
import { useIsFetching } from '@tanstack/preact-query'

function GlobalLoadingIndicator() {
  const isFetching = useIsFetching()

  return isFetching ? (
    <div>Queries are fetching in the background...</div>
  ) : null
}
```
