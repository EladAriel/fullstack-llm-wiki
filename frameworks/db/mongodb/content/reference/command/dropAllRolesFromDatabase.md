---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropAllRolesFromDatabase.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.076515Z"
---
# dropAllRolesFromDatabase (database command)

**meta:** :description: Delete all user-defined roles from a database using the `dropAllRolesFromDatabase` command.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** dropAllRolesFromDatabase

   Deletes all :ref:`user-defined <user-defined-roles>` roles
   on the database where you run the command.

   .. warning::

      The :dbcommand:`dropAllRolesFromDatabase` removes *all*
      :ref:`user-defined <user-defined-roles>` roles from the database.

   .. |method| replace:: :method:`db.dropAllRoles` helper method
   .. include:: /includes/fact-dbcommand-tip

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

.. code-block:: javascript

  db.runCommand(
     {
       dropAllRolesFromDatabase: 1,
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

   * - ``dropAllRolesFromDatabase``
     - integer
     - Specify ``1`` to drop all :ref:`user-defined <user-defined-roles>`
       roles from the database where the command is run.

   * - ``writeConcern``
     - document
     - /includes/source/fact-write-concern-spec-link.rst

   * - ``comment``
     - any
     - .. include:: /includes/extracts/comment-content.rst

## Required Access

**include:** /includes/access-drop-role.rst

## Example

The following operations drop all :ref:`user-defined
<user-defined-roles>` roles from the ``products`` database:

.. code-block:: javascript

   use products
   db.runCommand(
      {
        dropAllRolesFromDatabase: 1,
        writeConcern: { w: "majority" }
      }
   )

The ``n`` field in the results document reports the number of roles
dropped:

.. code-block:: javascript

   { "n" : 4, "ok" : 1 }