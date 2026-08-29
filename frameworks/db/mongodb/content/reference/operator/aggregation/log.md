---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/log.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.167153Z"
---
# $log (expression operator)

**meta:** :description: Calculate the logarithm of a number in a specified base using the `$log` operator in MongoDB aggregation.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**expression:** $log 

   Calculates the log of a number in the specified base and returns the
   result as a double.

   :expression:`$log` has the following syntax:

   .. code-block:: javascript

      { $log: [ <number>, <base> ] }
   
   The ``<number>`` expression can be any valid :ref:`expression
   <aggregation-expressions>` as long as it resolves to a non-negative number.

   The ``<base>`` expression can be any valid :ref:`expression
   <aggregation-expressions>` as long as it resolves to a positive
   number greater than ``1``.

   For more information on expressions, see :ref:`aggregation-expressions`.

## Behavior

**include:** /includes/agg-expression-double-unless-decimal-behavior.rst

**include:** /includes/extracts/agg-expression-null-operand-log.rst

.. list-table::
   :header-rows: 1
   :widths: 85 15

   * - Example
     - Results

   * - ``{ $log: [ 100, 10 ] }``
     - ``2``

   * - ``{ $log: [ 100, Math.E ] }`` where ``Math.E`` is a JavaScript
       representation for *e*.

     - ``4.605170185988092``

## Example

A collection ``integers`` contains the following documents:

.. code-block:: javascript

   db.integers.insertMany( [
      { _id: 1, int: 5 },
      { _id: 2, int: 2 },
      { _id: 3, int: 23 },
      { _id: 4, int: 10 }
   ] )


The following example uses log\ :sub:`2` in its calculation to
determine the number of bits required to represent the value of
``int``.

.. code-block:: javascript

   db.integers.aggregate([
      { $project: { bitsNeeded:
         {
            $floor: { $add: [ 1, { $log: [ "$int", 2 ] } ] } } }
         }
   ])

The operation returns the following results:

.. code-block:: javascript
   :copyable: false

   { "_id" : 1, "bitsNeeded" : 3 }
   { "_id" : 2, "bitsNeeded" : 2 }
   { "_id" : 3, "bitsNeeded" : 5 }
   { "_id" : 4, "bitsNeeded" : 4 }

**seealso:** - :expression:`$log10`
   - :expression:`$ln`