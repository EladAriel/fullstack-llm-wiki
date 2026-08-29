---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/interfaces/InjectIsFetchingOptions.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.428443Z"
---
# Injectisfetchingoptions

---
id: InjectIsFetchingOptions
title: InjectIsFetchingOptions
---

Defined in: [inject-is-fetching.ts:13](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-is-fetching.ts#L13)

## Properties

### injector?

```ts
optional injector: Injector;
```

Defined in: [inject-is-fetching.ts:19](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-is-fetching.ts#L19)

The `Injector` in which to create the isFetching signal.

If this is not provided, the current injection context will be used instead (via `inject`).
