---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/wildcard-projection-specifications.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

`wildcardProjection` works with specifications like:

However, you can't define an index that includes the same field in the wildcard fields and the regular (non-wildcard) fields. To define the index correctly, use a `wildcardProjection` to exclude duplicated fields from the wildcard pattern.

`wildcardProjection` does not work with a specification like:
