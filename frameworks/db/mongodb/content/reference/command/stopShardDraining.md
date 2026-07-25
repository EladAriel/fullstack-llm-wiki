---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/stopShardDraining.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

#################################### stopShardDraining (database command) ####################################

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** .. include:: /includes/edit-shards-atlas-compatibility.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( { 
     stopShardDraining: <shard> 
} )
```

## Behavior

### Access Requirements

.. include:: /includes/removeShard-access-requirements.rst

## Examples

To start draining a shard, use the :method:`db.adminCommand` method to run the :dbcommand:`startShardDraining` command:

```javascript
db.adminCommand( { startShardDraining: "shard04" } )
```

To stop draining the shard, use the :method:`db.adminCommand` method to run the `stopShardDraining` command:

```javascript
db.adminCommand( { stopShardDraining: "shard04" } )
```

## Learn More

- :dbcommand:`startShardDraining`
- :dbcommand:`shardDrainingStatus`
- :dbcommand:`commitShardRemoval`
