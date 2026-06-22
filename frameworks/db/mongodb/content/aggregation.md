---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/aggregation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# Aggregation Operations

Aggregation operations process multiple documents and return computed results. You can use aggregation operations to:

- Group values from multiple documents.
- Compute a single result from the grouped data.
- Analyze data changes over time.
- Query the most up-to-date version of your data.
The aggregation operators in MongoDB let you run analytics on your cluster without moving data to another platform.

## Get Started

To perform aggregation operations, you can use:

- `Aggregation pipelines <aggregation-pipeline-intro>`, the
preferred method.

- :ref:`Single purpose aggregation methods
<single-purpose-agg-methods>`, which have less functionality than an aggregation pipeline.

## Aggregation Pipelines

.. include:: /includes/aggregation-pipeline-introduction.rst

### Aggregation Pipeline Example

.. include:: /includes/sample-data-usage.rst

The following pipeline finds the top three directors who have directed the most movies in the database.

Use a :pipeline:`$match` stage to filter to movies that have directors listed (excluding documents where the directors field is null or empty):

The `$match` stage reduces the number of documents in our pipeline by filtering out movies without director information. Next, use :pipeline:`$unwind` to deconstruct the directors array so you can count movies per individual director:

Use :pipeline:`$group` to group documents by director name and count each director's movies:

Use :pipeline:`$sort` to order the remaining documents in descending order by movie count:

Use :pipeline:`$limit` to return the top three directors:

The full pipeline:

The pipeline returns these results:

For runnable examples containing sample input documents, see `aggregation-pipeline-examples`.

To learn more about aggregation pipelines, see `aggregation-pipeline`.

## Single Purpose Aggregation Methods

Single purpose aggregation methods aggregate documents from a single collection. These methods have less functionality than an aggregation pipeline.

## Contents

- Aggregation Pipeline </core/aggregation-pipeline>
- Reference </reference/aggregation>
- Map-Reduce </core/map-reduce>
