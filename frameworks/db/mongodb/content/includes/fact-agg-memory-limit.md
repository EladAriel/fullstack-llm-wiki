---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-agg-memory-limit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

$sort from 10% to 100 MB.

Starting in MongoDB 6.0, the :parameter:`allowDiskUseByDefault` parameter controls whether pipeline stages that require more than 100 megabytes of memory to execute write temporary files to disk by default.

- If :parameter:`allowDiskUseByDefault` is set to `true`, pipeline
stages that require more than 100 megabytes of memory to execute write temporary files to disk by default. You can disable writing temporary files to disk for specific `find` or `aggregate` commands using the `{ allowDiskUse: false }` option.

- If :parameter:`allowDiskUseByDefault` is set to `false`, pipeline
stages that require more than 100 megabytes of memory to execute raise an error by default. You can enable writing temporary files to disk for specific `find` or `aggregate` using the `{ allowDiskUse: true }` option.

The :pipeline:`$search` aggregation stage is not restricted to 100 megabytes of RAM because it runs in a separate process.

Examples of stages that can write temporary files to disk when `allowDiskUse <aggregate-cmd-allowDiskUse>` is `true` are:

- :pipeline:`$bucket`
- :pipeline:`$bucketAuto`
- :pipeline:`$group`
- :pipeline:`$setWindowFields`
- :pipeline:`$sort` when the sort operation is not supported by an
index

- :pipeline:`$sortByCount`
> **Note:** Pipeline stages operate on streams of documents with each pipeline
stage taking in documents, processing them, and then outputting the
resulting documents.
Some stages can't output any documents until they have processed all
incoming documents. These pipeline stages must keep their stage
output in RAM until all incoming documents are processed. As a
result, these pipeline stages may require more space than the 100 MB
limit.

If the results of one of your :pipeline:`$sort` pipeline stages exceed the limit, consider `adding a $limit stage <sort-limit-sequence>`.

.. include:: /includes/extracts/4.2-changes-usedDisk.rst
