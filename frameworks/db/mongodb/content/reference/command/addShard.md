---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/addShard.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# addShard (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** .. include:: /includes/edit-shards-atlas-compatibility.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     addShard: "<replica_set>/<hostname><:port>", 
     name: "<shard_name>" 
   } 
)
```

### Command Fields

> **Note:** .. include:: /includes/fact-remove-maxSize-addShard.rst

The command contains the following fields:

The :dbcommand:`addShard` command stores shard configuration information in the `config database`. Always run :dbcommand:`addShard` when using the `admin` database.

## Considerations

### Storage

The shard that you add to your sharded cluster must be empty.

### Balancing

.. include:: /includes/fact-adding-shards-changes-cluster-balance.rst

### Hidden Members

.. include:: /includes/important-add-shard-not-compatible-with-hidden-members.rst

### DDL Operations

If you add a shard while your cluster executes a DDL operation (operation that modifies a collection such as :dbcommand:`reshardCollection`), `addShard` only executes after the concurrent DDL operation finishes.

## Required Access

You must have the :authaction:`addShard` `action <security-user-actions>` on a cluster resource to run the `addShard` command. The :authrole:`clusterAdmin` or :authrole:`clusterManager` `built-in roles <built-in-roles>` contain the `addShard` action and grant privileges to run the `addShard` command.

## Examples

The following command adds a replica set as a shard:

```javascript
use admin
db.runCommand( { addShard: "repl0/mongodb3.example.net:27327"} )
```

> **Warning:** Do not use `localhost` for the hostname unless your
config server is also running on
`localhost`.
