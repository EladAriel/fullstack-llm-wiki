---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.dropAllRoles.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.955932Z"
---
# db.dropAllRoles() (mongosh method)

**meta:** :description: Delete all user-defined roles from a database using `db.dropAllRoles()` with optional write concern.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** db.dropAllRoles( writeConcern )

   Deletes all :ref:`user-defined <user-defined-roles>` roles on the
   database where you run the method.

   .. warning::

      The :method:`db.dropAllRoles()` method removes *all*
      :ref:`user-defined <user-defined-roles>` roles from the database.

   .. |dbcommand| replace:: :dbcommand:`dropAllRolesFromDatabase` command
   .. include:: /includes/fact-mongosh-shell-method-alt.rst

   The :method:`db.dropAllRoles()` method takes the following argument:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Field
        - Type
        - Description
      * - ``writeConcern``
        - document
        - .. include:: /includes/fact-write-concern-spec-link.rst

   .. COMMENT I added the returns here because in the example for this
      method, you have what the method returns.  But we don't specify
      what is returned for the other user/role mgmt methods.

   :returns:
      The number of :ref:`user-defined <user-defined-roles>` roles dropped.

   .. |local-cmd-name| replace:: :method:`db.dropAllRoles()`

## Compatibility

This method is available in deployments hosted in the following
environments:

**include:** /includes/fact-environments-no-atlas-support.rst

**include:** /includes/fact-environments-onprem-only.rst

                                 
## Behavior

### Replica set

.. |command| replace:: :method:`db.dropAllRoles()`

**include:** /includes/fact-management-methods-write-concern.rst

## Required Access

**include:** /includes/access-drop-role.rst

## Example

The following operations drop all :ref:`user-defined
<user-defined-roles>` roles from the ``products`` database and uses a
:ref:`write concern <write-concern-operation>` of ``majority``.

.. code-block:: javascript

   use products
   db.dropAllRoles( { w: "majority" } )

The method returns the number of roles dropped:

.. code-block:: javascript

   4