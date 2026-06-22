---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-index-resource-lock.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB uses an optimized build process that obtains and holds an exclusive lock on the specified collection at the start and end of the index build. All subsequent operations on the collection must wait until |method| releases the exclusive lock. |method| allows interleaving read and write operations during the majority of the index build.

For more information on the locking behavior of |method|, see `index-operations`.
