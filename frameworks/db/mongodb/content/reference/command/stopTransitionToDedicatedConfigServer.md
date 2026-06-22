---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/stopTransitionToDedicatedConfigServer.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================================

# stopTransitionToDedicatedConfigServer (database command)

## Definition

.. include:: /includes/command/stopTransitionToDedicatedConfigServer.rst

The shard resumes its role in the sharded cluster and is included in rebalancing operations.

When the command runs, the in-progress transition from an embedded config server to a dedicated config server stops by terminating the draining of chunks from the config shard. The config shard then resumes its normal role in balancing.

The command returns `ok: 1` on success, otherwise it returns `ok: 0` with a related error message.

To start transitioning to a dedicated config server, see the :dbcommand:`startTransitionToDedicatedConfigServer` command.

To show the status of the transition from an embedded config server to a dedicated config server, see the :dbcommand:`getTransitionToDedicatedConfigServerStatus` command.

To commit the transition from an embedded config server to a dedicated config server, see the :dbcommand:`commitTransitionToDedicatedConfigServer` command.

.. versionadded:: 8.3

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** This command is not supported in [{+atlas+}](https://www.mongodb.com/docs/atlas)_.
Contact MongoDB support to stop the transition from an embedded to dedicated
config server.

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( { 
     stopTransitionToDedicatedConfigServer: 1
} )
```

## Behavior

### Access Requirements

.. include:: /includes/removeShard-access-requirements.rst

## Examples

To start transitioning from an embedded to a dedicated config server, use the :method:`db.adminCommand` method to run the :dbcommand:`startTransitionToDedicatedConfigServer` command:

```javascript
db.adminCommand( { startTransitionToDedicatedConfigServer: 1 } )
```

To stop transitioning from an embedded to a dedicated config server, use the :method:`db.adminCommand` method to run the :dbcommand:`stopTransitionToDedicatedConfigServer` command:

```javascript
db.adminCommand( { stopTransitionToDedicatedConfigServer: 1 } )
```

## Learn More

- :dbcommand:`startTransitionToDedicatedConfigServer`
- :dbcommand:`getTransitionToDedicatedConfigServerStatus`
