---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectIsRestoring.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
