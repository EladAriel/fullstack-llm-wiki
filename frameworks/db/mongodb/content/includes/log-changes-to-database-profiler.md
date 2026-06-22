---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/log-changes-to-database-profiler.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, changes made to the `database profiler <database-profiler>` `level`, `slowms`, `sampleRate`, or `filter` using the :dbcommand:`profile` command or :method:`db.setProfilingLevel()` wrapper method are recorded in the :option:`log file <mongod --logpath>`.
