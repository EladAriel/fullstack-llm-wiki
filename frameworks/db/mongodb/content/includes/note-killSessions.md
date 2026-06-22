---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-killSessions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### In-progress Operations

Killing a session kills any in-progress operations in the session and closes any open cursors associated with these operations.

### Killed Session Availability

The killed session may still be listed as a current session, and future operations may use the killed session. To view existing sessions, see :pipeline:`$listSessions` operation or :pipeline:`$listLocalSessions`.

### Sessions with Transactions in Prepared State

The |command| operation ignores sessions that have `transactions` in prepared state. Transactions in prepared state refer to transactions with write operations that span multiple shards whose commit coordinator has completed the `"sendingPrepare" action <$currentOp.twoPhaseCommitCoordinator.action>`.
