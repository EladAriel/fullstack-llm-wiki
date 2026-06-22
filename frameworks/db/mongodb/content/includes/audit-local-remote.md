---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/audit-local-remote.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, can alternatively be a document with one of these fields:

- `isSystemUser` that indicates whether the user who
caused the event was a system user. Logged for self-referential jobs initiated by a background process that runs on the same server instance.

- `unix` that contains the MongoDB socket file path if the client
connects through a Unix domain socket.
