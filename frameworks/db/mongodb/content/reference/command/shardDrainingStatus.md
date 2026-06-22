---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/shardDrainingStatus.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# shardDrainingStatus (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** .. include:: /includes/edit-shards-atlas-compatibility.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( { 
     shardDrainingStatus: <shard> 
} )
```

## Output Fields

This command returns the following output:

## Behavior

### Access Requirements

.. include:: /includes/removeShard-access-requirements.rst

### Database Migration Requirements

.. include:: /includes/sharding-database-migration-requirements.rst

### Collection Migration Requirements

.. include:: /includes/sharding-collection-migration-requirements.rst

## Examples

To start draining a shard, use the :method:`db.adminCommand` method to run the :dbcommand:`startShardDraining` command:

```javascript
db.adminCommand( { startShardDraining: "shard04" } )
```

To check the status of the draining operation, use the `shardDrainingStatus` command:

## Learn More

- :dbcommand:`startShardDraining`
- :dbcommand:`commitShardRemoval`
