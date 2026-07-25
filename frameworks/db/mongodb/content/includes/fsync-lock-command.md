---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fsync-lock-command.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Important:** Servers maintain an fsync lock count.  The :dbcommand:`fsync` command with
the `lock` field set to `true` increments the lock count while the
:dbcommand:`fsyncUnlock` command decrements it. To enable writes on a locked
server or cluster, call the :dbcommand:`fsyncUnlock` command until the lock
count reaches zero.
