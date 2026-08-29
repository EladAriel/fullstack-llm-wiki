---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/index-unique/create.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.799095Z"
---
.. _index-unique-index:
.. _index-unique-create:

# Create a Single-Field Unique Index

**facet:** :name: programming_language
   :values: shell 

**facet:** :name: genre 
   :values: tutorial

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

Unique indexes ensure that a value appears at most once for a given
field.

To create a unique index in the MongoDB Shell, use the
:method:`db.collection.createIndex()` method with the ``unique`` option
set to ``true``. 

.. code-block:: javascript

   db.collection.createIndex(
      { <field>: <sortOrder> },
      { unique: true }
    )

## About this Task

This example adds a unique index on the ``user_id`` field of a
``members`` collection to ensure that there are no duplicate values in
the ``user_id`` field.

## Steps

To create a unique index on the ``user_id`` field of the ``members``
collection, run the following command in :binary:`~bin.mongosh`:

.. code-block:: javascript

   db.members.createIndex( { "user_id": 1 }, { unique: true } )

## Learn More

- :ref:`index-unique-compound-index`

- :ref:`index-convert-to-unique`