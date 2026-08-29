---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.status.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.957022Z"
---
# rs.status() (mongosh method)

**meta:** :description: Retrieve the current status of a replica set using the `rs.status()` method, reflecting data from heartbeat packets.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** rs.status()

   Returns the replica set status from the point of view of the member
   where the method is run. 

   .. |dbcommand| replace:: :dbcommand:`replSetGetStatus` command
   .. include:: /includes/fact-mongosh-shell-method-alt

   This output reflects the current status of the replica set, using
   data derived from the heartbeat packets sent by the other members
   of the replica set.

## Compatibility

**include:** /includes/fact-environments-atlas-only.rst
**include:** /includes/fact-environments-atlas-support-all.rst
**include:** /includes/fact-environments-onprem-only.rst

## Output

For an example and details on the output, see :ref:`replSetGetStatus
<rs-status-output>`.

If you run the :binary:`~bin.mongosh` helper method :method:`rs.status()` 
(or the :dbcommand:`replSetGetStatus` command) on a member during its 
:ref:`initial sync <replica-set-initial-sync>` (i.e. :replstate:`STARTUP2` 
state), the command returns :data:`replSetGetStatus.initialSyncStatus`
metrics.
      
Once the member completes its initial sync, the
:data:`replSetGetStatus.initialSyncStatus` metrics becomes unavailable.
      