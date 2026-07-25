---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/getDefaultQueryClient.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
