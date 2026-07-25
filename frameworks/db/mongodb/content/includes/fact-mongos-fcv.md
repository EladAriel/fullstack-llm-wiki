---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-mongos-fcv.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The :binary:`~bin.mongos` binary cannot connect to :binary:`~bin.mongod` instances whose `feature compatibility version (FCV) <view-fcv>` is greater than that of the :binary:`~bin.mongos`. For example, you cannot connect a MongoDB |oldversion| version :binary:`~bin.mongos` to a |newversion| sharded cluster with `FCV <view-fcv>` set to |newversion|. You can, however, connect a MongoDB |oldversion| version :binary:`~bin.mongos` to a |newversion| sharded cluster with `FCV <view-fcv>` set to |oldversion|.
