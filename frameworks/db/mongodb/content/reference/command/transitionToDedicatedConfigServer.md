---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/transitionToDedicatedConfigServer.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================================

# transitionToDedicatedConfigServer (database command)

## Definition

.. include:: /includes/config-shard-introduction.rst

The `transitionToDedicatedConfigServer` command configures a config shard to run as a dedicated config server. The command causes the `balancer` to prioritize moving the chunks from the config shard to other shards in the cluster.

Before you run `transitionToDedicatedConfigServer`, connect to :binary:`~bin.mongos` and use the `admin database`.

The sharded cluster must have `featureCompatibilityVersion <view-fcv>` set to at least `8.0`.

## Syntax

Command syntax:

```javascript
db.adminCommand( { 
   transitionToDedicatedConfigServer: 1
} )
```

## Behavior

The `transitionToDedicatedConfigServer` command moves application data from the config shard to the other shards in the same way that :dbcommand:`removeShard` moves data. The balancer moves sharded collection data to other eligible shards in the cluster. You must move unsharded collection data and databases to a shard of your choice in the cluster. For the procedure to remove a config shard, see `Remove Shards from a Sharded Cluster <remove-shards-from-cluster-tutorial>`.

Internally, `transitionToDedicatedConfigServer` runs the `removeShard` command. `transitionToDedicatedConfigServer` returns the same response as `removeShard`. The response after a successful data move contains `state: "completed"`. For full response details and examples, see `removeShard Example <removeShard-examples>`. Review the :dbcommand:`removeShard` documentation before running `transitionToDedicatedConfigServer` to understand how it may affect your deployment.

If you run `transitionToDedicatedConfigServer` twice and the shard data is currently moving to other shards, the second run of `transitionToDedicatedConfigServer` returns the current status of the data move. `transitionToDedicatedConfigServer` returns the same response as `removeShard`.

After `transitionToDedicatedConfigServer` completes the data move, the config server is a dedicated config server and is no longer a config shard.

## Access Control

If access control is enabled, the `transitionToDedicatedConfigServer` command requires the :authaction:`transitionToDedicatedConfigServer` authorization action for the `cluster <resource-document>`:

```javascript
{
   resource: { cluster : true },
   actions: [ "transitionToDedicatedConfigServer" ]
}
```

The :authrole:`clusterManager` role has `transitionToDedicatedConfigServer` authorization action and can be assigned to a user.

.. include:: /includes/config-shard-add-role.rst

## Example

The following example configures a config shard to run as a dedicated config server:

```javascript
db.adminCommand( { 
   transitionToDedicatedConfigServer: 1
} )
```

For details, see `<sharded-cluster-config-server-config-shards-downgrade>`.

## Learn More

.. include:: /includes/config-shard-learn-more.rst
