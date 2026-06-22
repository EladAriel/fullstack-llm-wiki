---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getTransitionToDedicatedConfigServerStatus.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================================

# getTransitionToDedicatedConfigServerStatus (database command)

## Definition

.. include:: /includes/command/getTransitionToDedicatedConfigServerStatus.rst

The command returns `ok: 0` with an error if the transition fails, otherwise it returns `ok: 1`.

To start transitioning to a dedicated config server, see the :dbcommand:`startTransitionToDedicatedConfigServer` command.

To stop the in-progress transition from an embedded config server to a dedicated config server, see the :dbcommand:`stopTransitionToDedicatedConfigServer` command.

To commit the transition from an embedded config server to a dedicated config server, see the :dbcommand:`commitTransitionToDedicatedConfigServer` command.

.. versionadded:: 8.3

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** .. include:: /includes/fact-transaction-sharded.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( { 
     getTransitionToDedicatedConfigServerStatus: 1 
} )
```

## Output Fields

This command returns the following output:

## Behavior

### Access Requirements

.. include:: /includes/removeShard-access-requirements.rst

### Database Migration Requirements

.. include:: /includes/config-server-database-migration-requirements.rst

### Collection Migration Requirements

.. include:: /includes/config-server-collection-migration-requirements.rst

## Examples

To start the transition to a dedicated config server, use the :method:`db.adminCommand` method to run the :dbcommand:`startTransitionToDedicatedConfigServer` command:

```javascript
db.adminCommand( { startTransitionToDedicatedConfigServer: 1 } )
```

To check the status of the draining operation, use the `getTransitionToDedicatedConfigServerStatus` command:

## Learn More

- :dbcommand:`startTransitionToDedicatedConfigServer`
- :dbcommand:`stopTransitionToDedicatedConfigServer`
- :dbcommand:`commitTransitionToDedicatedConfigServer`
