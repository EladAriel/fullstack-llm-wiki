---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/find-getmore-partialresults.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If :dbcommand:`find` (or subsequent :dbcommand:`getMore` commands) returns partial results because the queried shard(s) aren't available, the `find output <cmd-find-output>` includes a `partialResultsReturned` indicator field. If the queried shards are available for the initial `find` command, but one or more shards become unavailable for subsequent `getMore` commands, only the `getMore` commands that run while the shards aren't available include `partialResultsReturned` in their output.
