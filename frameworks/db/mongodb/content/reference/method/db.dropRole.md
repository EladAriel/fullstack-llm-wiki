---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.dropRole.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.922929Z"
---
# db.dropRole() (mongosh method)

**meta:** :description: Delete a user-defined role from a database using `db.dropRole()` with optional write concern settings.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** db.dropRole( rolename, writeConcern )

   Deletes a :ref:`user-defined <user-defined-roles>` role from the
   database on which you run the method.

   .. |dbcommand| replace:: :dbcommand:`dropRole` command
   .. include:: /includes/fact-mongosh-shell-method-alt.rst

   The :method:`db.dropRole()` method takes the following arguments:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
        - Type
        - Description
      * - ``rolename``
        - string
        - The name of the :ref:`user-defined role <user-defined-roles>` to remove
          from the database.
      * - ``writeConcern``
        - document
        - .. include:: /includes/fact-write-concern-spec-link.rst

   .. |local-cmd-name| replace:: :method:`db.dropRole()`

## Compatibility

This method is available in deployments hosted in the following
environments:

**include:** /includes/fact-environments-no-atlas-support.rst

**include:** /includes/fact-environments-onprem-only.rst

## Behavior

### Authentication

**include:** /includes/behavior-drop-role.rst

### Replica Set

.. |command| replace:: :method:`db.dropRole()`

**include:** /includes/fact-management-methods-write-concern.rst

## Required Access

**include:** /includes/access-drop-role.rst

## Example

The following operations remove the ``readPrices`` role from the
``products`` database:

.. code-block:: javascript

   use products
   db.dropRole( "readPrices", { w: "majority" } )