---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectIsRestoring.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.423490Z"
---
# Injectisrestoring

---
id: injectIsRestoring
title: injectIsRestoring
---

```ts
function injectIsRestoring(options?): Signal<boolean>;
```

Defined in: [inject-is-restoring.ts:32](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-is-restoring.ts#L32)

Injects a signal that tracks whether a restore is currently in progress. [injectQuery](injectQuery.md) and friends also check this internally to avoid race conditions between the restore and initializing queries.

## Parameters

### options?

`InjectIsRestoringOptions`

Options for injectIsRestoring.

## Returns

`Signal`\<`boolean`\>

readonly signal with boolean that indicates whether a restore is in progress.
