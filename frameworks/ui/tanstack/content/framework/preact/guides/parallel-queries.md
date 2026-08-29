---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/guides/parallel-queries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.370959Z"
---
# Parallel Queries

---
id: parallel-queries
title: Parallel Queries
ref: docs/framework/react/guides/parallel-queries.md
replace: { 'react-query': 'preact-query', 'React': 'Preact' }
---

[//]: # 'Info'

> When using Preact Query with compat's Suspense, this pattern of parallelism does not work, since the first query would throw a promise internally and would suspend the component before the other queries run. To get around this, you'll either need to use the `useSuspenseQueries` hook (which is suggested) or orchestrate your own parallelism with separate components for each `useSuspenseQuery` instance.

[//]: # 'Info'
