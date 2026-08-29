---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/query-predicates/bitwise.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.098761Z"
---
.. _query-selectors-bitwise:

# Bitwise Query Predicate Operators

Bitwise operators return data based on bit position conditions.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name

     - Description

   * - :query:`$bitsAllClear`

     - Matches numeric or binary values in which a set of bit positions *all* have a value of ``0``.

   * - :query:`$bitsAllSet`

     - Matches numeric or binary values in which a set of bit positions *all* have a value of ``1``.

   * - :query:`$bitsAnyClear`

     - Matches numeric or binary values in which *any* bit from a set of bit positions has a value of ``0``.

   * - :query:`$bitsAnySet`

     - Matches numeric or binary values in which *any* bit from a set of bit positions has a value of ``1``.


**toctree:** :titlesonly: 
   :hidden: 

   $bitsAllClear </reference/operator/query/bitsAllClear>
   $bitsAllSet </reference/operator/query/bitsAllSet>
   $bitsAnyClear </reference/operator/query/bitsAnyClear>
   $bitsAnySet </reference/operator/query/bitsAnySet>