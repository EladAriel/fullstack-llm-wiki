---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.697054Z"
---
.. _mql-reference:

# MongoDB Query Language Reference

**meta:** :description: Reference guide for the MongoDB Query Language, including query predicates, aggregation pipelines, expressions, projections, accumulators, and update operators.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

:abbr:`MQL (MongoDB Query Language)` comprises query predicates,
aggregation pipelines, and other ways to interact with your data.

:ref:`crud-commands-ref`
  Database commands used to perform CRUD operations, including
  aggregation.

:ref:`aggregation-pipeline-operator-reference`
  Aggregation stages used to construct aggregation pipelines.

:ref:`query-predicates-ref`
  Expressions used to indicate whether a document matches a given query.

:ref:`expressions-ref-landing`
  Expressions used in various contexts of MQL including aggregations,
  query predicates, and projections.

:ref:`projection-operators-ref`
  Specialized operators used in find command projections.

:ref:`accumulators-ref`
  Operators used in group stages to return aggregated values from
  multiple input documents.

:ref:`update-operators-ref`
  Operators used to modify documents.


.. TODO: Separate Window Functions in DOCSP-46302
.. :ref:`window-functions-ref`
.. Operators used in :pipeline:`$setWindowFields` stages.

**toctree:** :hidden:

   CRUD Commands </reference/mql/crud-commands>
   Aggregation Stages </reference/mql/aggregation-stages>
   Query Predicates </reference/mql/query-predicates>
   Expressions </reference/mql/expressions>
   Projection </reference/mql/projection>
   Accumulators </reference/mql/accumulators>
   Update </reference/mql/update>
.. Window Functions </reference/mql/window-functions>