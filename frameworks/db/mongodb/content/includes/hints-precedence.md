---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/hints-precedence.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Cluster query settings take precedence over query settings or index hints passed as a command field. MongoDB ignores index hints in command fields if a matching query setting already contains index hints.

Index hints don't affect `query shape <query-shapes>`.

For more information about hints and query settings, see `Query Settings Syntax <setQuerySettings-syntax>`.
