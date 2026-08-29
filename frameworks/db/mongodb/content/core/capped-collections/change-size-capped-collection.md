---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/change-size-capped-collection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.784043Z"
---
.. _capped-collections-change-size:

# Change the Size of a Capped Collection

**meta:** :description: Modify the size of a capped collection using the `collMod` command with the `cappedSize` option in MongoDB.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

**facet:** :name: genre
   :values: tutorial

**versionadded:** 6.0

To change the size of a :ref:`capped collection
<manual-capped-collection>`, use the :dbcommand:`collMod` command's
``cappedSize`` option. ``cappedSize`` is specified in bytes, and must be
greater than ``0`` and less than or equal to ``1024^5`` (1 {+pb+}).

If ``cappedSize`` is less than the current size of the collection,
MongoDB removes the excess documents on the next insert operation.

## About this Task

**include:** /includes/capped-collections/use-ttl-index.rst

## Before you Begin

Create a capped collection called ``log`` that has a maximum size of
2,621,440 bytes:

.. code-block:: javascript

   db.createCollection( "log", { capped: true, size: 2621440 } )

## Steps

Run the following command to set the maximum size of the ``log``
collection to 5,242,880 bytes:

.. code-block:: javascript

   db.runCommand( { collMod: "log", cappedSize: 5242880 } )

## Learn More

- :ref:`capped-collections-change-max-docs`

- :ref:`capped-collections-check`

- :ref:`capped-collections-query`