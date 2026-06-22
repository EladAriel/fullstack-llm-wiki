---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/resume-after-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. Specifies a `resume token <change-stream-resume>` as the logical starting point for the change stream. Cannot be used to resume the change stream after an `invalidate` event.

`resumeAfter` is mutually exclusive with `startAfter` and `startAtOperationTime`.
