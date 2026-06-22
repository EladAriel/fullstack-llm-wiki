---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/confirm-sharded-cluster-config-server-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You can confirm that a sharded cluster uses a config shard by using one of the following methods:

- Run the :method:`sh.isConfigShardEnabled()` method
in `mongosh`. If the `sh.isConfigShardEnabled()` output contains `enabled: true`, the cluster uses a config shard. If the output contains `enabled: false`, the cluster does not use a config shard.

- Run the :dbcommand:`listShards` command against the `admin` database while
connected to a :binary:`mongos and inspect the output for a document where id` is set to `"config"`. If the `listShards output does not contain a document where id` is set to `"config"`, the cluster does not use a config shard.
