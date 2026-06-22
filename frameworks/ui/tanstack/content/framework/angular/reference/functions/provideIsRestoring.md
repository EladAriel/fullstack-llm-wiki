---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/provideIsRestoring.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: provideIsRestoring
title: provideIsRestoring
---

# Function: provideIsRestoring()

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
