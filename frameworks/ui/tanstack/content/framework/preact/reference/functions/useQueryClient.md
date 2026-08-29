---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useQueryClient.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.373306Z"
---
# Usequeryclient

---
id: useQueryClient
title: useQueryClient
---

```ts
function useQueryClient(queryClient?): QueryClient;
```

Defined in: [preact-query/src/QueryClientProvider.tsx:21](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryClientProvider.tsx#L21)

The `useQueryClient` hook returns the current `QueryClient` instance.

## Parameters

### queryClient?

`QueryClient`

Use this to use a custom `QueryClient`. Otherwise, the one from the nearest context will
be used.

## Returns

`QueryClient`

The current `QueryClient` instance.

## Throws

If no `queryClient` argument is passed and no `QueryClientProvider` is found in the component tree.
