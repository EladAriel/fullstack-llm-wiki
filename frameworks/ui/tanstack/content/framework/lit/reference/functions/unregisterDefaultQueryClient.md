---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/unregisterDefaultQueryClient.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: unregisterDefaultQueryClient
title: unregisterDefaultQueryClient
---

# Function: unregisterDefaultQueryClient()

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
