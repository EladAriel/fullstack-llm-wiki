---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-distribute-collection-data.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# Distribute Collection Data

Sharding a collection distributes its documents across multiple shards in your MongoDB cluster. MongoDB uses your specified shard key to determine precisely where each document belongs. Choosing an effective shard key is critical, ensuring even data distribution and workload balancing across all available shards. This approach becomes essential when collections grow too large for a single shard to handle efficiently. Once sharded, MongoDB automatically distributes the collection across all available shards according to your chosen sharding strategy.

## When to Consider Sharding

You should consider sharding a collection when you approach certain resource limits or performance thresholds.

### High Resource Utilization

If a collection’s `working set` fits in RAM, MongoDB serves queries from memory, which provides the fastest query response times. When the working set grows beyond available memory, query latencies grow longer due to increased disk access. Sharding a collection improves query performance by distributing the data across multiple shards, where each shard maintains its own data indexes.

### Large Data Size

If your collection contains 3TB of data or more, you should consider sharding it to optimize performance.

## Distribution Options

When sharding a collection in MongoDB, you can choose from the following distribution options:

## Behavior

When sharding a collection, you must:

- Choose a shard key. Use the :dbcommand:`analyzeShardKey` database command
to facilitate this choice.

- Select a sharding method:
- `sharding-balancing` for automatic data migration
- `Reshard to shard <resharding-a-collection-back-to-same-key>` for complete redistribution
## Learn More

- `sharding-shard-key-creation`
