---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/defragment-sharded-collections-conditions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Fragmentation is where a sharded collection's data is broken up into an unnecessarily large number of small chunks. This can increase operation times of CRUD operations run on that collection. Defragmentation reduces the number of chunks by merging smaller chunks into larger ones, resulting in lower CRUD operation times.

If CRUD operation times are acceptable, you don't need to defragment collections.

The following table summarizes defragmentation information for various MongoDB versions.
