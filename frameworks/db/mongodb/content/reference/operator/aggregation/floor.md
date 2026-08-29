---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/floor.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.192383Z"
---
# $floor (expression operator)

**meta:** :description: Use the `$floor` operator in MongoDB to return the largest integer less than or equal to a specified number in aggregation queries.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**expression:** $floor

   Returns the largest integer less than or equal to the specified
   number.

   :expression:`$floor` has the following syntax:

   .. code-block:: javascript

      { $floor: <number> }

   The ``<number>`` expression can be any valid :ref:`expression
   <aggregation-expressions>` as long as it resolves to a number. For
   more information on expressions, see :ref:`aggregation-expressions`.

## Behavior

**include:** /includes/extracts/agg-expression-null-operand-floor.rst

.. list-table::
   :header-rows: 1
   :widths: 85 15

   * - Example
     - Results

   * - ``{ $floor: 1 }``
     - ``1``

   * - ``{ $floor: 7.80 }``
     - ``7``

   * - ``{ $floor: -2.8 }``
     - ``-3``

## Example

Create a collection named ``samples`` with the following documents:

.. code-block:: javascript

   db.samples.insertMany(
      [
         { _id: 1, value: 9.25 },
         { _id: 2, value: 8.73 },
         { _id: 3, value: 4.32 },
         { _id: 4, value: -5.34 }
      ]
   )

The following example returns both the original value and the floor
value:

.. code-block:: javascript

   db.samples.aggregate([
      { $project: { value: 1, floorValue: { $floor: "$value" } } }
   ])

The operation returns the following results:

.. code-block:: javascript

   { "_id" : 1, "value" : 9.25, "floorValue" : 9 }
   { "_id" : 2, "value" : 8.73, "floorValue" : 8 }
   { "_id" : 3, "value" : 4.32, "floorValue" : 4 }
   { "_id" : 4, "value" : -5.34, "floorValue" : -6 }