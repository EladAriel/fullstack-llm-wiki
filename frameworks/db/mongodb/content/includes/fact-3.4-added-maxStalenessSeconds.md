---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-3.4-added-maxStalenessSeconds.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB supports the `maxStalenessSeconds </core/read-preference-staleness>` read preference option. The `maxStalenessSeconds` option lets you specify a maximum replication lag, or "staleness", that `secondaries <secondary>` can have and still be eligible for read operations. When a secondary's estimated staleness exceeds `maxStalenessSeconds`, the secondary becomes ineligible for read operations.
