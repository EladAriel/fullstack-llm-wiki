---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-collection-namespace-limit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The namespace length limit for unsharded collections and views is 255 bytes, and 235 bytes for sharded collections. For a collection or a view, the namespace includes the database name, the dot (`.`) separator, and the collection/view name (e.g. `<database>.<collection>`).
