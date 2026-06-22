---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-csrs-versionchanged.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Config servers for sharded clusters can be deployed as a `replica set <replication>` (CSRS). Using a replica set for the config servers improves consistency across the config servers, since MongoDB can take advantage of the standard replica set read and write protocols for the config data. In addition, using a replica set for config servers allows a sharded cluster to have more than 3 config servers since a replica set can have up to 50 members. To deploy config servers as a replica set, the config servers must run the `storage-wiredtiger`.
