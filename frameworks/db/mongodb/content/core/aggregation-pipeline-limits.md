---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/aggregation-pipeline-limits.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# Aggregation Pipeline Limits

Aggregation operations with the :dbcommand:`aggregate` command have the following limitations.

## Result Size Restrictions

The :dbcommand:`aggregate` command can either return a cursor or store the results in a collection. Each document in the result set is subject to the 16 mebibyte :limit:`BSON Document Size limit <BSON Document Size>`. If any single document exceeds the :limit:`BSON Document Size limit <BSON Document Size>`, the aggregation produces an error. The limit only applies to the returned documents. During the pipeline processing, the documents may exceed this size. The :method:`db.collection.aggregate()` method returns a cursor by default.

## Number of Stages Restrictions

.. include:: /includes/fact-agg-stage-limit.rst

## Memory Restrictions

.. include:: /includes/fact-agg-memory-limit.rst
