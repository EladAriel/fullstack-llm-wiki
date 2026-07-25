---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/defragment-sharded-collections-conditions.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Fragmentation is where a sharded collection's data is broken up into an unnecessarily large number of small chunks. This can increase operation times of CRUD operations run on that collection. Defragmentation reduces the number of chunks by merging smaller chunks into larger ones, resulting in lower CRUD operation times.

If CRUD operation times are acceptable, you don't need to defragment collections.

The following table summarizes defragmentation information for various MongoDB versions.
