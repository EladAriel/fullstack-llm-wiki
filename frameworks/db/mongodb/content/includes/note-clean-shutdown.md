---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-clean-shutdown.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** If you do not perform a clean shut down, errors may result that
prevent the :binary:`~bin.mongod` process from starting.
Forcibly terminating the :binary:`~bin.mongod` process may cause
inaccurate results for :method:`db.collection.count()` and
:method:`db.stats()`. It may also lengthen startup time the next time
that the :binary:`~bin.mongod` process is restarted.
This applies whether you attempt to terminate the
:binary:`~bin.mongod` process from the command line via `kill` or
similar, or whether you use your platform's initialization system to
issue a `stop` command, like `sudo systemctl stop mongod` or
`sudo service mongod stop`.
