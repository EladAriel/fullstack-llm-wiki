---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/index-tutorials-considerations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

During index builds, applications may encounter reduced performance or limited read/write access to the collection being indexed.

For more information on the index build process, see `index-operations`, especially the `index-operations-replicated-build` section.

Some drivers use `Long(1)` instead of `1` to specify the index order. The resulting indexes are the same.
