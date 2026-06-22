---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-shard-key.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========

# Shard Keys

The shard key is either a single indexed `field` or multiple fields covered by a `compound index` that determines the distribution of the collection's `documents <document>` among the cluster's `shards <shard>`. For details, see `<sharding-shard-key-indexes>`.

MongoDB divides the span of shard key values (or hashed shard key values) into non-overlapping ranges. Each range is associated with a `chunk`, and MongoDB attempts to distribute chunks evenly among the shards in the cluster.

.. include:: /images/sharding-range-based.rst

## Shard a Collection

.. include:: /includes/sharding/shard-a-collection.rst

## Choose a Shard Key

The choice of shard key affects the creation and `distribution of data <sharding-balancing>` across the available `shards <shard>`. The ideal shard key allows MongoDB to distribute documents evenly throughout the cluster while also facilitating common query patterns.

For details, see the `Choose a Shard Key <sharding-internals-choose-shard-key>` page.

## Change a Shard Key

You can change a shard key in two ways:

- You can `refine a shard key <shard-key-refine>` by adding fields to your existing key.
- You can change a shard key entirely and `reshard a collection <sharding-resharding>`
with the new key.

For details, see the `Change a Shard Key <change-a-shard-key>` page.

## Change Shard Key Field Value for a Document

You can change the value for the shard key field in any document in your collection unless the shard key field is the `_id` field. This can affect which shard the document lives on.

For details, see `<update-shard-key>`.

## Set Missing Shard Key Fields

Documents in your collection can be missing fields that your shard key specifies. By default, documents that are missing fields specified by your shard key live in the same chunk range as shard keys with null values.

For details, see `<shard-key-missing-set>`.

## Display a Shard Key

Use :method:`db.printShardingStatus()` to display the shard key used for your collection.

For details, see `<sharding-display-shard-key>`.

## Troubleshoot

Common issues caused by a suboptimal shard key are:

- Jumbo chunks
- Uneven load distribution
- Decreased query performance
For details, see `Troubleshoot Shard Keys <shardkey-troubleshoot-shard-keys>`.

## Contents

- Shard Key Indexes </core/sharding-shard-key-indexes.txt>
- Choose Shard Key </core/sharding-choose-a-shard-key.txt>
- Change Shard Key </core/sharding-change-a-shard-key.txt>
- Change Shard Key Value </core/sharding-change-shard-key-value.txt>
- Set Missing Key Fields </core/sharding-set-missing-shard-key-fields.txt>
- Display a Shard Key </core/sharding-find-shard-key.txt>
- Troubleshoot </core/sharding-troubleshooting-shard-keys.txt>
