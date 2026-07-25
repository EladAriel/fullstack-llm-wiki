---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-multikey-index-sort-limitation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When you sort based on an array field that is indexed with a `multikey index <index-type-multikey>`, the query plan includes an `in-memory sort` stage unless both of the following are true:

- The index `boundaries <multikey-index-bounds-intersecting>` for
all sort fields are `[MinKey, MaxKey]`.

- No boundaries for any multikey-indexed field have the same path prefix
as the sort pattern.
