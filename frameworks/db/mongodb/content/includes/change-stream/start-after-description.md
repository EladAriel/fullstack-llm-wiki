---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/start-after-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. Specifies a `resume token <change-stream-resume>` as the logical starting point for the change stream. Unlike `resumeAfter`, `startAfter` can resume notifications after an `invalidate` event by creating a new change stream.

`startAfter` is mutually exclusive with `resumeAfter` and `startAtOperationTime`.
