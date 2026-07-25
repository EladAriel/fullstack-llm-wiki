---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/serverStatus/details-noneInfo.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Number of non-transaction query operations that use default write concerns. The metrics track usage of the :dbcommand:`cluster wide write concern <setDefaultRWConcern>` (the global default write concern) and the implicit-default write concern.

The sum of the values in `opWriteConcernCounters.noneInfo` should equal the value of `opWriteConcernCounters.none`.
