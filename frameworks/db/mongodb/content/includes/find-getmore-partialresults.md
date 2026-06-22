---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/find-getmore-partialresults.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If :dbcommand:`find` (or subsequent :dbcommand:`getMore` commands) returns partial results because the queried shard(s) aren't available, the `find output <cmd-find-output>` includes a `partialResultsReturned` indicator field. If the queried shards are available for the initial `find` command, but one or more shards become unavailable for subsequent `getMore` commands, only the `getMore` commands that run while the shards aren't available include `partialResultsReturned` in their output.
