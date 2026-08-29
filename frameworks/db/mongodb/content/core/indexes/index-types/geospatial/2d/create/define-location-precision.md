---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2d/create/define-location-precision.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.847375Z"
---
.. _2d-index-define-location-precision:

# Define Location Precision for a 2d Index

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

In a 2d index, location precision is defined by the size in bits of the
:term:`geohash` values used to store the indexed data. By default, 2d
indexes use 26 bits of precision, which is equivalent to approximately
two feet (60 centimeters).

Location precision affects performance for insert and read operations.

To change the default precision, specify a ``bits`` value when you
create the 2d index. You can specify a ``bits`` value between 1 and 32,
inclusive.

.. code-block:: javascript

   db.<collection>.createIndex(
      { <location field>: "2d" },
      { bits: <bit precision> }
   )

## About this Task

Location precision affects query performance:

- Lower precision improves performance for insert and update operations,
  and uses less storage.

- Higher precision improves performance for read operations because
  queries scan smaller portions of the index to return results.

Location precision does not affect query accuracy. Grid coordinates are
always used in the final query processing.

## Before You Begin

**include:** /includes/indexes/2d-sample-docs.rst

## Procedure

Create a 2d index on the ``address`` field. Specify a location precision
of ``32`` bits:

.. code-block:: javascript

   db.contacts.createIndex(
      { address: "2d" },
      { bits: 32 }
   )

## Next Steps

**include:** /includes/indexes/2d-index-create-next-steps.rst

## Learn More

- :ref:`geospatial-indexes-geohash`

- :ref:`geospatial-geometry`

- :ref:`geospatial-legacy`