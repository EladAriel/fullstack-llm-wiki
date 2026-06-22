---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/setWindowFields.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# $setWindowFields (aggregation stage)

## Definition

.. versionadded:: 5.0

Performs operations on a specified span of documents in a collection, known as a window, and returns the results based on the chosen `window operator <setWindowFields-window-operators>`.

.. include:: /includes/setWindowFields-introduction-examples.rst

## Syntax

The :pipeline:`$setWindowFields` stage syntax:

```none
{
   $setWindowFields: {
      partitionBy: <expression>,
      sortBy: {
         <sort field 1>: <sort order>,
         <sort field 2>: <sort order>,
         ...,
         <sort field n>: <sort order>
      },
      output: {
         <output field 1>: {
            <window operator>: <window operator parameters>,
            window: {
               documents: [ <lower boundary>, <upper boundary> ],
               range: [ <lower boundary>, <upper boundary> ],
               unit: <time unit>
            }
         },
         <output field 2>: { ... },
         ...
         <output field n>: { ... }
      }
   }
}
```

The :pipeline:`$setWindowFields` stage takes a document with these fields:

> **Seealso:** `setWindowFields-examples`

## Behavior

The :pipeline:`$setWindowFields` stage appends new fields to existing documents. You can include one or more :pipeline:`$setWindowFields` stages in an aggregation operation.

.. include:: /includes/setWindowFields-and-transactions-snapshots.rst

The `$setWindowFields` stage doesn't guarantee the order of the returned documents.

## Window Operators

.. include:: /includes/setWindowFields-operators.rst

## Explain Output

.. versionadded:: 8.3

If you run :dbcommand:`explain` on a `$setWindowsFields` operation, the output contains a `peakTrackedMemBytes` field that contains the maximum number of bytes of tracked memory in use. For more information, see `explain.executionStats.peakTrackedMemBytes`.

## Restrictions

Restrictions for the :pipeline:`$setWindowFields` stage:

- Before MongoDB 5.3, the :pipeline:`$setWindowFields`
stage cannot be used:

- Within `transactions <transactions>`.
- With :readconcern:`"snapshot"` read concern.
- `sortBy <setWindowFields-sortBy>` is required for:
- `Rank <setWindowFields-rank-operators>` and :ref:`order
<setWindowFields-order-operators>` window operators.

- Bounded windows (either a :ref:`documents
<setWindowFields-documents>` window or a `range <setWindowFields-range>` window).

- :group:`$linearFill` operator.
- `Range <setWindowFields-range>` windows require all :ref:`sortBy
<setWindowFields-sortBy>` values to be numbers.

- `Time range <setWindowFields-unit>` windows require all
`sortBy <setWindowFields-sortBy>` values to be dates.

- `Range <setWindowFields-range>` and :ref:`time range
<setWindowFields-unit>` windows can only contain one `sortBy <setWindowFields-sortBy>` field and the sort must be ascending.

- You cannot specify both a `documents <setWindowFields-documents>`
window and a `range <setWindowFields-range>` window.

- These operators use an implicit window and return an error if you
specify a `window <setWindowFields-window>` option:

- `Rank <setWindowFields-rank-operators>` operators.
- :group:`$shift` operator.
- For `range <setWindowFields-range>` windows, only numbers in
the specified range are included in the window. Missing, undefined, and `null` values are excluded.

- For `time range <setWindowFields-unit>` windows:
- Only date and time types are included in the window.
- Numeric boundary values must be integers. For example, you can use 2
hours as a boundary but you cannot use 1.5 hours.

- For empty windows or windows with incompatible values (for example,
using :group:`$sum` on strings), the returned value depends on the operator:

- For :group:`$count` and :group:`$sum`, the returned value is `0`.
- For :group:`$addToSet` and :group:`$push`, the returned value is an
empty array.

- For all other operators, the returned value is `null`.
## Examples

> **Seealso:** .. include:: /includes/fact-timeseries-example-aggregation-book.rst
