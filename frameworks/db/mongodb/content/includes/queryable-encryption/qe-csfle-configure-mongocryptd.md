---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-configure-mongocryptd.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If the driver has access to the `mongocryptd` process, it spawns the process by default. Your application must have write permissions on the working directory to create the `mongocryptd.pid` file.

> **Important:** If possible, start `mongocryptd` on boot, rather than launching it
on demand.

Configure how the driver starts `mongocryptd` through the following parameters:

If a `mongocryptd` process is already running on the port specified by the driver, the driver may log a warning and continue without spawning a new process. Any settings specified by the driver only apply once the existing process exits and a new encrypted client attempts to connect.
