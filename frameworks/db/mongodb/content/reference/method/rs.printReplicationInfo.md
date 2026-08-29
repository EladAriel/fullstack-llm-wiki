---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.printReplicationInfo.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.922595Z"
---
# rs.printReplicationInfo() (mongosh method)

**meta:** :description: Use `rs.printReplicationInfo()` to print a formatted report of a replica set member's oplog for manual inspection.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** rs.printReplicationInfo()

   Prints a formatted report of the replica set member's :term:`oplog`.
   The displayed report formats the data returned by
   :method:`db.getReplicationInfo()`.  The output of
   :method:`rs.printReplicationInfo()` is identical to that of
   :method:`db.printReplicationInfo()`.

   .. |method| replace:: :method:`rs.printReplicationInfo()`
   .. |method-alternative| replace:: :method:`db.getReplicationInfo()`

   .. include:: /includes/note-method-does-not-return-json.rst

**include:** /includes/output-printReplicationInfo.rst

## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst
**include:** /includes/fact-environments-atlas-support-no-free.rst
**include:** /includes/fact-environments-onprem-only.rst