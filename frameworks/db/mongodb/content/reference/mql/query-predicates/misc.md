---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/query-predicates/misc.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.099919Z"
---
.. _query-selectors-misc:

# Miscellaneous Query Predicate Operators

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The following operators perform specialized functions in query
predicates.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name

     - Description

   * - :query:`$expr`

     - .. include:: /includes/query-predicates/expr-desc.rst

   * - :query:`$jsonSchema`

     - .. include:: /includes/query-predicates/jsonSchema-desc.rst

   * - :query:`$mod`

     - Matches documents based on the result of a modulo operation on a
       field value.
   
   * - :query:`$regex`

     - Matches documents where values match a specified regular expression.

   * - :query:`$where`

     - Matches documents that satisfy a JavaScript expression.

**toctree:** :titlesonly: 
   :hidden: 

   $expr </reference/operator/query/expr>
   $jsonSchema </reference/operator/query/jsonSchema>
   $mod </reference/operator/query/mod>
   $regex </reference/operator/query/regex>
   $where </reference/operator/query/where>