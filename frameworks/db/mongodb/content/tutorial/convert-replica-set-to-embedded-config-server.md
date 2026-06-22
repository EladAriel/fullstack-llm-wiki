---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/convert-replica-set-to-embedded-config-server.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Convert Replica Set to an Embedded Config Shard

Starting in MongoDB 8.0, you can configure a config server to store your application data in addition to the usual `sharded cluster` metadata. A config server that stores application data is called a `config shard <config-shard-concept>` or embedded config server.

Converting your replica set into a sharded cluster with an embedded config shard can reduce:

- The number of nodes required in your deployment.
- Complexity for maintaining one-shard clusters.
## About this Task

Starting in MongoDB 8.3, you can convert a replica set directly into a sharded cluster with an embedded config shard.

Previous releases require you to first convert the replica set into a sharded cluster with a dedicated config server replica set, then convert that into one with an embedded config shard.

### Access Control

If access control is enabled, the :dbcommand:`transitionFromDedicatedConfigServer` command requires the :authaction:`transitionFromDedicatedConfigServer` authorization action for the `cluster <resource-document>`.

The :authrole:`clusterManager` role has the `transitionFromDedicatedConfigServer` authorization action and can be assigned to a user.

## Before You Begin

.. include:: /includes/fact-no-shard-after-demotion.rst

## Steps

The following example converts a self-managed replica set to a config shard that contains a pre-existing user data from the replica set.

## Learn More

- `config-shard-concept`
- `manual-convert-replica-set-to-sharded-cluster`
- `remove-shards-from-cluster-tutorial`
- `sharding-config-server`
- :dbcommand:`transitionFromDedicatedConfigServer`
- :dbcommand:`transitionToDedicatedConfigServer`
