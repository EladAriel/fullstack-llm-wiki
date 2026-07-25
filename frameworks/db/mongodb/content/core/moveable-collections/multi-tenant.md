---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/moveable-collections/multi-tenant.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================================

# Multi-tenant Architecture with Moveable Collections

.. versionadded:: 8.0

In a multi-tenant architecture, a single instance of an application serves multiple users. Multi-tenant users share resources, and generally data belonging to the same tenant is kept on a single shard.

If your multi-tenant configuration has a single tenant per database and the majority of its workload takes place on a single shard, you can move frequently-accessed collections to other shards for more even workload distribution. This reduces the number of collections on the original shard and improves performance system-wide.

> **Note:** If your multi-tenant deployment is a replica set, you can convert it
to a sharded cluster and add additional shards to more evenly
distribute your workload. For more information, see either:
- :atlas:`Modify a Cluster </scale-cluster>` for MongoDB Atlas
 deployments
- `manual-convert-replica-set-to-sharded-cluster`

## Considerations

- Moving collections has operational overhead. Before you move
collections, review the :method:`sh.moveCollection()` documentation for performance considerations.

- The optimal multi-tenant configuration depends on your workload and
application needs. Moving collections to new shards is not as scalable as `multi-tenancy in a single database with shared collections <all-tenants-single>`. However, having each database correspond to a single tenant allows for more customizable security and access patterns.

- To optimize performance for cross-collection operations (like
:pipeline:`$lookup` or transactions that access multiple collections), place all collections for a given tenant on the same shard.

## Learn More

- `task-move-a-collection`
- :atlas:`Build a Multi-Tenant Architecture </build-multi-tenant-arch/>`
