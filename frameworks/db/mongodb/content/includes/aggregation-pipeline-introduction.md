---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation-pipeline-introduction.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

An aggregation pipeline consists of one or more `stages <aggregation-pipeline-operator-reference>` that process documents. These documents can come from a collection, a view, or a specially designed stage.

Each stage performs an operation on the input documents. For example, a stage can :expression:`$filter` documents, :pipeline:`$group` documents, and calculate values. The documents that a stage outputs are then passed to the next stage in the pipeline.

An aggregation pipeline can return results for groups of documents. You can also update documents with an aggregation pipeline using the stages shown in `updates-agg-pipeline`.

> **Note:** Aggregation pipelines run with the
:method:`db.collection.aggregate()` method do not modify documents in
a collection, unless the pipeline contains a :pipeline:`$merge` or
:pipeline:`$out` stage.
