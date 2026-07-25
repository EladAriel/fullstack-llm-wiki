---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-index-resource-lock.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB uses an optimized build process that obtains and holds an exclusive lock on the specified collection at the start and end of the index build. All subsequent operations on the collection must wait until |method| releases the exclusive lock. |method| allows interleaving read and write operations during the majority of the index build.

For more information on the locking behavior of |method|, see `index-operations`.
