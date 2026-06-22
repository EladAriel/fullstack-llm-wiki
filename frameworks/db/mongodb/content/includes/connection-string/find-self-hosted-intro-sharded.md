---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/connection-string/find-self-hosted-intro-sharded.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you are connected to your self-hosted MongoDB deployment, run :method:`db.getMongo()` method to return the connection string.

If you are not connected to your deployment, you can determine your connection string based on the connection string format and options you want to use.

The following sharded cluster connection string includes these elements:

- The hostnames of the :binary:`~bin.mongos` instances of the sharded
cluster.

- Authentication as user `myDatabaseUser` with the password
`D1fficultP%40ssw0rd`.
