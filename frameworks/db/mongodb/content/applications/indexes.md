---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/applications/indexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================

# Indexing Strategies

The best indexes for your application depend on several factors, including the kinds of queries you expect, the ratio of reads to writes, and the amount of free memory on your system.

Before building indexes, map out your application's queries and the fields they access. Indexes have a performance cost, but are worth it for frequent queries on large data sets. Consider the frequency of each query and whether it justifies an index.

Profile multiple index configurations against production-representative data to find which performs best. Inspect existing indexes to confirm they support your current and planned queries. Drop indexes that are no longer used.

Generally, MongoDB only uses one index to fulfill most queries. However, each clause of an :query:`$or` query may use a different index.

The following documents introduce indexing strategies:

`Use the ESR (Equality, Sort, Range) Guideline <esr-indexing-guideline>` Arrange compound index keys to optimize equality, sort, and range operations.

`create-indexes-to-support-queries` An index supports a query when it contains all the fields the query scans, greatly improving performance.

`sorting-with-indexes` Use these strategies to specify index field order and support efficient sort queries.

`index-selectivity` Understand how index selectivity affects query performance and design indexes that answer queries efficiently.

`unique-indexes-schema-validation` Combine index properties and schema validation to implement your application design.

## Contents

- Equality, Sort, Range Guideline </tutorial/equality-sort-range-guideline>
- Sort Query Results </tutorial/sort-results-with-indexes>
- Ensure Query Selectivity </tutorial/create-queries-that-ensure-selectivity>
- Unique Indexes and Schema Validation </tutorial/unique-indexes-schema-validation>
