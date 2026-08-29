---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/provideIsRestoring.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.423944Z"
---
# Provideisrestoring

---
id: provideIsRestoring
title: provideIsRestoring
---

```ts
function provideIsRestoring(isRestoring): Provider;
```

Defined in: [inject-is-restoring.ts:43](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-is-restoring.ts#L43)

Used by TanStack Query Angular persist client plugin to provide the signal that tracks the restore state

## Parameters

### isRestoring

`Signal`\<`boolean`\>

a readonly signal that returns a boolean

## Returns

`Provider`

Provider for the `isRestoring` signal
