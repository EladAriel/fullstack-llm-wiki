---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/query-predicates/data-type.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.099375Z"
---
.. _query-selectors-data-type:

# Data Type Query Predicate Operators

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

Data type query predicate operators return data based on field existence
or data types. 

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Operator

     - Description

   * - :query:`$exists`

     - Matches documents that have the specified field.

   * - :query:`$type`

     - Matches documents if a field is of the specified type.


**toctree:** :titlesonly: 
   :hidden: 

   $exists </reference/operator/query/exists>
   $type </reference/operator/query/type>