---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/batch-size-aggregate.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The `{ cursor: { batchSize: 0 } }` document, which specifies the size of the initial batch size, indicates an empty first batch. This batch size is useful for quickly returning a cursor or failure message without doing significant server-side work.

To specify batch size for subsequent :dbcommand:`getMore` operations (after the initial batch), use the `batchSize` field when running the :dbcommand:`getMore` command.
