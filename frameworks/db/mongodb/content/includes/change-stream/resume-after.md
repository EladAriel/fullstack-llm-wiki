---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/resume-after.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** You cannot use `resumeAfter` to resume a change stream after an
`invalidate event <change-event-invalidate>` (for example, a collection
drop or rename) closes the stream. Instead, you can use
`startAfter <change-stream-start-after>` to start a new change
stream after an `invalidate event <change-event-invalidate>`.
