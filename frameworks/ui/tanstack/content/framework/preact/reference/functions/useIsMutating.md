---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useIsMutating.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.374686Z"
---
# Useismutating

---
id: useIsMutating
title: useIsMutating
---

```ts
function useIsMutating(filters?, queryClient?): number;
```

Defined in: [preact-query/src/useMutationState.ts:33](https://github.com/TanStack/query/blob/main/packages/preact-query/src/useMutationState.ts#L33)

`useIsMutating` is an optional hook that returns the `number` of mutations that your application is fetching
(useful for app-wide loading indicators).

## Parameters

### filters?

`MutationFilters`\<`unknown`, `Error`, `unknown`, `unknown`\>

The MutationFilters to narrow down the matched mutations.

### queryClient?

`QueryClient`

Use this to use a custom `QueryClient`. Otherwise, the one from the nearest context will
be used.

## Returns

`number`

Will be the `number` of the mutations that your application is currently fetching.

## Example

```tsx
import { useIsMutating } from '@tanstack/preact-query'

// How many mutations are fetching?
const isMutating = useIsMutating()
// How many mutations matching the posts prefix are fetching?
const isMutatingPosts = useIsMutating({ mutationKey: ['posts'] })
```
