---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/fact-wildcard-index-ordering.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 6.3, 6.0.5, and 5.0.16, the `wildcardProjection` field stores the index projection in its submitted form. Earlier versions of the server may have stored the projection in a normalized form.

The server uses the index the same way, but you may notice a difference in the output of the :dbcommand:`listIndexes` and :method:`db.collection.getIndexes()` commands.
