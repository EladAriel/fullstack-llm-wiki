---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/interfaces/InjectMutationStateOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: InjectMutationStateOptions
title: InjectMutationStateOptions
---

# Interface: InjectMutationStateOptions

Defined in: [inject-mutation-state.ts:45](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-mutation-state.ts#L45)

## Properties

### injector?

```ts
optional injector: Injector;
```

Defined in: [inject-mutation-state.ts:51](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-mutation-state.ts#L51)

The `Injector` in which to create the mutation state signal.

If this is not provided, the current injection context will be used instead (via `inject`).
