---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-start-with-sharding.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# Start with Sharded Clusters

We recommend starting with a single sharded cluster when you are building a new application regardless of your immediate need for multiple shards.

The following scenarios benefit from sharded cluster architecture:

## Details

Starting with a sharded cluster is a proactive approach that offers:

- Effortless Horizontal Scaling – You can easily add shards as your application
grows, without the complexity of migrating from a replica set.

- Cost-Effective Infrastructure – MongoDB 8.0 introduces
`config shards <config-shard-concept>`, allowing you to set up a sharded cluster on a single replica set infrastructure without dedicated config servers. In MongoDB Atlas, sharded clusters with up to 3 shards in version 8.0 use config shards by default.

Consider adding shards when your database reaches 60-70% of resource utilization (RAM, vCPUs, or storage) of a sizable machine. For example, in Atlas, consistent 60-70% resource utilization of an M60 machine with a 4 TB disk indicates an additional shard should be added.

## Learn More

- `sharding-manage-unsharded-collections`
- `sharding-distribute-collection-data`
