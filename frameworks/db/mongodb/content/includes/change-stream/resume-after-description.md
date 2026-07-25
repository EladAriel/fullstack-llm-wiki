---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/resume-after-description.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. Specifies a `resume token <change-stream-resume>` as the logical starting point for the change stream. Cannot be used to resume the change stream after an `invalidate` event.

`resumeAfter` is mutually exclusive with `startAfter` and `startAtOperationTime`.
