---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/useQueryClient.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.385054Z"
---
# Usequeryclient

---
id: useQueryClient
title: useQueryClient
---

```ts
function useQueryClient(): QueryClient;
```

Defined in: [packages/lit-query/src/context.ts:98](https://github.com/TanStack/query/blob/main/packages/lit-query/src/context.ts#L98)

Resolves the current default `QueryClient` registered by a connected
`QueryClientProvider`.

This helper is useful outside a Lit reactive controller when a single
provider is mounted. It throws if no client is registered or if multiple
clients are mounted and the default would be ambiguous.

## Returns

`QueryClient`

The single registered query client.
