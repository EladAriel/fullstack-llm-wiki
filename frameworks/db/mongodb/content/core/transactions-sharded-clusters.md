---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/transactions-sharded-clusters.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# Production Considerations (Sharded Clusters)

You can perform multi-document transactions on sharded clusters.

The following page lists concerns specific to running transactions on a sharded cluster. These concerns are in addition to those listed in `/core/transactions-production-consideration`.

## Performance

### Single Shard

Transactions that target a single shard should have the same performance as replica-set transactions.

### Multiple Shards

Transactions that affect multiple shards incur a greater performance cost.

> **Note:** On a sharded cluster, transactions that span multiple shards will
error and abort if any involved shard contains an arbiter.

### Time Limit

To specify a time limit, specify a `maxTimeMS` limit on `commitTransaction`.

If `maxTimeMS` is unspecified, MongoDB will use the :parameter:`transactionLifetimeLimitSeconds`.

If `maxTimeMS` is specified but would result in transaction that exceeds :parameter:`transactionLifetimeLimitSeconds`, MongoDB will use the :parameter:`transactionLifetimeLimitSeconds`.

To modify :parameter:`transactionLifetimeLimitSeconds` for a sharded cluster, the parameter must be modified for all shard replica set members.

## Read Concerns

Multi-document transactions support :readconcern:`"local"`, :readconcern:`"majority"`, and :readconcern:`"snapshot"` read concern levels.

For transactions on a sharded cluster, only the :readconcern:`"snapshot"` read concern provides a consistent snapshot across multiple shards.

For more information on read concern and transactions, see `transactions-read-concern`.

## Write Concerns

.. include:: /includes/extracts/transactions-shards-wcmajority-disabled.rst

> **Note:** .. include:: /includes/extracts/transactions-sharded-clusters-commit-writeconcern.rst

## Arbiters

.. include:: /includes/extracts/transactions-arbiters.rst

## Backups and Restores

> **Warning:** .. include:: /includes/extracts/sharded-clusters-backup-restore-mongodump-mongorestore-restriction.rst

## Chunk Migrations

.. include:: /includes/extracts/transactions-chunk-migration.rst

> **Seealso:** :serverstatus:`shardingStatistics.countDonorMoveChunkLockTimeout`

## Outside Reads During Commit

.. include:: /includes/extracts/transactions-multi-shard-block-external-reads.rst

> **Seealso:** `transactions-atomicity`

## Additional Information

See also `/core/transactions-production-consideration`.
