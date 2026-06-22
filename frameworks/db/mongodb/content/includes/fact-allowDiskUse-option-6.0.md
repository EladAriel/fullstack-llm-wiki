---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-allowDiskUse-option-6.0.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Use this option to override :parameter:`allowDiskUseByDefault` for a specific query. You can use this option to either:

- Prohibit disk use on a system where disk use is allowed by
default.

- Allow disk use on a system where disk use is prohibited by
default.

Starting in MongoDB 6.0, if :parameter:`allowDiskUseByDefault` is set to `true` and the server requires more than 100 megabytes of memory for a pipeline execution stage, MongoDB automatically writes temporary files to disk unless the query specifies `{ allowDiskUse: false }`.

For details, see :parameter:`allowDiskUseByDefault`.
