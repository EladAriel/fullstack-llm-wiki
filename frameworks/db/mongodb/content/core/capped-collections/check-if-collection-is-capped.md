---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/check-if-collection-is-capped.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.784615Z"
---
.. _capped-collections-check:

# Check if a Collection is Capped

**meta:** :description: Determine if a collection is capped using the `isCapped()` method in MongoDB.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

**facet:** :name: genre
   :values: tutorial

To check if a collection is capped, use the
:method:`~db.collection.isCapped()` method.

## About this Task

**include:** /includes/capped-collections/use-ttl-index.rst

## Before you Begin

Create a non-capped collection and a capped collection:

.. code-block:: javascript

   db.createCollection("nonCappedCollection1")

   db.createCollection("cappedCollection1", { capped: true, size: 100000 } )
   
## Steps

To check if the collections are capped, use the
:method:`~db.collection.isCapped()` method:

.. io-code-block::
    :copyable: true

    .. input::
        :language: javascript

        db.nonCappedCollection1.isCapped()

        db.cappedCollection1.isCapped()

    .. output::
        :language: javascript

        false
        true

## Learn More

- :ref:`capped-collections-create`

- :ref:`capped-collections-convert`

- :pipeline:`$collStats`