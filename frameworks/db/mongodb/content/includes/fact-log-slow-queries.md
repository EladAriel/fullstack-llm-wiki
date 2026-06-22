---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-log-slow-queries.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When :parameter:`logLevel` is set to `0`, MongoDB records slow operations to the diagnostic log at a rate determined by :setting:`~operationProfiling.slowOpSampleRate`.

At higher :parameter:`logLevel` settings, all operations appear in the diagnostic log regardless of their latency with the following exception: the logging of slow oplog entry messages by the secondaries. The secondaries log only the slow oplog entries; increasing the :parameter:`logLevel` does not log all oplog entries.
