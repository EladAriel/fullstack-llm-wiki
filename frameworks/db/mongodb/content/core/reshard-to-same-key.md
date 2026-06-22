---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/reshard-to-same-key.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# Reshard to the Same Shard Key

Starting in MongoDB 8.0, you can reshard to the same shard key to move data with no downtime or impact on workload. This enables you to:

.. include:: /includes/resharding-about.rst

Starting in MongoDB 8.0, resharding reads data using natural order scan. Resharding first clones all the data and then builds relevant indexes, resulting in orders of magnitude speed improvement of the resharding process.

## Command Syntax

You can reshard to the same key using the `reshardCollection` command with `forceRedistribution` set to `true`.

The `reshardCollection` command has the following syntax:

.. include:: /includes/reshardCollection-syntax.rst

> **Note:** .. include:: /includes/fact-resharding-if-key-is-hashed.rst

For details, see :dbcommand:`reshardCollection`.

## Use Cases

Resharding is a strategy to move data with no downtime or impact on workload. Use the `<reshard-to-shard-def>` technique to shard a collection and distribute data across all shards.

Use resharding to distribute your collections across all relevant shards faster than `chunk migrations <migrate-chunks-sharded-cluster>`. Resharding writes to all shards in parallel while each shard can only participate in one chunk migration at a time. Resharding drops the old collection at the end of the process. There are no orphan documents at the end of resharding.

### Reshard to Shard

The **Reshard to Shard** technique lets you use resharding to shard a collection and distribute the data to all of the shards in a cluster.

Consider using **Reshard to Shard** when you are initially sharding a collection of any size across any number of shards. If your deployment meets the `resource requirements <reshard-to-same-key-behavior>`, use **Reshard to Shard** no matter how large the collection you want to shard.

## Behavior

### Storage

.. include:: /includes/reshard-to-same-key/storage.rst

### Latency

.. include:: /includes/reshard-to-same-key/latency.rst

### Reshard Limitations

.. include:: /includes/fact-reshard-limitations.rst

### Additional Resource Requirements

.. include:: /includes/reshard-to-same-key/addl-resource-reqs.rst

## Get Started

- `<resharding-a-collection-back-to-same-key>`
- `<resharding-for-adding-and-removing-shards-tutorial>`
## Learn More

- :method:`sh.reshardCollection()`
- `<sharding-resharding>`
