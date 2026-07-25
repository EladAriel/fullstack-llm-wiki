---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/hints-precedence.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Cluster query settings take precedence over query settings or index hints passed as a command field. MongoDB ignores index hints in command fields if a matching query setting already contains index hints.

Index hints don't affect `query shape <query-shapes>`.

For more information about hints and query settings, see `Query Settings Syntax <setQuerySettings-syntax>`.
