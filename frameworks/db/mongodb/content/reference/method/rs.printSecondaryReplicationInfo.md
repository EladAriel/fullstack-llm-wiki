---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.printSecondaryReplicationInfo.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.002084Z"
---
# rs.printSecondaryReplicationInfo() (mongosh method)

**meta:** :description: Print a formatted report of replica set status from a secondary member's perspective using `rs.printSecondaryReplicationInfo()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** rs.printSecondaryReplicationInfo()

   Prints a formatted report of the :term:`replica set` status from the
   perspective of the :term:`secondary` member of the set. The output is
   identical to :method:`db.printSecondaryReplicationInfo()`.

## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst
**include:** /includes/fact-environments-atlas-support-no-free.rst
**include:** /includes/fact-environments-onprem-only.rst

## Output

.. |method| replace:: :method:`rs.printSecondaryReplicationInfo()`
.. |method-alternative| replace:: :method:`rs.status()`

**include:** /includes/output-printSecondaryReplicationInfo.rst