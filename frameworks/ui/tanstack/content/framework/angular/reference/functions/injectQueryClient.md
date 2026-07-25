---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectQueryClient.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: injectQueryClient
title: injectQueryClient
---

# ~~Function: injectQueryClient()~~

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
