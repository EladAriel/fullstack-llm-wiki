---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-remove-maxSize-addShard.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in version 6.2, MongoDB removes the `maxSize` field from the :dbcommand:`addShard` command. As a result:

- Running :dbcommand:`addShard` with the `maxSize` field returns
an `InvalidOptions` error.

- New documents in the `config.shards` collection no longer
include the `maxSize` field.

- Any pre-existing `maxSize` field entries are ignored.
