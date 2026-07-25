---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/audit-local-remote.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, can alternatively be a document with one of these fields:

- `isSystemUser` that indicates whether the user who
caused the event was a system user. Logged for self-referential jobs initiated by a background process that runs on the same server instance.

- `unix` that contains the MongoDB socket file path if the client
connects through a Unix domain socket.
