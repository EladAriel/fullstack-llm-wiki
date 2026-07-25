---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-3.4-added-maxStalenessSeconds.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB supports the `maxStalenessSeconds </core/read-preference-staleness>` read preference option. The `maxStalenessSeconds` option lets you specify a maximum replication lag, or "staleness", that `secondaries <secondary>` can have and still be eligible for read operations. When a secondary's estimated staleness exceeds `maxStalenessSeconds`, the secondary becomes ineligible for read operations.
