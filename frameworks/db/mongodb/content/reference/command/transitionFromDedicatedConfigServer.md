---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/transitionFromDedicatedConfigServer.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================================

# transitionFromDedicatedConfigServer (database command)

## Definition

.. include:: /includes/config-shard-introduction.rst

The `transitionFromDedicatedConfigServer` command configures a dedicated config server to run as a config shard.

Before you run `transitionFromDedicatedConfigServer`, connect to :binary:`~bin.mongos` and use the `admin database`.

The sharded cluster must have `featureCompatibilityVersion <view-fcv>` set to at least `8.0`.

## Syntax

Command syntax:

```javascript
db.adminCommand( { 
   transitionFromDedicatedConfigServer: 1
} )
```

## Behavior

The `transitionFromDedicatedConfigServer` command adds the config server as a shard in the cluster. Internally, `transitionFromDedicatedConfigServer` runs the `addShard` command.

.. include:: /includes/confirm-sharded-cluster-config-server-intro.rst

For details, see `<confirm-use-of-config-shard>`.

If you must downgrade the `feature compatibility version <view-fcv>` below 8.0, first run the :dbcommand:`transitionToDedicatedConfigServer` command. For downgrade details, see `sharded-cluster-config-server-config-shards-downgrade`.

## Access Control

If access control is enabled, the `transitionFromDedicatedConfigServer` command requires the :authaction:`transitionFromDedicatedConfigServer` authorization action for the `cluster <resource-document>`:

```javascript
{
   resource: { cluster : true },
   actions: [ "transitionFromDedicatedConfigServer" ]
}
```

The :authrole:`clusterManager` role has `transitionFromDedicatedConfigServer` authorization action and can be assigned to a user.

.. include:: /includes/config-shard-add-role.rst

## Example

The following example configures a dedicated config server to run as a config shard:

```javascript
db.adminCommand( { 
   transitionFromDedicatedConfigServer: 1
} )
```

## Learn More

.. include:: /includes/config-shard-learn-more.rst
