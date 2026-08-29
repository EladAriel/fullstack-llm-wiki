---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/query-predicates/arrays.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.100185Z"
---
.. _query-selectors-arrays:
.. _operator-query-array:

# Array Query Predicate Operators

Array operators return data based on array conditions.

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

   * - :query:`$all`

     - Matches arrays that contain all elements specified in the query.

   * - :query:`$elemMatch`

     - .. include:: /includes/query-predicates/elemMatch-desc.rst

   * - :query:`$size`

     - .. include:: /includes/query-predicates/size-desc.rst


**toctree:** :titlesonly: 
   :hidden: 

   $all </reference/operator/query/all>
   $elemMatch </reference/operator/query/elemMatch>
   $size </reference/operator/query/size>

For examples on querying array fields, see:

- :ref:`read-operations-arrays`

- :ref:`array-match-embedded-documents`