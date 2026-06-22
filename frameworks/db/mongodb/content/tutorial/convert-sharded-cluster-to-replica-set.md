---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/convert-sharded-cluster-to-replica-set.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================================

# Convert Self-Managed Sharded Cluster to Replica Set

This tutorial describes how to convert a `sharded cluster` to a non-sharded `replica set`. To convert a replica set into a sharded cluster, see `/tutorial/convert-replica-set-to-replicated-shard-cluster`. See the `/sharding` documentation for more information on sharded clusters.

This tutorial guides you through the following tasks:

1. Disable the balancer and lock the cluster.
#. Convert a Single or Sharded Cluster into a Replica Set

#. Unlock the cluster after converting to a replica set.

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

### Version Compatibility

The steps in this tutorial require MongoDB 6.0 or later.

### Authorization

The :dbcommand:`fsync` and :dbcommand:`fsyncUnlock` commands require the :authaction:`fsync` authorization action, which can be assigned through the :authrole:`hostManager` role or a custom role.

### Schedule the Cluster Conversion

Convert the cluster when chunk migrations, resharding, and schema transformations aren't typically performed.

### Reversion to Sharded Cluster

.. include:: /includes/fact-no-shard-after-demotion.rst

## Steps

## Learn More

`sharded-cluster-balancer`
