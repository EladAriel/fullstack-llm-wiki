---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-dropindexes-inprog.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The :method:`db.collection.dropIndexes()` command cannot drop `ready indexes <index-build-process-ready>` if there are any in-progress index builds.

- In versions 4.4.0-4.4.4 of MongoDB, this logic was not true
due to a bug.
