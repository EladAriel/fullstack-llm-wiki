---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/lte.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.173289Z"
---
.. _lte-aggregation-operator:

# $lte (expression operator)

**meta:** :description: Use the `$lte` operator in MongoDB to compare two values, returning true if the first is less than or equal to the second.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**expression:** $lte

   Compares two values and returns:

   - ``true`` when the first value is *less than or equivalent to* the
     second value.

   - ``false`` when the first value is *greater than* the second
     value.

   .. include:: /includes/extracts/fact-agg-comparison-expression-lte.rst

   :expression:`$lte` has the following syntax:

   .. code-block:: javascript

      { $lte: [ <expression1>, <expression2> ] }

   For more information on expressions, see :ref:`aggregation-expressions`.

## Example

Consider an ``inventory`` collection with the following documents:

**include:** /includes/lt-lte-sample-data.rst

The following operation uses the :expression:`$lte` operator to
determine if ``qty`` is less than or equal to ``250``:

.. code-block:: javascript

   db.inventory.aggregate(
      [
        {
          $project:
             {
               item: 1,
               qty: 1,
               qtyLte250: { $lte: [ "$qty", 250 ] },
               _id: 0
             }
        }
      ]
   )

The operation returns the following results:

.. code-block:: javascript

   { "item" : "abc1", "qty" : 300, "qtyLte250" : false }
   { "item" : "abc2", "qty" : 200, "qtyLte250" : true }
   { "item" : "xyz1", "qty" : 250, "qtyLte250" : true }
   { "item" : "VWZ1", "qty" : 300, "qtyLte250" : false }
   { "item" : "VWZ2", "qty" : 180, "qtyLte250" : true }