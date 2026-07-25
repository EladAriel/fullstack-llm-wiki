---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-mongod-mongos-ftdc-thread.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:binary:`~bin.mongod` includes a `Full Time Diagnostic Data Capture <ftdc-stub>` mechanism to assist MongoDB engineers with troubleshooting deployments. If this thread fails, it terminates the originating process. To avoid the most common failures, confirm that the user running the process has permissions to create the FTDC `diagnostic.data` directory. For `mongod` the directory is within :setting:`storage.dbPath`. For `mongos` it is parallel to :setting:`systemLog.path`.
