---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/initiate-replica-set.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

From :binary:`~bin.mongosh`, run the :method:`rs.initiate()` method.

:method:`rs.initiate()` can take an optional `replica set configuration document </reference/replica-configuration>`. In the `replica set configuration document </reference/replica-configuration>`, include:

- The :rsconf:`_id` field set to the replica set name specified in
either the :setting:`replication.replSetName` or the `--replSet` option.

- The :rsconf:`members` array with a document per each member of the
replica set.
