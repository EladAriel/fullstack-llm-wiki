---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/serverStatus/details-noneInfo.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Number of non-transaction query operations that use default write concerns. The metrics track usage of the :dbcommand:`cluster wide write concern <setDefaultRWConcern>` (the global default write concern) and the implicit-default write concern.

The sum of the values in `opWriteConcernCounters.noneInfo` should equal the value of `opWriteConcernCounters.none`.
