---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-session-timeout.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The time in minutes that a `session <sessions>` remains active after its most recent use. Sessions that have not received a new read/write operation from the client or been refreshed with :dbcommand:`refreshSessions` within this threshold are cleared from the cache. State associated with an expired session may be cleaned up by the server at any time.
