---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/registerDefaultQueryClient.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: registerDefaultQueryClient
title: registerDefaultQueryClient
---

# Function: registerDefaultQueryClient()

```ts
function registerDefaultQueryClient(client): void;
```

Defined in: [packages/lit-query/src/context.ts:32](https://github.com/TanStack/query/blob/main/packages/lit-query/src/context.ts#L32)

Registers a `QueryClient` as a process-local fallback for APIs that resolve a
client without an explicit argument.

`QueryClientProvider` calls this automatically while it is connected. Prefer
passing an explicit client or rendering under a provider when possible.

## Parameters

### client

`QueryClient`

The query client to register as the current default.

## Returns

`void`
