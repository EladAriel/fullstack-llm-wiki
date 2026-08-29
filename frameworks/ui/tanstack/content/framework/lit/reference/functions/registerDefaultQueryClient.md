---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/registerDefaultQueryClient.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.386996Z"
---
# Registerdefaultqueryclient

---
id: registerDefaultQueryClient
title: registerDefaultQueryClient
---

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
