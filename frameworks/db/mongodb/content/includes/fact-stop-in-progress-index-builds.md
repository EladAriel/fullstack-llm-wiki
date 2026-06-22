---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-stop-in-progress-index-builds.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If an index specified to |drop-index| is still building, |drop-index| attempts to stop the in-progress build. Stopping an index build has the same effect as dropping the built index.

For replica sets, run |drop-index| on the `primary`. The primary stops the index build and creates an associated "abortIndexBuild" `oplog` entry. Secondaries which replicate the "abortIndexBuild" oplog entry stop the in-progress index build and discard the build job. See `index-build-process` for detailed documentation on the index build process.

Use :dbcommand:`currentOp` to identify the index builds associated with a :dbcommand:`createIndexes` or :method:`db.collection.createIndexes()` operation. See `currentOp-cmd-index-creation` for an example.
