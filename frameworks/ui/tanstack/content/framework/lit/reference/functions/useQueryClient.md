---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/useQueryClient.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: useQueryClient
title: useQueryClient
---

# Function: useQueryClient()

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
