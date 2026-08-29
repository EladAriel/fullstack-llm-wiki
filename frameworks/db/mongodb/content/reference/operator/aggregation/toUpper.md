---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toUpper.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.115518Z"
---
# $toUpper  (expression operator)

**meta:** :description: Convert strings to uppercase using the `$toUpper` aggregation operator, which returns an empty string for null values.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**expression:** $toUpper

   Converts a string to uppercase, returning the result.

   :expression:`$toUpper` has the following syntax:

   .. code-block:: javascript

      { $toUpper: <expression> }

   The argument can be any :ref:`expression <aggregation-expressions>`
   as long as it resolves to a string. For more information on
   expressions, see :ref:`aggregation-expressions`.

   If the argument resolves to null, :expression:`$toUpper` returns an
   empty string ``""``.

## Behavior

.. |exp-has| replace:: :expression:`$toUpper` only has

**include:** /includes/intro-aggregation-string.rst

## Example

Consider a ``inventory`` collection with the following documents:

**include:** /includes/toLower-toUpper-sample-data.rst

The following operation uses the :expression:`$toUpper` operator to return
uppercase ``item`` and uppercase ``description`` values:

.. code-block:: javascript

   db.inventory.aggregate(
      [
        {
          $project:
            {
              item: { $toUpper: "$item" },
              description: { $toUpper: "$description" }
            }
        }
      ]
   )

The operation returns the following results:

.. code-block:: javascript
   :copyable: false

   { _id: 1, item: "ABC1", description: "PRODUCT 1" }
   { _id: 2, item: "ABC2", description: "PRODUCT 2" }
   { _id: 3, item: "XYZ1", description: "" }