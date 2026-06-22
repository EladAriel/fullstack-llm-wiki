---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-multikey-index-sort-limitation.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you sort based on an array field that is indexed with a `multikey index <index-type-multikey>`, the query plan includes an `in-memory sort` stage unless both of the following are true:

- The index `boundaries <multikey-index-bounds-intersecting>` for
all sort fields are `[MinKey, MaxKey]`.

- No boundaries for any multikey-indexed field have the same path prefix
as the sort pattern.
