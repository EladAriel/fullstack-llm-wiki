---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropRole.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.054861Z"
---
# dropRole (database command)

**meta:** :description: Delete a user-defined role from a database using the `dropRole` command, with optional write concern and comment fields.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** dropRole

   Deletes a :ref:`user-defined <user-defined-roles>` role from the
   database on which you run the command.

   .. |method| replace:: :method:`db.dropRole` helper method
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
        dropRole: "<role>",
        writeConcern: { <write concern> },
        comment: <any>
      }
   )

## Command Fields

The command has the following fields:

.. list-table::
   :header-rows: 1
   :widths: 20 20 80
 
   * - Field
     - Type
     - Description

   * - ``dropRole``
     - string
     - The name of the :ref:`user-defined role <user-defined-roles>` to remove
       from the database.

   * - ``writeConcern``
     - document
     - .. include:: /includes/fact-write-concern-spec-link.rst

   * - ``comment``
     - any
     - .. include:: /includes/extracts/comment-content.rst

## Behavior

### Authentication

**include:** /includes/behavior-drop-role.rst

## Required Access

**include:** /includes/access-drop-role.rst

## Example

The following operations remove the ``readPrices`` role from the
``products`` database:

.. code-block:: javascript

   use products
   db.runCommand(
      {
        dropRole: "readPrices",
        writeConcern: { w: "majority" }
      }
   )