---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/getDefaultQueryClient.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.386149Z"
---
# Getdefaultqueryclient

---
id: getDefaultQueryClient
title: getDefaultQueryClient
---

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
