---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation-pipeline-introduction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

An aggregation pipeline consists of one or more `stages <aggregation-pipeline-operator-reference>` that process documents. These documents can come from a collection, a view, or a specially designed stage.

Each stage performs an operation on the input documents. For example, a stage can :expression:`$filter` documents, :pipeline:`$group` documents, and calculate values. The documents that a stage outputs are then passed to the next stage in the pipeline.

An aggregation pipeline can return results for groups of documents. You can also update documents with an aggregation pipeline using the stages shown in `updates-agg-pipeline`.

> **Note:** Aggregation pipelines run with the
:method:`db.collection.aggregate()` method do not modify documents in
a collection, unless the pipeline contains a :pipeline:`$merge` or
:pipeline:`$out` stage.
