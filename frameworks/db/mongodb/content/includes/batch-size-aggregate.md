---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/batch-size-aggregate.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The `{ cursor: { batchSize: 0 } }` document, which specifies the size of the initial batch size, indicates an empty first batch. This batch size is useful for quickly returning a cursor or failure message without doing significant server-side work.

To specify batch size for subsequent :dbcommand:`getMore` operations (after the initial batch), use the `batchSize` field when running the :dbcommand:`getMore` command.
