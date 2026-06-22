---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fsync-lock-command.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** Servers maintain an fsync lock count.  The :dbcommand:`fsync` command with
the `lock` field set to `true` increments the lock count while the
:dbcommand:`fsyncUnlock` command decrements it. To enable writes on a locked
server or cluster, call the :dbcommand:`fsyncUnlock` command until the lock
count reaches zero.
