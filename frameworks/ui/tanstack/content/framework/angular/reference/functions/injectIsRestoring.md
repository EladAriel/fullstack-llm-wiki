---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectIsRestoring.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: injectIsRestoring
title: injectIsRestoring
---

# Function: injectIsRestoring()

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
