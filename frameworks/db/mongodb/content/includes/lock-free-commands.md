---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/lock-free-commands.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
