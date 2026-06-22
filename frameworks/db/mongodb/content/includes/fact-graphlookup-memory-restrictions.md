---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-graphlookup-memory-restrictions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If the :pipeline:`$graphLookup` stage consumes more than 100 megabytes of memory, it automatically writes temporary files to disk. You can see when :pipeline:`$graphLookup` uses disk through the :dbcommand:`serverStatus` command and view an explanation of :pipeline:`$graphLookup` disk usage through the :method:`~db.collection.explain()` command in `executionStats` verbosity mode.

If the :pipeline:`$graphLookup` stage exceeds 100 megabytes of memory and the `allowDiskUse` option is set to `false`, :pipeline:`$graphLookup` returns an error.
