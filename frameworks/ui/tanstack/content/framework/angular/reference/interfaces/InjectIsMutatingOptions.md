---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/interfaces/InjectIsMutatingOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: InjectIsMutatingOptions
title: InjectIsMutatingOptions
---

# Interface: InjectIsMutatingOptions

Defined in: [inject-is-mutating.ts:13](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-is-mutating.ts#L13)

## Properties

### injector?

```ts
optional injector: Injector;
```

Defined in: [inject-is-mutating.ts:19](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-is-mutating.ts#L19)

The `Injector` in which to create the isMutating signal.

If this is not provided, the current injection context will be used instead (via `inject`).
