---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getCollectionNames.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.934864Z"
---
# db.getCollectionNames() (mongosh method)

**meta:** :description: Retrieve an array of collection and view names in the current database using `db.getCollectionNames()`, considering user privileges.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** db.getCollectionNames()

   Returns an array containing the names of all collections and
   :ref:`views <views-landing-page>` in the current database, or if running
   with access control, the names of the collections according to user's
   privilege. For details, see :ref:`db.collectionnames-access`.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst


.. _db.collectionnames-access:

## Required Access

**include:** /includes/extracts/listCollections-auth-showCollectionNames.rst

## Behavior

### Client Disconnection

**include:** /includes/extracts/4.2-changes-disconnect.rst

.. |operation| replace:: :method:`db.getCollectionNames()`

### Replica Set Member State Restriction

**include:** /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

.. |operations| replace:: :dbcommand:`listCollections`

## Example

The following returns the names of all collections in the ``records``
database:

.. code-block:: javascript

   use records
   db.getCollectionNames()

The method returns the names of the collections in an array:

.. code-block:: javascript

   [ "employees", "products", "mylogs", "system.indexes" ]