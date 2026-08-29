---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/resolveQueryClient.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.385693Z"
---
# Resolvequeryclient

---
id: resolveQueryClient
title: resolveQueryClient
---

```ts
function resolveQueryClient(explicit?): QueryClient;
```

Defined in: [packages/lit-query/src/context.ts:118](https://github.com/TanStack/query/blob/main/packages/lit-query/src/context.ts#L118)

Resolves an explicit `QueryClient` or falls back to `useQueryClient`.

## Parameters

### explicit?

`QueryClient`

Optional client supplied by the caller.

## Returns

`QueryClient`

The explicit client when provided, otherwise the current default
client.
