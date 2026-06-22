---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/deploy-sharded-cluster-with-keyfile-access-control.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================================

# Keyfile Authentication for Self-Managed Sharded Clusters

## Overview

Enforcing access control on a `sharded cluster` requires configuring:

- Security between components of the cluster using
`Internal Authentication<replica-set-security>`.

- Security between connecting clients and the cluster using
`User Access Controls<authorization>`.

For this tutorial, each member of the sharded cluster must use the same internal authentication mechanism and settings. This means enforcing internal authentication on each :binary:`~bin.mongos` and :binary:`~bin.mongod` in the cluster.

The following tutorial uses a `keyfile <internal-auth-keyfile>` to enable internal authentication.

Enforcing internal authentication also enforces user access control. To connect to the replica set, clients like :binary:`~bin.mongosh` need to use a `user account<authorization>`. See `security-shardClust-deploy-access-control`.

### CloudManager and OpsManager

If you are using Cloud Manager or Ops Manager to manage your deployment, see the respective :mms-docs:`Cloud Manager manual </tutorial/edit-host-authentication-credentials>` or the :opsmgr:`Ops Manager manual </tutorial/edit-host-authentication-credentials>` to enforce authentication.

## Considerations

.. include:: /includes/important-hostnames.rst

### IP Binding

.. include:: /includes/fact-default-bind-ip-change.rst

### Keyfile Security

Keyfiles are bare-minimum forms of security and are best suited for testing or development environments. For production environments we recommend using `X.509 certificates<security-auth-x509>`.

### Access Control

.. include:: /includes/internal-authentication-tutorials-access-control-consideration.rst

### Users

.. include:: /includes/sharded-clusters-users.rst

This tutorial requires creating sharded cluster users, but includes optional steps for adding shard-local users.

See the `/core/security-users` security documentation for more information.

### Operating System

This tutorial uses the :binary:`~bin.mongod` and :binary:`~bin.mongos` programs. Windows users should use the :binary:`mongod.exe` and :binary:`mongos.exe` programs instead.

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Deploy Sharded Cluster with Keyfile Access Control

The following procedures involve creating a new sharded cluster that consists of a :binary:`~bin.mongos`, the config servers, and two shards.

.. include:: /includes/important-hostnames.rst

### Create the Keyfile

.. include:: /includes/extracts/keyfile-intro-sharded-cluster.rst

```bash
openssl rand -base64 756 > <path-to-keyfile>
chmod 400 <path-to-keyfile>
```

See `internal-auth-keyfile` for additional details  and requirements for using keyfiles.

### Distribute the Keyfile

.. include:: /includes/extracts/keyfile-distribution-sharded-cluster.rst

### Create the Config Server Replica Set

The following steps deploys a config server replica set.

For a production deployment, deploys a config server replica set with at least three members. For testing purposes, you can create a single-member replica set.

.. include:: /includes/steps/deploy-sharded-cluster-config-server.rst

Once the config server replica set (CSRS) is initiated and up, proceed to creating the shard replica sets.

### Create the Shard Replica Sets

For a production deployment, use a replica set with at least three members. For testing purposes, you can create a single-member replica set.

These steps include optional procedures for adding shard-local users. Executing them now ensures that there are users available for each shard to perform shard-level maintenance.

.. include:: /includes/steps/deploy-sharded-cluster-shard-replica.rst

### Connect a `mongos` to the Sharded Cluster

.. include:: /includes/steps/deploy-sharded-cluster-connect.rst

### Add Shards to the Cluster

To proceed, you must be connected to the :binary:`~bin.mongos` and authenticated as the cluster administrator user for the sharded cluster.

> **Note:** This is the cluster administrator for the sharded cluster and not
the shard-local cluster administrator.

To add each shard to the cluster, use the :method:`sh.addShard()` method. If the shard is a replica set, specify the name of the replica set and specify a member of the set. In production deployments, all shards should be replica sets.

The following operation adds a single shard replica set to the cluster:

```javascript
sh.addShard( "<replSetName>/s1-mongo1.example.net:27017")
```

The following operation is an example of adding a standalone :binary:`~bin.mongod` shard to the cluster:

```javascript
sh.addShard( "s1-mongo1.example.net:27017")
```

Repeat these steps until the cluster includes all shards. At this point, the sharded cluster enforces access control for the cluster as well as for internal communications between each sharded cluster component.

### Shard a Collection

To proceed, you must be connected to the :binary:`~bin.mongos` and authenticated as the cluster administrator user for the sharded cluster.

> **Note:** This is the cluster administrator for the sharded cluster and not
the shard-local cluster administrator.

To shard a collection, use the :method:`sh.shardCollection()` method. You must specify the full namespace of the collection and a document containing the shard key.

Your selection of shard key affects the efficiency of sharding, as well as your ability to take advantage of certain sharding features such as `zones <zone-sharding>`. See the selection considerations listed in the `sharding-shard-key-selection`.

If the collection already contains data, you must create an index on the `shard key` using the :method:`db.collection.createIndex()` method before using :method:`~sh.shardCollection()`.

If the collection is empty, MongoDB creates the index as part of :method:`sh.shardCollection()`.

The following is an example of the :method:`sh.shardCollection()` method:

```javascript
sh.shardCollection("<database>.<collection>", { <key> : <direction> } )
```

## Next Steps

Create users to allow clients to connect to and interact with the sharded cluster.

See `database-user-roles` for basic built-in roles to use in creating read-only and read-write users.

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see `/tutorial/configure-x509-member-authentication`.

To upgrade from keyfile internal authentication to X.509 internal authentication, see `/tutorial/upgrade-keyfile-to-x509`.

> **Seealso:** - `/core/sharded-cluster-components`
- `/core/sharded-cluster-requirements`
