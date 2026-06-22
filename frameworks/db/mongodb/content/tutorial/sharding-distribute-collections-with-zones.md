---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/sharding-distribute-collections-with-zones.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# Distribute Collections Using Zones

.. include:: /includes/intro-zone-sharding.rst

You can use `zone sharding <zone-sharding>` to distribute collections across a sharded cluster and designate which shards store data for each collection. You can distribute collections based on shard properties, such as physical resources and available memory, to ensure that each collection is stored on the optimal shard for that data.

## Prerequisites

To complete this tutorial, you must:

- `Deploy a sharded cluster <sharding-procedure-setup>`. This
tutorial uses a sharded cluster with three shards.

- Connect to a :program:`mongos`. You cannot create zones or zone ranges
by connecting directly to a shard.

- Authenticate as a user with at least the :authrole:`clusterManager`
role on the `admin` database. To view user permissions, use the :method:`db.getUser()` method.

## Scenario

You have a database called `shardDistributionDB` that contains two sharded collections:

- `bigData`, which contains a large amount of data.
- `manyIndexes`, which contains many large indexes.
You want to limit each collection to a subset of shards so that each collection can use the shards' different physical resources.

### Architecture

The sharded cluster has three shards. Each shard has unique physical resources:

### Zones

To distribute collections based on physical resources, use shard zones. A shard zone associates collections with a specific subset of shards, which restricts the shards that store the collection's data. In this example, you need two shard zones:

### Shard Key

In this tutorial, the `shard key <shard-key>` you will use to shard each collection is `{ _id: "hashed" }`. You will configure shard zones **before** you shard the collections. As a result, each collection's data only ever exists on the shards in the corresponding zone.

With `hashed sharding <index-type-hashed>`, if you shard collections before you configure zones, MongoDB assigns `chunks <chunk>` evenly between all shards when sharding is enabled. This means that chunks may be temporarily assigned to a shard poorly suited to handle that chunk's data.

### Balancer

The `balancer <sharding-balancing>` migrates chunks to the appropriate shard, respecting any configured zones. When balancing is complete, shards only contain chunks whose ranges match its assigned zones.

> **Important:** Adding, removing, or changing zones or zone ranges can result in
chunk migrations. Depending on the size of your dataset and the
number of chunks a zone or zone range affects, these migrations may
impact cluster performance. Consider running the balancer during
specific scheduled windows. To learn how to set a scheduling window,
see `sharding-schedule-balancing-window`.

## Steps

Use the following procedure to configure shard zones and distribute collections based on shard physical resources.

## Learn More

To learn more about sharding and balancing, see the following pages:

- `sharding-data-partitioning`
- `index-type-hashed`
- `sharding-manage-zones`
- `sharding-shards`
