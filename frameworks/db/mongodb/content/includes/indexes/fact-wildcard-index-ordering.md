---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/fact-wildcard-index-ordering.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 6.3, 6.0.5, and 5.0.16, the `wildcardProjection` field stores the index projection in its submitted form. Earlier versions of the server may have stored the projection in a normalized form.

The server uses the index the same way, but you may notice a difference in the output of the :dbcommand:`listIndexes` and :method:`db.collection.getIndexes()` commands.
