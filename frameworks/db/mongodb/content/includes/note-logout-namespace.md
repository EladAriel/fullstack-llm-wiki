---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-logout-namespace.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** If you're not logged in and using authentication, |operation-name|
has no effect.
Because MongoDB allows users defined in one database to have
privileges on another database, you must call |operation-name| while
using the same database context that you authenticated to.
If you authenticated to a database such as `users` or
`$external`, you must issue |operation-name| against this
database in order to successfully log out.
