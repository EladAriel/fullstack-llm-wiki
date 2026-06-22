---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/index-tutorials-considerations.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

During index builds, applications may encounter reduced performance or limited read/write access to the collection being indexed.

For more information on the index build process, see `index-operations`, especially the `index-operations-replicated-build` section.

Some drivers use `Long(1)` instead of `1` to specify the index order. The resulting indexes are the same.
