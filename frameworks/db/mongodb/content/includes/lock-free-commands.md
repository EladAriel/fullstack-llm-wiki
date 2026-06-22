---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/lock-free-commands.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, the following read operations are not blocked when another operation holds an exclusive (X) write lock on the collection:

- :dbcommand:`find`
- :dbcommand:`count`
- :dbcommand:`distinct`
- :dbcommand:`aggregate`
- :dbcommand:`mapReduce`
- :dbcommand:`listCollections`
- :dbcommand:`listIndexes`
When writing to a collection, :dbcommand:`mapReduce` and :dbcommand:`aggregate` hold an intent exclusive (IX) lock. Therefore, if an exclusive X lock is already held on a collection, :dbcommand:`mapReduce` and :dbcommand:`aggregate` write operations are blocked.
