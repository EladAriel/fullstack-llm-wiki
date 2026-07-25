---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-set-global-write-concern-before-reconfig.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, you must explicitly set the global default `write concern <write-concern>` before attempting to reconfigure a `replica set <replica set>` with a `configuration <replica-set-configuration-settings>` that would change the implicit default write concern. To set the global default write concern, use the :dbcommand:`setDefaultRWConcern` command.
