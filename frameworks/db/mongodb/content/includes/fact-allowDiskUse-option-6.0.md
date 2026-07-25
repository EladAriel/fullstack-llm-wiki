---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-allowDiskUse-option-6.0.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Use this option to override :parameter:`allowDiskUseByDefault` for a specific query. You can use this option to either:

- Prohibit disk use on a system where disk use is allowed by
default.

- Allow disk use on a system where disk use is prohibited by
default.

Starting in MongoDB 6.0, if :parameter:`allowDiskUseByDefault` is set to `true` and the server requires more than 100 megabytes of memory for a pipeline execution stage, MongoDB automatically writes temporary files to disk unless the query specifies `{ allowDiskUse: false }`.

For details, see :parameter:`allowDiskUseByDefault`.
