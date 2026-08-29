---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/query-predicates/logical.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.098483Z"
---
.. _query-selectors-logical:

# Logical Query Predicate Operators

**meta:** :description: Learn about logical query operators in MongoDB. The $and, $not, $nor, and $or operators help you build queries based on logical conditions.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

Logical operators return data based on boolean logic (and, or, and nor).

.. list-table::
   :widths: 30,70
   :header-rows: 1

   * - Name

     - Description

   * - :query:`$and`

     - .. include:: /includes/query-predicates/and-desc.rst

   * - :query:`$nor`

     - .. include:: /includes/query-predicates/nor-desc.rst
     
   * - :query:`$not`

     - Inverts the effect of a query predicate and returns documents
       that do *not* match the query predicate.

   * - :query:`$or`

     - .. include:: /includes/query-predicates/or-desc.rst

**toctree:** :titlesonly: 
   :hidden: 

   $and </reference/operator/query/and>
   $nor </reference/operator/query/nor>
   $not </reference/operator/query/not>
   $or </reference/operator/query/or>