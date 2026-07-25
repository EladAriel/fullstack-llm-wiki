---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-collection-namespace-limit.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The namespace length limit for unsharded collections and views is 255 bytes, and 235 bytes for sharded collections. For a collection or a view, the namespace includes the database name, the dot (`.`) separator, and the collection/view name (e.g. `<database>.<collection>`).
