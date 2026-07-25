---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/functions/resolveQueryClient.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: resolveQueryClient
title: resolveQueryClient
---

# Function: resolveQueryClient()

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
