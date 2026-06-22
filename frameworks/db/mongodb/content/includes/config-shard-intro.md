---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/config-shard-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.0, you can configure a config server to store your application data in addition to the usual sharded cluster metadata. A :binary:`mongod` node that provides both config server and shard server functionality is called a config shard. A `mongod` node that runs as a standalone :option:`--configsvr` without shard server functionality is called a dedicated `config server <sharded-cluster-config-server>`.
