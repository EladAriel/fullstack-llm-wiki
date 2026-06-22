---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/getDefaultQueryClient.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: getDefaultQueryClient
title: getDefaultQueryClient
---

# Function: getDefaultQueryClient()

```ts
function getDefaultQueryClient(): QueryClient | undefined;
```

Defined in: [packages/lit-query/src/context.ts:72](https://github.com/TanStack/query/blob/main/packages/lit-query/src/context.ts#L72)

Returns the registered default `QueryClient`, if exactly one default client is
available.

## Returns

`QueryClient` \| `undefined`

The default query client, or `undefined` when there is no registered
client or more than one registered client.
