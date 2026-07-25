---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/registerDefaultQueryClient.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
