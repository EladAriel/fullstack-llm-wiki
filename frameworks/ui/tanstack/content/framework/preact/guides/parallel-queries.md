---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/guides/parallel-queries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: parallel-queries
title: Parallel Queries
ref: docs/framework/react/guides/parallel-queries.md
replace: { 'react-query': 'preact-query', 'React': 'Preact' }
---

[//]: # 'Info'

> When using Preact Query with compat's Suspense, this pattern of parallelism does not work, since the first query would throw a promise internally and would suspend the component before the other queries run. To get around this, you'll either need to use the `useSuspenseQueries` hook (which is suggested) or orchestrate your own parallelism with separate components for each `useSuspenseQuery` instance.

[//]: # 'Info'
