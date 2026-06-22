---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/moveable-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Moveable Collections

.. versionadded:: 8.0

.. include:: /includes/moveable-collections-intro.rst

## Use Cases

Moving unsharded collections to any shard can:

- Optimize performance on larger, complex workloads.
- Achieve better resource utilization.
- More evenly distribute data across shards.
Consider the following scenarios:

- A company runs an e-commerce platform with several unsharded collections, such
as `products`, `orders`, and `users` on a single shard. The `orders` collection begins to grow significantly larger than the others, which causes performance issues on the shard. To improve performance and balance the load across the cluster, the administrator can use the `moveCollection` command to move the smaller `products` and `users` collections to a different shard.

- A global application stores user data in three separate unsharded collections
for users located in North America, Europe, and Asia on one shard. To reduce latency for users, an administrator can move these collections to a shard located in each respective region in the same cluster.

- An application frequently performs :pipeline:`$lookup` operations between
two unsharded collections, `orders` and `customers`, that reside on different shards. To improve query performance, a database administrator can move both collections to the same shard.

## Get Started

- `task-move-a-collection`
- `task-stop-moving-a-collection`
## Access Control

To move unsharded collections on a deployment that enforces authentication, you must authenticate as a user with at least the :authrole:`enableSharding` role.

## Learn More

- `primary-shard`
- `sharded-vs-non-sharded-collections`
## Contents

- Move a Collection </tutorial/move-a-collection>
- Multi-Tenant Architecture <core/moveable-collections/multi-tenant>
- Stop Moving a Collection </tutorial/stop-moving-a-collection>
