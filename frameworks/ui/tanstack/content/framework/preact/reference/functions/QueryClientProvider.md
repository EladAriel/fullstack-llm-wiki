---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/QueryClientProvider.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.374338Z"
---
# Queryclientprovider

---
id: QueryClientProvider
title: QueryClientProvider
---

```ts
function QueryClientProvider(__namedParameters): VNode;
```

Defined in: [preact-query/src/QueryClientProvider.tsx:70](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryClientProvider.tsx#L70)

Use the `QueryClientProvider` component to connect and provide a `QueryClient` to your application. Also
calls `client.mount()`/`client.unmount()` as this component mounts/unmounts, which subscribes the client to
focus/online events (resuming any paused mutations and refetching as needed when the app regains focus or
comes back online).

## Parameters

### \_\_namedParameters

[`QueryClientProviderProps`](../type-aliases/QueryClientProviderProps.md)

## Returns

`VNode`

The provided `children`, wrapped so they can read the `QueryClient` via `useQueryClient`.

## Example

```tsx
import { QueryClient, QueryClientProvider } from '@tanstack/preact-query'

const queryClient = new QueryClient()

function App() {
  return <QueryClientProvider client={queryClient}>...</QueryClientProvider>
}
```
