---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetGetStatus.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# replSetGetStatus (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     replSetGetStatus: 1 
   } 
)
```

If you run :dbcommand:`replSetGetStatus` or the :binary:`~bin.mongosh` helper :method:`rs.status()` on a member during its `initial sync <replica-set-initial-sync>` (i.e. :replstate:`STARTUP2` state), the command returns `replSetGetStatus.initialSyncStatus` metrics.

After the member completes the initial synchronization and transitions to another state, the `replSetGetStatus.initialSyncStatus` metrics are no longer available.

> **Note:** If you haven't yet :method:`initialized <rs.initiate()>` your replica
set, the `replSetGetStatus` command returns the following error:
.. code-block:: shell
   :copyable: false
   MongoServerError: no replset config has been received
Run the :dbcommand:`replSetInitiate` command and try again.

## Example

## Output

The :command:`replSetGetStatus` command returns a document with the following fields:

See also `command-response` for details on the `ok` status field, the `operationTime` field and the `$clusterTime` field.
