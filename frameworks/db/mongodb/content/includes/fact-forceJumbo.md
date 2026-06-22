---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-forceJumbo.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:red:`WARNING:`

The |cmd| command with `forceJumbo=true` blocks write operations on the collection.

This option causes the shard to migrate chunks even when they are larger than the configured chunk size. The collection remains unavailable for writes for the duration of the migration.

To migrate these large chunks without this long blocking period, see `balance-chunks-that-exceed-size-limit` instead.
