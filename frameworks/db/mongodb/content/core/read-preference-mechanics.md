---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/read-preference-mechanics.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# Server Selection Algorithm

MongoDB drivers use a Server Selection algorithm to choose which replica set member to use or, when connected to multiple :binary:`~bin.mongos` instances, which :binary:`~bin.mongos` instance to use.

Server selection occurs once per operation.

> **Note:** .. include:: /includes/extracts/transactions-read-pref.rst

## Read Preference for Replica Sets

Server selection occurs once per operation and is governed by the `read preference <read-preference>` and `localThresholdMS` settings to determine member eligibility for reads. The read preference is re-evaluated for each operation.

.. include:: /includes/extracts/server-selection-read-preference-replica-sets.rst

## Read Preference for Sharded Clusters

### Load Balancing

If there is more than one :binary:`~bin.mongos` instance in the connection seed list, the driver determines which :binary:`~bin.mongos` is the "closest" (that is, the member with the lowest average network round-trip-time) and calculates the latency window by adding the average round-trip-time of this "closest" :binary:`~bin.mongos` instance and the `localThresholdMS`. The driver load balances randomly across the :binary:`~bin.mongos` instances that fall within the latency window.

> **Note:** `localThresholdMS` biases server selection toward
lower-latency local targets. The setting can't remove the
cross-region network topology that a single private endpoint
creates or guarantee all connections remain in the local
region. In this configuration, a client can still connect
through a :binary:`~bin.mongos` in another region.

### Read Preference and Shards

For sharded clusters that have replica set shards, :binary:`~bin.mongos` applies the read preference when reading from the shards. Server selection is governed by the `read preference </core/read-preference>` and :setting:`replication.localPingThresholdMs` settings. The read preference is re-evaluated for each operation.

.. include:: /includes/extracts/server-selection-read-preference-sharded-clusters.rst
