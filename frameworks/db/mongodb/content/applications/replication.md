---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/applications/replication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Replica Set Read and Write Semantics

From the perspective of a client application, whether a MongoDB instance is running as a single server (i.e. "standalone") or a `replica set` is transparent. However, MongoDB provides additional read and write configurations for replica sets.

> **Note:** `Sharded clusters <sharded cluster>` where the shards are also
replica sets provide the same operational semantics with regards to
write and read operations.

`/core/replica-set-write-concern` Write concern describes the level of acknowledgment requested from MongoDB for write operations.

`/core/read-preference` Read preference specifies where (i.e. which members of the replica set) the drivers should direct the read operations.

`/core/read-preference-mechanics` Describes the mechanics of read preference.

## Contents

- Write Concern </core/replica-set-write-concern>
- Read Preference </core/read-preference>
- Server Selection Algorithm </core/read-preference-mechanics>
