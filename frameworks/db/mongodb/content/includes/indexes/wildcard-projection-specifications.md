---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/wildcard-projection-specifications.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`wildcardProjection` works with specifications like:

However, you can't define an index that includes the same field in the wildcard fields and the regular (non-wildcard) fields. To define the index correctly, use a `wildcardProjection` to exclude duplicated fields from the wildcard pattern.

`wildcardProjection` does not work with a specification like:
