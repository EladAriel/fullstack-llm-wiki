---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-drop-index-5.2.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.2, you can use |drop-index| to drop existing indexes on the same collection even if there is a build in progress on another index. In earlier versions, attempting to drop a different index during an in-progress index build results in a `BackgroundOperationInProgressForNamespace` error.
