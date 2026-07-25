---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-dropindexes-inprog.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The :method:`db.collection.dropIndexes()` command cannot drop `ready indexes <index-build-process-ready>` if there are any in-progress index builds.

- In versions 4.4.0-4.4.4 of MongoDB, this logic was not true
due to a bug.
