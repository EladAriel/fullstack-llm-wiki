---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-read-concern-latency.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, :readconcern:`"local"` is the default read concern level for read operations against the primary and secondaries. In MongoDB 4.4, queries targeting sharded cluster secondaries use read concern :readconcern:`"available"` and can return `orphaned documents <orphaned document>`.

This may introduce a significant latency increase for count queries that use a filter and for `covered queries <covered-queries>`.

You can opt out of this behavior by setting the cluster-wide `read concern <read-concern>` with :dbcommand:`setDefaultRWConcern`.
