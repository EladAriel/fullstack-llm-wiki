---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-remove-maxSize-addShard.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in version 6.2, MongoDB removes the `maxSize` field from the :dbcommand:`addShard` command. As a result:

- Running :dbcommand:`addShard` with the `maxSize` field returns
an `InvalidOptions` error.

- New documents in the `config.shards` collection no longer
include the `maxSize` field.

- Any pre-existing `maxSize` field entries are ignored.
