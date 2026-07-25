---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-possible-data-loss-body.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

There is a small chance of data loss when using dollar (`$`) prefixed field names or field names that contain periods (`.`) if these field names are used in conjunction with unacknowledged writes (`write concern <write-concern>` `w=0`) on servers that are older than MongoDB 5.0.

When running :dbcommand:`insert`, :dbcommand:`update`, and :dbcommand:`findAndModify` commands, drivers that are 5.0 compatible remove restrictions on using documents with field names that are dollar (`$`) prefixed or that contain periods (`.`). These field names generated a client-side error in earlier driver versions.

The restrictions are removed regardless of the server version the driver is connected to. If a 5.0 driver sends a document to an older server, the document will be rejected without sending an error.
