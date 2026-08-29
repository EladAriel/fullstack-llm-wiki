---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.dropSearchIndex.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.885267Z"
---
# db.collection.dropSearchIndex() (mongosh method)

**meta:** :description: Delete an existing {+fts+} index using the `dropSearchIndex()` method in MongoDB Atlas.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

## Definition

**method:** db.collection.dropSearchIndex()

**versionadded:** 7.0 (*Also available starting in 6.0.7*)

.. |fts-index| replace:: :atlas:`{+fts+} index </atlas-search/atlas-search-overview/#fts-indexes>` or :atlas:`{+avs+} index </atlas-vector-search/vector-search-overview/>`

**include:** /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst

.. |dbcommand| replace:: :dbcommand:`dropSearchIndex` command

**include:** /includes/fact-mongosh-shell-method-alt.rst

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst




## Syntax

Command syntax:

.. code-block:: javascript

   db.<collection>.dropSearchIndex(<name>)

## Command Fields

``dropSearchIndex()`` takes the following field:

.. list-table::
  :header-rows: 1
  :widths: 20 20 20 80

  * - Field
    - Type
    - Necessity
    - Description

  * - ``name``
    - string
    - Required
    - Name of the search index to drop.

## Behavior

.. |method-name| replace:: ``dropSearchIndex()``
.. |method-name-title| replace:: ``dropSearchIndex()``

**include:** /includes/atlas-search-commands/behavior/delete-behavior.rst

## Access Control

If your deployment enforces access control, the user running the
``dropSearchIndex()`` method must have the
:authaction:`dropSearchIndex` privilege action on the database:

.. code-block:: javascript

   { resource: { database : true }, actions: [ "dropSearchIndex" ] }

The built-in :authrole:`dbAdmin` and :authrole:`readWrite` roles provide
the ``dropSearchIndex`` privilege. The following example grants the
``readWrite`` role on the ``qa`` database:

.. code-block:: javascript

   db.grantRolesToUser(
      "<user>",
      [ { role: "readWrite", db: "qa" } ]
   )

## Example

The following example deletes a search index named ``searchIndex01`` on
the ``movies`` collection:

.. code-block:: javascript

   db.movies.dropSearchIndex("searchIndex01")