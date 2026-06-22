---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/resume-after.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** You cannot use `resumeAfter` to resume a change stream after an
`invalidate event <change-event-invalidate>` (for example, a collection
drop or rename) closes the stream. Instead, you can use
`startAfter <change-stream-start-after>` to start a new change
stream after an `invalidate event <change-event-invalidate>`.
