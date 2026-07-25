---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/map-reduce-examples.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================

# Map-Reduce Examples

> **Note:** An `aggregation pipeline <aggregation-pipeline>` provides
better performance and usability than a :doc:`map-reduce
</core/map-reduce>` operation.
Map-reduce operations can be rewritten using :ref:`aggregation
pipeline stages <aggregation-pipeline-operator-reference>` such
as :pipeline:`$group` and :pipeline:`$merge`.
For map-reduce operations that require custom functionality, MongoDB
provides the :group:`$accumulator` and :expression:`$function`
aggregation operators. Use these operators to define custom aggregation
expressions in JavaScript.

In :binary:`~bin.mongosh`, the :method:`db.collection.mapReduce()` method is a wrapper around the :dbcommand:`mapReduce` command. The following examples use the :method:`db.collection.mapReduce()` method.

.. include:: /includes/examples-map-reduce.rst

> **Seealso:** - `incremental-map-reduce`
- `map-reduce-to-agg-pipeline`
