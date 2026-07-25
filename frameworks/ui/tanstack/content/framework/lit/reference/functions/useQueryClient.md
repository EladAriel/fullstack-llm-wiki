---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/useQueryClient.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
