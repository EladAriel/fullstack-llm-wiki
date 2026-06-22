---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-logout-namespace.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** If you're not logged in and using authentication, |operation-name|
has no effect.
Because MongoDB allows users defined in one database to have
privileges on another database, you must call |operation-name| while
using the same database context that you authenticated to.
If you authenticated to a database such as `users` or
`$external`, you must issue |operation-name| against this
database in order to successfully log out.
