---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-mongos-fcv.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The :binary:`~bin.mongos` binary cannot connect to :binary:`~bin.mongod` instances whose `feature compatibility version (FCV) <view-fcv>` is greater than that of the :binary:`~bin.mongos`. For example, you cannot connect a MongoDB |oldversion| version :binary:`~bin.mongos` to a |newversion| sharded cluster with `FCV <view-fcv>` set to |newversion|. You can, however, connect a MongoDB |oldversion| version :binary:`~bin.mongos` to a |newversion| sharded cluster with `FCV <view-fcv>` set to |oldversion|.
