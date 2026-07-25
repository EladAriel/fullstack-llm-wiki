---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-stop-in-progress-index-builds.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If an index specified to |drop-index| is still building, |drop-index| attempts to stop the in-progress build. Stopping an index build has the same effect as dropping the built index.

For replica sets, run |drop-index| on the `primary`. The primary stops the index build and creates an associated "abortIndexBuild" `oplog` entry. Secondaries which replicate the "abortIndexBuild" oplog entry stop the in-progress index build and discard the build job. See `index-build-process` for detailed documentation on the index build process.

Use :dbcommand:`currentOp` to identify the index builds associated with a :dbcommand:`createIndexes` or :method:`db.collection.createIndexes()` operation. See `currentOp-cmd-index-creation` for an example.
