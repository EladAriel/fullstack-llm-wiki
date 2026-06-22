---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-maxconns-mongos.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This is particularly useful for a :binary:`~bin.mongos` if you have a client that creates multiple connections and allows them to timeout rather than closing them.

In this case, set :setting:`~net.maxIncomingConnections` to a value slightly higher than the maximum number of connections that the client creates, or the maximum size of the connection pool.

This setting prevents the `mongos` from causing connection spikes on the individual `shards <shard>`. Spikes like these may disrupt the operation and memory allocation of the `sharded cluster`.
