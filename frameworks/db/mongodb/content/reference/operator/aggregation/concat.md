---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/concat.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.167466Z"
---
# $concat (expression operator)

**meta:** :description: Concatenate strings using the `$concat` operator in MongoDB aggregation, returning `null` for missing or `null` values.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**expression:** $concat

   Concatenates strings and returns the concatenated string.

   ``$concat`` has this syntax:

   .. code-block:: javascript

        { $concat: [ <expression1>, <expression2>, ... ] }

   The arguments can be any valid :ref:`expression
   <aggregation-expressions>` as long as they resolve to
   strings. For more information on expressions, see
   :ref:`aggregation-expressions`.

   If the argument resolves to a value of ``null`` or refers to a field
   that is missing, ``$concat`` returns ``null``.

## Example

Create an ``inventory`` collection with these documents:

.. code-block:: javascript

   db.inventory.insertMany( [
      { _id : 1, item : "ABC1", quarter: "13Q1", description : "product 1" },
      { _id : 2, item : "ABC2", quarter: "13Q4", description : "product 2" },
      { _id : 3, item : "XYZ1", quarter: "14Q2", description : null }
   ] )

Use the ``$concat`` operator to concatenate the ``item`` field and the
``description`` field with a " - " delimiter:

.. code-block:: javascript

   db.inventory.aggregate(
      [
         { $project: { itemDescription: { $concat: [ "$item", " - ", "$description" ] } } }
      ]
   )

Output:

.. code-block:: javascript
   :copyable: false

   { _id : 1, itemDescription : "ABC1 - product 1" }
   { _id : 2, itemDescription : "ABC2 - product 2" }
   { _id : 3, itemDescription : null }