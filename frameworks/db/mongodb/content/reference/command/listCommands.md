---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/listCommands.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.060311Z"
---
# listCommands (database command)

**meta:** :description: Generate a list of all database commands available for the current `mongod` or `mongos` instance using the `listCommands` command.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** listCommands

   The :dbcommand:`listCommands` command generates a list of all
   database commands implemented for the current :binary:`~bin.mongod` or
   :binary:`~bin.mongos` instance.

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
        listCommands: 1 
      } 
   )

.. slave-ok