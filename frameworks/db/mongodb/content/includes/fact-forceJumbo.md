---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-forceJumbo.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:red:`WARNING:`

The |cmd| command with `forceJumbo=true` blocks write operations on the collection.

This option causes the shard to migrate chunks even when they are larger than the configured chunk size. The collection remains unavailable for writes for the duration of the migration.

To migrate these large chunks without this long blocking period, see `balance-chunks-that-exceed-size-limit` instead.
