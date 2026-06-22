---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/monitor-slow-queries.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Monitor Slow Queries

The :pipeline:`$currentOp` aggregation stage provides information on all operations currently running on MongoDB. If your application is experiencing performance issues, you can build an aggregation pipeline around this stage to monitor for slow queries and similar issues.

## About This Task

### Database Profilers

This task uses :pipeline:`$currentOp` to identify slow queries currently running on your application. To find all slow queries within a specified period, consider using a profiler.

.. include:: /includes/fact-profiler-use

### Explain Queries

This task identifies queries with performance issues. If you already know which queries have performance issues, see `manual-explain-slow-queries` to troubleshoot them.

## Steps

## Learn More

- `query-performance`
- `profiler`
- `manual-find-slow-queries-with-database-profiler`
- `manual-explain-slow-queries`
