---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/listDatabases-auth.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Users without the :authaction:`listDatabases` privilege action can run the :dbcommand:`listDatabases` command to return a list of databases for which they have privileges. This includes databases where the user has privileges on specific collections. Run the command with the `authorizedDatabases` option unspecified or set to `true`.
