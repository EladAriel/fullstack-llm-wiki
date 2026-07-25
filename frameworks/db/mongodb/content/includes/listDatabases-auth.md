---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/listDatabases-auth.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Users without the :authaction:`listDatabases` privilege action can run the :dbcommand:`listDatabases` command to return a list of databases for which they have privileges. This includes databases where the user has privileges on specific collections. Run the command with the `authorizedDatabases` option unspecified or set to `true`.
