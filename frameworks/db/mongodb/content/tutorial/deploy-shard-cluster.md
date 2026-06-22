---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/deploy-shard-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# Deploy a Self-Managed Sharded Cluster

## Overview

This tutorial involves creating a new sharded cluster that consists of a :binary:`~bin.mongos`, the config server replica set, and two shard replica sets.

## Considerations

### Connectivity

Each member of a sharded cluster must be able to connect to all other members in the cluster. This includes all shards and config servers. Ensure that network and security systems, including all interface and firewalls, allow these connections.

### Hostnames and Configuration

.. include:: /includes/important-hostnames.rst

Localhost Deployments `````````````````````

If you use either `localhost` or its IP address as the hostname portion of any host identifier, you must use that identifier as the host setting for any other MongoDB component in the cluster.

For example, the :method:`sh.addShard()` method takes a `host` parameter for the hostname of the target shard. If you set `host` to `localhost`, you must then use `localhost` as the host for all other shards in the cluster.

### Security

This tutorial does not include the required steps for configuring `/core/security-internal-authentication` or `/core/authorization`.

In production environments, sharded clusters should employ at minimum `/core/security-x.509` security for internal authentication and client access.

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Procedure

### Create the Config Server Replica Set

The following steps deploys a config server replica set.

For a production deployment, deploy a config server replica set with at least three members. For testing purposes, you can create a single-member replica set.

> **Note:** The config server replica set must not use the same name as any of
the shard replica sets.

For this tutorial, the config server replica set members are associated with the following hosts:

.. include:: /includes/steps/deploy-sharded-cluster-config-server-noauth.rst

Once the config server replica set (CSRS) is initiated and up, proceed to creating the shard replica sets.

### Create the Shard Replica Sets

For a production deployment, use a replica set with at least three members. For testing purposes, you can create a single-member replica set.

> **Note:** Shard replica sets must not use the same name as the config server replica set.

For each shard, use the following steps to create the shard replica set:

.. include:: /includes/steps/deploy-sharded-cluster-shard-replica-noauth.rst

### Start a `mongos` for the Sharded Cluster

Start a :binary:`~bin.mongos` using either a configuration file or a command line parameter to specify the config servers.

At this point, your sharded cluster consists of the :binary:`~bin.mongos` and the config servers.  You can now connect to the sharded cluster using :binary:`~bin.mongosh`.

### Connect to the Sharded Cluster

Connect :binary:`~bin.mongosh` to the :binary:`~bin.mongos`. Specify the `host` and `port` on which the `mongos` is running:

```bash
mongosh --host <hostname> --port <port>
```

Once you have connected :binary:`~bin.mongosh` to the :binary:`~bin.mongos`, continue to the next procedure to add shards to the cluster.

### Add Shards to the Cluster

In a :binary:`~bin.mongosh` session that is connected to the :binary:`~bin.mongos`, use the :method:`sh.addShard()` method to add each shard to the cluster.

The following operation adds a single shard replica set to the cluster:

```javascript
sh.addShard( "<replSetName>/s1-mongo1.example.net:27018,s1-mongo2.example.net:27018,s1-mongo3.example.net:27018")
```

Repeat these steps until the cluster includes all desired shards.

### Shard a Collection

To shard a collection, connect :binary:`~bin.mongosh` to the :binary:`~bin.mongos` and use the :method:`sh.shardCollection()` method.

> **Note:** If the collection already contains data, you must
`create an index <method-createIndex>` that supports the
`shard key` before sharding the collection. If the collection
is empty, MongoDB creates the index as part of
:method:`sh.shardCollection()`.

MongoDB provides two strategies to shard collections:

- `Hashed sharding <sharding-hashed>` uses a
`hashed index <index-hashed-index>` of a single field as the `shard key` to partition data across your sharded cluster.

```javascript
  sh.shardCollection("<database>.<collection>", { <shard key field> : "hashed" } )
```

- `Range-based sharding <sharding-ranged>` can use multiple
fields as the shard key and divides data into contiguous ranges determined by the shard key values.

```javascript
  sh.shardCollection("<database>.<collection>", { <shard key field> : 1, ... } )
```

### Shard Key Considerations

Your selection of shard key affects the efficiency of sharding, as well as your ability to take advantage of certain sharding features such as `zones <zone-sharding>`. To learn how to choose an effective shard key, see `sharding-shard-key-selection`.

:binary:`~bin.mongosh` provides the method :method:`convertShardKeyToHashed()`. This method uses the same hashing function as the hashed index and can be used to see what the hashed value would be for a key.

> **Seealso:** - For hashed sharding shard keys, see
  `hashed-sharding-shard-key`
- For ranged sharding shard keys, see
  `sharding-ranged-shard-key`

## Contents

- Tiered Hardware for Varying SLA or SLO </tutorial/sharding-tiered-hardware-for-varying-slas>
