---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/convert-replica-set-to-replicated-shard-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# Convert a Self-Managed Replica Set to a Sharded Cluster

Sharded clusters partition data across multiple servers based on a `shard key`. A sharded cluster scales better than a replica set for deployments with large data sets and high throughput operations.

This tutorial converts a single three-member replica set to a sharded cluster with two shards. Each shard in the new cluster is an independent three-member replica set.

## About This Task

- This tutorial is for deployments that have :ref:`authentication
enabled <authentication>`.

- In this tutorial, you specify server settings with :ref:`configuration
files <configuration-options>`. Configuration files contain settings that are equivalent to the :binary:`mongod` and :binary:`mongos` command-line options.

- The sharded cluster you deploy with this tutorial contains ten
servers:

- One server for the :binary:`mongos`.
- Three servers each for the two shards in the cluster (six servers in
total).

- Three servers for the :ref:`config server replica set
<sharding-config-server>`.

> **Important:** Do not add arbiters to your replica sets during the conversion
process. Arbiters change the implicit default write concern from
`{w: majority}` to `{w: 1}`.

### Server Architecture

This tutorial uses the following servers:

The hostnames used in this tutorial are examples. Replace the hostnames used in the example commands with the hostnames used in your deployments.

.. include:: /includes/important-hostnames.rst

## Before You Begin

- To complete this tutorial, you must have a replica set that uses
either keyfile or X.509 certificate authentication. To deploy a secure replica set that uses one of these authentication methods, see either:

- `deploy-repl-set-with-keyfile`
- `x509-internal-authentication`
- This tutorial uses the default data directories `/data/db` and
`/data/configdb`. To use different paths, set the :setting:`storage.dbPath` setting in your configuration file.

- .. include:: /includes/fact-support-online-transition-from-replset-to-sharded-cluster.rst
- All nodes must use the same binary and have the same :ref:`featureCompatibilityVersion
<set-fcv>` while converting a replica set to a sharded cluster.

- .. include:: /includes/fact-no-shard-after-demotion.rst
- .. include:: /includes/fact-convert-shard-query-analysis.rst
## Steps

> **Note:** .. include:: /includes/fact-cannot-connect-directly-to-shards.rst

## Learn More

For more sharding tutorials and procedures, see these pages:

- `sharding-manage-shards`
- `back-up-sharded-cluster-metadata`
- `sharding-high-availability`
