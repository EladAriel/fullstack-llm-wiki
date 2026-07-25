---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/explain-slow-queries.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
