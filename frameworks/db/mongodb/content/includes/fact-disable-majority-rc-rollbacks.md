---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-disable-majority-rc-rollbacks.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you disable :readconcern:`"majority"` read concern, MongoDB prevents :dbcommand:`collMod` commands which modify an index from `rolling back <replica-set-rollbacks>`. If you need to roll back `collMod` commands, you must resync the affected nodes with the `primary` node.
