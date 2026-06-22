---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/compound-and-partial-indexes.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For a compound index that includes `2dsphere` index keys and keys for other types, only the `2dsphere` index fields determine whether the index references a document.

`Partial indexes <index-type-partial>` have a superset of the sparse index functionality. Unless your application has a specific requirement, use partial indexes instead of sparse indexes.
