---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/important-defaults.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: important-defaults
title: Important Defaults
ref: docs/framework/react/guides/important-defaults.md
---

[//]: # 'StructuralSharing'

- Query results by default are **structurally shared to detect if data has actually changed** and if not, **the data reference remains unchanged** to better help with value stabilization. If this concept sounds foreign, then don't worry about it! 99.9% of the time you will not need to disable this and it makes your app more performant at zero cost to you.

[//]: # 'StructuralSharing'
[//]: # 'Materials'
[//]: # 'Materials'
