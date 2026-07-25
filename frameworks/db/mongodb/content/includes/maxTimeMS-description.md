---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/maxTimeMS-description.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Specifies a time limit in milliseconds. If you do not specify a value for `maxTimeMS`, operations will not time out. A value of `0` explicitly specifies the default unbounded behavior.

MongoDB terminates operations that exceed their allotted time limit using the same mechanism as :method:`db.killOp()`. MongoDB only terminates an operation at one of its designated `interrupt points <interrupt point>`.
