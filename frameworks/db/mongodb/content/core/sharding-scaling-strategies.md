---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-scaling-strategies.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Scaling Strategies

Database scaling is a fundamental challenge for growing applications. Whether you start a new application or experience growth, there are two main scaling strategies:

- Vertical scaling – Upgrade a single server with additional resources.
- Horizontal scaling – Distribute the workload across multiple servers.
While vertical scaling can provide immediate relief to resource allocation, horizontal scaling is a more sustainable and flexible approach when scale is a factor.

As applications grow, traditional database scaling forces difficult trade-offs between performance, complexity, and cost. MongoDB supports horizontal scaling through its `sharding architecture <sharding-background>`, which distributes data and workloads across multiple servers known as `shards <shards-concepts>`. If you’re building for scale, it’s crucial to consider sharding proactively to ensure seamless growth.

MongoDB's sharded cluster architecture offers several strategies to scale your database:

- Start early with a sharded cluster, even with a single shard, to future-proof
your application.

- Move unsharded collections between shards to isolate workloads, support
multi-tenant architectures, comply with geographic requirements, optimize costs, and reduce collection density.

- Shard specific collections when they approach resource limits or grow beyond
3 TB in storage size.

- Unshard collections when application patterns change and the benefits of a
sharded collection no longer outweigh the costs.

You can use these flexible scaling capabilities to optimize performance and control costs, while maintaining a single connection point for your applications.

## Strategies for Horizontal Scaling

In a sharded cluster, each shard is a replica set. Multiple shards function as a part of the same cluster. Your application accesses all resources transparently by connecting to `mongos <mongos>`, which handles the complexity of routing requests to the right place.

There are two primary methods to distribute workloads in a sharded cluster:

- Moving collections onto dedicated shards – Assign entire collections to
specific shards, optimizing performance by distributing workloads strategically.

- Partitioning a collection across multiple shards – Split a single collection
across multiple shards using a `shard key <sharding-shard-key>`, distributing data more evenly for scalability.

These approaches can be used independently or combined, depending on your requirements.

## Getting Started

`/core/sharding-start-with-sharding` Learn the benefits of starting with a single shard when building your application.

`/core/sharding-manage-unsharded-collections` Learn about isolating collections on dedicated shards.

`/core/sharding-distribute-collection-data` Learn about sharding a collection.

`/core/sharding-consolidate-collection-data` Learn about unsharding a collection.

## Contents

- Start with Sharded Clusters </core/sharding-start-with-sharding>
- Manage Unsharded Collections </core/sharding-manage-unsharded-collections>
- Distribute Collection Data </core/sharding-distribute-collection-data>
- Consolidate Collection Data </core/sharding-consolidate-collection-data>
