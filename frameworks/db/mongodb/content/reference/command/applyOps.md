---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/applyOps.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.055173Z"
---
# applyOps (database command)

**meta:** :description: Execute the `applyOps` command to apply specified oplog entries to a `mongod` instance, requiring a global write lock.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** applyOps

   Applies specified :term:`oplog` entries to a :binary:`~bin.mongod`
   instance. The :dbcommand:`applyOps` command is an internal
   command.

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-onprem-only.rst

## Behavior

**include:** /includes/warning-blocking-global.rst

## Required Access

If the specified :term:`oplog` entries contain
:ref:`collection UUIDs <collections-uuids>`, executing this command
requires both the :authaction:`useUUID` and :authaction:`forceUUID`
privileges on the cluster resource to which the oplog entries are
attempting to be written.

.. write-lock

.. see: DOCS-133; SERVER-4259