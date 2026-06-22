---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/map-reduce-examples.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
