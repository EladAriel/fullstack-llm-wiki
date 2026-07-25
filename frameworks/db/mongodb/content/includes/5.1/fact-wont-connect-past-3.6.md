---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/5.1/fact-wont-connect-past-3.6.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.1, certain wire protocol opcodes are removed from the `mongo` shell. The shell will not connect to any version of :binary:`~bin.mongod` or :binary:`~bin.mongos` less than 3.6 since these versions do not support the OP_MSG RPC protocol.
