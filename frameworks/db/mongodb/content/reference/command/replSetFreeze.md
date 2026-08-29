---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetFreeze.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.057564Z"
---
# replSetFreeze (database command)

**meta:** :description: Prevent a replica set member from seeking election for a specified time using the `replSetFreeze` command.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** replSetFreeze

   The :dbcommand:`replSetFreeze` command prevents a replica set
   member from seeking election for the specified number of
   seconds. Use this command in conjunction with the
   :dbcommand:`replSetStepDown` command to make a different node in
   the replica set a primary.

   .. |method| replace:: :method:`rs.freeze` helper method
   .. include:: /includes/fact-dbcommand-tip

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-onprem-only.rst

**include:** /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

.. code-block:: javascript

   db.runCommand(
      {   
        replSetFreeze: <seconds> 
      }
   )

## Behavior

If you want to unfreeze a replica set member before the specified number
of seconds has elapsed, you can issue the command with a seconds
value of ``0``:

.. code-block:: javascript

   db.runCommand(
      { 
        replSetFreeze: 0 
      }
   )

Restarting the :binary:`~bin.mongod` process also unfreezes a replica
set member.

:dbcommand:`replSetFreeze` is an administrative command, and you
must issue it against the :term:`admin database`.

.. slave-ok, admin-only