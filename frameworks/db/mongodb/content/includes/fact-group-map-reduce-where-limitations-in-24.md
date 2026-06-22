---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-group-map-reduce-where-limitations-in-24.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:dbcommand:`map-reduce operations <mapReduce>` and :query:`$where` operator expressions **cannot** access certain global functions or properties, such as `db`, that are available in :binary:`~bin.mongosh`.

The following JavaScript functions and properties **are available** to :dbcommand:`map-reduce operations <mapReduce>` and :query:`$where` operator expressions:
