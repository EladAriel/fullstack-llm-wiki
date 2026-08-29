---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectQueryClient.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.422301Z"
---
# Injectqueryclient

---
id: injectQueryClient
title: injectQueryClient
---

```ts
function injectQueryClient(injectOptions): QueryClient;
```

Defined in: [inject-query-client.ts:18](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-query-client.ts#L18)

Injects a `QueryClient` instance and allows passing a custom injector.

## Parameters

### injectOptions

`InjectOptions` & `object` = `{}`

Type of the options argument to inject and optionally a custom injector.

## Returns

`QueryClient`

The `QueryClient` instance.

## Deprecated

Use `inject(QueryClient)` instead.
If you need to get a `QueryClient` from a custom injector, use `injector.get(QueryClient)`.

**Example**
```ts
const queryClient = injectQueryClient();
```
