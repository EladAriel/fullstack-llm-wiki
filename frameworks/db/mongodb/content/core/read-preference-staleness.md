---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/read-preference-staleness.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# Read Preference `maxStalenessSeconds`

Replica set members can lag behind the `primary` due to network congestion, low disk throughput, long-running operations, etc. The read preference `maxStalenessSeconds` option lets you specify a maximum replication lag, or "staleness", for reads from `secondaries <secondary>`. When a secondary's estimated staleness exceeds `maxStalenessSeconds`, the client stops using it for read operations.

.. include:: /includes/fact-important-maxStalenessSeconds-intended-use.rst

> **Note:** `Flow control <replication-flow-control>` limits the rate at which
the primary applies its writes with the goal of keeping :data:`majority
committed <replSetGetStatus.optimes.lastCommittedOpTime>` lag under a
specified maximum value.

You can specify `maxStalenessSeconds` with the following read preference modes:

- :readmode:`primaryPreferred`
- :readmode:`secondary`
- :readmode:`secondaryPreferred`
- :readmode:`nearest`
Max staleness is not compatible with mode :readmode:`primary` and only applies when `selecting <replica-set-read-preference-behavior-member-selection>` a `secondary` member of a set for a read operation.

When selecting a server for a read operation with `maxStalenessSeconds`, clients estimate how stale each secondary is by comparing the secondary's last write to that of the primary. The client will then direct the read operation to a secondary whose estimated lag is less than or equal to `maxStalenessSeconds`.

If there is no primary, the client uses the secondary with the most recent write for the comparison.

By default, there is no maximum staleness and clients will not consider a secondary's lag when choosing where to direct a read operation.

You must specify a `maxStalenessSeconds` value of 90 seconds or longer: specifying a smaller `maxStalenessSeconds` value will raise an error. Clients estimate secondaries' staleness by periodically checking the latest write date of each replica set member. Since these checks are infrequent, the staleness estimate is coarse. Thus, clients cannot enforce a `maxStalenessSeconds` value of less than 90 seconds.
