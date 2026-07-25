---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/return-commit-decision-parameter.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The server parameter :parameter:`coordinateCommitReturnImmediatelyAfterPersistingDecision` controls when transaction commit decisions are returned to the client.

The parameter was introduced in MongDB 5.0 with a default value of `true`. In MongoDB 6.1 the default value changes to `false`.

When `coordinateCommitReturnImmediatelyAfterPersistingDecision` is `false`, the `shard <shards-concepts>` transaction coordinator waits for all members to acknowledge a `transaction <transactions-atomicity>` commit before returning the commit decision to the client.
