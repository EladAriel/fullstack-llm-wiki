---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/explain-slow-queries.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Explain Slow Queries

The :method:`~db.collection.explain` method provides information on how MongoDB plans and executes the given query. You may find this information useful when troubleshooting query performance and planning optimizations.

## About This Task

### Explain Queries

The :method:`~db.collection.explain` method is available to queries that use the following methods:

.. include:: /includes/fact-explain-methods-support

### Profilers

This task runs the :method:`~db.collection.explain` method on a sample query in an attempt to identify performance issues. In practice, it may be difficult to run `explain()` on every query your application runs.

To narrow the list of queries to analyze to only those that are slow, you can use a profiler:

.. include:: /includes/fact-profiler-use

## Steps

## Learn More

- `query-performance`
- `Atlas Query Profiler <query-profiler>`
- `database-profiler`
