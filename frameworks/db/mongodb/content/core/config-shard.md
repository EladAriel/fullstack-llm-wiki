---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/config-shard.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============

# Config Shard

.. include:: /includes/config-shard-intro.rst

A sharded cluster must have a config server, but it can be either a config shard (embedded config server) or a dedicated config server. Using a config shard reduces the number of nodes required and can simplify your deployment. A config shard cluster is also called an embedded config server cluster. You cannot use the same config server for multiple sharded clusters.

## Use Cases

.. include:: /includes/config-shard-use-cases.rst

## Behavior

In an embedded config server cluster, a config shard will be used to store cluster metadata and user data. It helps reduce the complexity of a sharded cluster deployment.

You can store sharded and unsharded collection data in your config shard. It has all the properties of a shard as well as acting as the config server.

### Confirm use of Config Shard

.. include:: /includes/confirm-use-config-shard.rst

### Commands

To configure a dedicated config server to run as a config shard, run the :dbcommand:`transitionFromDedicatedConfigServer` command.

To configure a config shard to run as a dedicated config server, run the :dbcommand:`transitionToDedicatedConfigServer` command.

## Get Started

- `convert-replica-set-to-embedded-config-server`
- `Start a Sharded Cluster with a Config Shard <start-a-sharded-cluster-with-config-shard>`
## Learn More

- `Config Shards <sharded-cluster-config-server-config-shards>`
- :dbcommand:`transitionFromDedicatedConfigServer`
- :dbcommand:`transitionToDedicatedConfigServer`
## Contents

- Convert a Replica Set to a Sharded Cluster with an Embedded Config Server </tutorial/convert-replica-set-to-embedded-config-server>
