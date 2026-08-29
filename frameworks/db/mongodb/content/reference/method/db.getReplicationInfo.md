---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getReplicationInfo.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.988926Z"
---
# db.getReplicationInfo() (mongosh method)

**meta:** :description: Retrieve the status of a replica set using `db.getReplicationInfo()` to diagnose replication issues.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** db.getReplicationInfo()

   Returns a document with the status of the replica set, using data
   polled from the :term:`oplog`. Use this output when diagnosing
   issues with replication.
   
## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst


## Output

**data:** db.getReplicationInfo().logSizeMB

   Returns the total size of the :term:`oplog` in megabytes. This refers
   to the total amount of space allocated to the oplog rather than the
   current size of operations stored in the oplog.

   .. include:: /includes/fact-oplog-size.rst

**data:** db.getReplicationInfo().usedMB

   Returns the total amount of space used by the :term:`oplog` in
   megabytes. This refers to the total amount of space currently used by
   operations stored in the oplog rather than the total amount of space
   allocated.

**data:** db.getReplicationInfo().errmsg

   Returns an error message if there are no entries in the oplog.

**data:** db.getReplicationInfo().oplogMainRowCount

   Only present when there are no entries in the oplog. Reports the
   number of items or rows in the :term:`oplog` (e.g. ``0``).

**data:** db.getReplicationInfo().timeDiff

   Returns the difference between the first and
   last operation in the :term:`oplog`, represented in seconds.

   Only present if there are entries in the oplog.

**data:** db.getReplicationInfo().timeDiffHours

   Returns the difference between the first and last
   operation in the :term:`oplog`, rounded and represented in hours.

   Only present if there are entries in the oplog.

**data:** db.getReplicationInfo().tFirst

   Returns a timestamp for the first (i.e. earliest)
   operation in the :term:`oplog`. Compare this value to the last write
   operation issued against the server.

   Only present if there are entries in the oplog.

**data:** db.getReplicationInfo().tLast

   Returns a timestamp for the last (i.e. latest)
   operation in the :term:`oplog`. Compare this value to the last write
   operation issued against the server.

   Only present if there are entries in the oplog.

**data:** db.getReplicationInfo().now

   Returns a timestamp that reflects the current time.
   The shell process generates this value, and the datum may differ
   slightly from the server time if you're connecting from a remote host
   as a result. Equivalent to :method:`Date()`.

   Only present if there are entries in the oplog.