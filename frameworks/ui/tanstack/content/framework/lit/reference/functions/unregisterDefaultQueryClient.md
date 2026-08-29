---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/unregisterDefaultQueryClient.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.386297Z"
---
# Unregisterdefaultqueryclient

---
id: unregisterDefaultQueryClient
title: unregisterDefaultQueryClient
---

```ts
function unregisterDefaultQueryClient(client): void;
```

Defined in: [packages/lit-query/src/context.ts:45](https://github.com/TanStack/query/blob/main/packages/lit-query/src/context.ts#L45)

Unregisters a client previously registered with
`registerDefaultQueryClient`.

`QueryClientProvider` calls this automatically when it disconnects.

## Parameters

### client

`QueryClient`

The query client registration to release.

## Returns

`void`
