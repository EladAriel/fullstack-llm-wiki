---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/ping.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.097629Z"
---
.. _ping-database-command:

# ping (database command)

**meta:** :description: Use the `ping` command to test server responsiveness in MongoDB environments, including Atlas, Enterprise, and Community versions.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** ping

   The :dbcommand:`ping` command is a no-op used to test whether a
   server is responding to commands. This command will return
   immediately even if the server is write-locked:

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
        ping: 1 
      }
   )

The value (e.g. ``1`` above) does not impact the behavior of the
command.