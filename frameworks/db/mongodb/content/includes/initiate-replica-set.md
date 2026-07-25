---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/initiate-replica-set.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

From :binary:`~bin.mongosh`, run the :method:`rs.initiate()` method.

:method:`rs.initiate()` can take an optional `replica set configuration document </reference/replica-configuration>`. In the `replica set configuration document </reference/replica-configuration>`, include:

- The :rsconf:`_id` field set to the replica set name specified in
either the :setting:`replication.replSetName` or the `--replSet` option.

- The :rsconf:`members` array with a document per each member of the
replica set.
