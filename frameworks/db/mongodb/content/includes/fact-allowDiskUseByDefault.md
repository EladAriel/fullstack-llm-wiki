---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-allowDiskUseByDefault.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Pipeline stages that require more than 100 megabytes of memory to execute write temporary files to disk by default. These temporary files last for the duration of the pipeline execution and can influence storage space on your instance.

Individual `find` and `aggregate` commands can override the :parameter:`allowDiskUseByDefault` parameter by either:

- Using `{ allowDiskUse: true }` to allow writing temporary files out
to disk when `allowDiskUseByDefault` is set to `false`

- Using `{ allowDiskUse: false }` to prohibit writing temporary files
out to disk when `allowDiskUseByDefault` is set to `true`
