---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetAbortPrimaryCatchUp.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.052965Z"
---
# replSetAbortPrimaryCatchUp (database command)

**meta:** :description: Force the elected primary in a replica set to abort sync and complete the transition to primary using the `replSetAbortPrimaryCatchUp` command.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** replSetAbortPrimaryCatchUp

   The ``replSetAbortPrimaryCatchUp`` command forces the elected
   :term:`primary` member of the replica set to abort sync (catch up)
   then complete the transition to primary. 

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

.. code-block:: javascript
   
   db.runCommand(
      { 
        replSetAbortPrimaryCatchUp: 1 
      }
   )