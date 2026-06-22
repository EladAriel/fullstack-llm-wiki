---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-manage-unsharded-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# Manage Unsharded Collections

Collections on the same replica set can encounter performance bottlenecks when competing for resources. As your data grows beyond the available memory, increased disk I/O introduces latency and strains system resources, degrading overall application performance. Isolating collections on dedicated shards within your cluster reduces these resource constraints while maintaining a single connection point for your application.

Benefits of Collection Isolation:

- Workload Separation – Prevent resource contention by assigning collections to
specific shards.

- Hardware Optimization – Configure `asymmetric shards <independently-scaling-shards>`
with hardware tailored to specific collection requirements.

- Independent Scaling –  Scale collections individually based on workload growth.
- Improved Resilience – Reduce recovery time by isolating potential failures.
## When to Use `moveCollection`

Moving collections on dedicated shards is particularly beneficial when your collection requirements vary in the following ways:

Assigning collections to shards with the necessary hardware to meet their specific requirements optimizes performance while maintaining operational simplicity.

## When to Move Unsharded Collections

Starting in MongoDB 8.0, `movable collections <moveable-collections>` allow you to strategically place any unsharded collection on any shard within the cluster. Previously, unsharded collections were restricted to the primary shard of their database, leading to resource bottlenecks. `Moving a collection <task-move-a-collection>` simplifies horizontal scaling by allowing you to relocate unsharded collections without disrupting workloads.

While not every collection needs to be sharded, deploying a sharded cluster provides horizontal scaling advantages even for unsharded collections. This approach maintains a single connection point for all data access, simplifying application architecture.

The following scenarios benefit from moving unsharded collections across shards:

### Workload Isolation

When multiple collections serve different workloads within the same cluster, moving unsharded collections across different shards helps prevent resource contention. This separation eliminates issues where one workload's performance negatively impacts others.

### Multi-Tenant Architecture

In environments hosting collections for different tenants, MongoDB's :dbcommand:`moveCollection` command enables seamless distribution of collections across shards without downtime. This flexibility optimizes resource allocation based on each tenant's specific needs.

### Geographic Data Distribution

Organizations may need to store user data in specific geographic regions to comply with data sovereignty regulations. With moveCollection, you can place unsharded collections on shards in different regions and relocate them as regulatory requirements evolve.

### Cost Optimization

Before MongoDB 8.0, all unsharded collections within a database were restricted to the primary shard. This limitation often forced upgrades to larger, more expensive instance tiers. MongoDB 8.0 removes this constraint, allowing movement of unsharded collections across all available shards in the cluster.

Moving unsharded collections across `asymmetric shard <cluster-autoscaling>` hardware delivers significant benefits for resource optimization, allowing you to place specific collections on hardware tailored to their requirements. By matching collections to appropriate hardware resources, you can scale different workloads independently based on their actual demands. This targeted approach improves performance while avoiding the cost of over-provisioning resources across the entire cluster.

### Reduced Collection Density

While MongoDB has no hard limit on collection count per instance, performance degrades when a node manages too many collections and indexes. To learn more about these limits, see `limits-atlas-collection-and-index`.

By distributing unsharded collections across different shards, you can reduce collection density on any single node while maintaining a unified access point for applications.

### Strategic co-location

Consider co-locating unsharded collections on the same shard to minimize distributed operations, such as cross-collection transactions or join operations (:pipeline:`$lookup`). Keeping related operations confined to a single shard eliminates network overhead, reduces latency, and improves overall performance. This approach is particularly effective for collections that are frequently joined or accessed together in the same transaction.

## Command Syntax

```javascript
sh.moveCollection("database.collection", "shardName")
```

The following example moves four unsharded collection between two shards for equal distribution of collections:

```javascript
db.adminCommand({moveCollection:"E", toShard: "shard1"})
```

.. figure:: /images/sharding-move-unsharded-collection.bakedsvg.svg

## When to avoid using `moveCollection`

While `moveCollection` offers significant flexibility, there are a few specific scenarios where it may not be the optimal solution:

### Large Collections

Don't use `moveCollection` when a collection is too large for a single shard. Consider sharding a collection when it is approaching 3 TB in size.

### Collections with {+fts+} Indexes

If a specific collection uses :atlas:`{+fts+} </atlas-search/>`, be aware that `moveCollection` uses `resharding <sharding-resharding>` to rewrite the collection on a different shard. After moving the collection, you will need to manually rebuild its {+fts+} index. Until the indexes are fully rebuilt, {+fts+} functionality will be unavailable for this specific collection, though the rest of your application will function normally.

Before using `moveCollection`, evaluate these limitations against your application requirements to determine if it's the appropriate solution.

## Learn More

- `task-move-a-collection`
