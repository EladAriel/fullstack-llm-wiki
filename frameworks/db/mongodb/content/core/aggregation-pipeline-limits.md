---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/aggregation-pipeline-limits.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.532370Z"
---
.. _agg-pipeline-limits:

# Aggregation Pipeline Limits

**meta:** :description: Understand the limitations of MongoDB's aggregation pipeline, including result size, number of stages, and memory usage constraints.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

Aggregation operations with the :dbcommand:`aggregate` command have the
following limitations.

## Result Size Restrictions

The :dbcommand:`aggregate` command can either return a cursor or store
the results in a collection. Each document in the result set is subject
to the 16 mebibyte :limit:`BSON Document Size limit <BSON Document
Size>`. If any single document exceeds the :limit:`BSON Document Size
limit <BSON Document Size>`, the aggregation produces an error. The
limit only applies to the returned documents. During the pipeline
processing, the documents may exceed this size. The
:method:`db.collection.aggregate()` method returns a cursor by default.

.. _stage-restrictions:

## Number of Stages Restrictions

**include:** /includes/fact-agg-stage-limit.rst

.. _agg-memory-restrictions:

## Memory Restrictions

**include:** /includes/fact-agg-memory-limit.rst
