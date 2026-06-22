---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/maxTimeMS-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Specifies a time limit in milliseconds. If you do not specify a value for `maxTimeMS`, operations will not time out. A value of `0` explicitly specifies the default unbounded behavior.

MongoDB terminates operations that exceed their allotted time limit using the same mechanism as :method:`db.killOp()`. MongoDB only terminates an operation at one of its designated `interrupt points <interrupt point>`.
