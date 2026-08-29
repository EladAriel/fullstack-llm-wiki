---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropUser.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.017017Z"
---
# dropUser (database command)

**meta:** :description: Remove a user from a database using the `dropUser` command, specifying optional write concern and comments.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** dropUser

   Removes the user from the database on which you run the command. 

   .. |method| replace:: :method:`db.dropUser` helper method
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
        dropUser: "<user>",
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

   * - ``dropUser``
     - string
     - The name of the user to delete. You must issue the
       :dbcommand:`dropUser` command while using the database where the
       user exists.

   * - ``writeConcern``
     - document
     - .. include:: /includes/fact-write-concern-spec-link.rst

   * - ``comment``
     - any
     - .. include:: /includes/extracts/comment-content.rst

**include:** /includes/check-before-dropping-useradmin.rst

## Required Access

.. |local-cmd-name| replace:: :command:`dropUser`

**include:** /includes/access-drop-user.rst

## Example

The following sequence of operations in :binary:`~bin.mongosh` removes
``reportUser1`` from the ``products`` database:

.. code-block:: javascript

   use products
   db.runCommand( { 
      dropUser: "reportUser1",
      writeConcern: { w: "majority", wtimeout: 5000 }
   } )