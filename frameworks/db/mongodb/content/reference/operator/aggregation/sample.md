---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/sample.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $sample (aggregation stage)

## Definition

## Behavior

If all of the following conditions are true, :pipeline:`$sample` uses a pseudo-random cursor to select the `N` documents:

- :pipeline:`$sample` is the first stage of the pipeline.
- `N` is less than 5% of the total documents in the collection.
> **Note:**   You can't configure the threshold that :pipeline:`$sample` uses to
  determine when to scan the entire collection. The thresholds is 5%.
  If the size is greater than 5% of the total number of documents in
  the collection, :pipeline:`$sample` performs a
  `top-k <sort-limit-results>` sort by a generated random value.
  The top-k sort could spill to disk if the sample documents are
  larger than 100MB.

- The collection contains more than 100 documents.
If any of the previous conditions are false, :pipeline:`$sample`:

- Reads all documents that are output from a preceding aggregation
stage or a collection scan.

- Performs a random sort to select `N` documents. Random sorts are
subject to the `sort memory restrictions <sort-memory-limit>`.

> **Note:**   `Views <views-landing-page>` are the result of aggregation
  pipelines. When you use `$sample` on a view, MongoDB appends the stage
  to the end of the view's aggregation pipeline syntax. Therefore, the
  `$sample` stage on a view is never the first stage and always
  results in a collection scan.

If you use `$sample` in a `sharded cluster`, each shard performs the sample operation independently. :binary:`~bin.mongos` samples the merged result of each shard's sample operation and returns the requested number of documents.

## Examples
