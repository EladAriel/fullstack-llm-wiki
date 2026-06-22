---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/autoCompact.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# autoCompact (database command)

## Definition

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     autoCompact: <boolean>, 
     freeSpaceTargetMB: <int>, // Optional 
     runOnce: <boolean>, // Optional
   }
)
```

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Command Fields

The command can take the following optional fields:

## Required Privileges

For clusters enforcing `authentication <authentication>`:

- **{+atlas+}:** Users must have the :atlasrole:`autoCompact` built-in role.
- **Self-managed deployments:** Users must have the :authaction:`compact` privilege
action on the cluster. The :authrole:`hostManager` role provides the required privileges for running `autoCompact`.

## Behavior

### Blocking

Background compaction triggered by `autoCompact` applies the same blocking behavior as the :dbcommand:`compact` command. Consequently, if you call `autoCompact` while background compaction is active, MongoDB returns an error.

If you need to restart `autoCompact` or run it again with different options, you must first stop the current background compaction operation:

```javascript
db.runCommand( { autoCompact: false } )
```

Once the current background compaction is disabled, you can restart `autoCompact` with the new configuration.

### Excluded Collections

If an `oplog` exists, MongoDB excludes it from background compaction.

### Performance Considerations

We recommend running `autoCompact` during periods of low traffic.

.. include:: /includes/compaction-checkpoints.rst

### Replica Sets

You can run background compaction on collections and indexes that are stored in a replica set. However, note the following considerations:

- The primary node does not replicate the `autoCompact` command to the
secondary nodes.

- A secondary node can replicate data while background compaction is
running.

- Reads and writes are permitted while background compaction is running.
### Sharded Clusters

`autoCompact` only applies to :binary:`~bin.mongod` instances. In a sharded environment, run `autoCompact` on each shard separately.

You cannot run `autoCompact` against a :binary:`~bin.mongos` instance.

## Learn More

- :dbcommand:`compact`
