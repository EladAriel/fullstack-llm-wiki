---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/interfaces/InjectInfiniteQueryOptions.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: InjectInfiniteQueryOptions
title: InjectInfiniteQueryOptions
---

# Interface: InjectInfiniteQueryOptions

Defined in: [inject-infinite-query.ts:25](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-infinite-query.ts#L25)

## Properties

### injector?

```ts
optional injector: Injector;
```

Defined in: [inject-infinite-query.ts:31](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-infinite-query.ts#L31)

The `Injector` in which to create the infinite query.

If this is not provided, the current injection context will be used instead (via `inject`).
