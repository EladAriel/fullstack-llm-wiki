---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-maxconns-mongos.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

This is particularly useful for a :binary:`~bin.mongos` if you have a client that creates multiple connections and allows them to timeout rather than closing them.

In this case, set :setting:`~net.maxIncomingConnections` to a value slightly higher than the maximum number of connections that the client creates, or the maximum size of the connection pool.

This setting prevents the `mongos` from causing connection spikes on the individual `shards <shard>`. Spikes like these may disrupt the operation and memory allocation of the `sharded cluster`.
