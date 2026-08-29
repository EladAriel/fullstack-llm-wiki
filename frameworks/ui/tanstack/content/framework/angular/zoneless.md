---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/zoneless.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.364021Z"
---
# Zoneless

---
id: zoneless
title: Zoneless Angular
---

Because the Angular adapter for TanStack Query is built on signals, it fully supports Zoneless!

Among Zoneless benefits are improved performance and debugging experience. For details see the [Angular documentation](https://angular.dev/guide/zoneless).

> Besides Zoneless, ZoneJS change detection is also fully supported.

> When using Zoneless, ensure you are on Angular v19 or later to take advantage of the `PendingTasks` integration that keeps `ApplicationRef.whenStable()` in sync with ongoing queries and mutations.
