---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-drop-index-5.2.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.2, you can use |drop-index| to drop existing indexes on the same collection even if there is a build in progress on another index. In earlier versions, attempting to drop a different index during an in-progress index build results in a `BackgroundOperationInProgressForNamespace` error.
