---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/query.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Query Performance

Optimize your MongoDB queries to ensure the best possible performance for your application. This can occur both during development and later, as your data usage and demand changes. As collections grow, a periodic review of query performance can help determine when clusters need to scale up or scale out.

## Behavior

When you send a query to MongoDB, the server interprets the query, builds a query plan to determine how best to retrieve the data, executes the plan, then returns the results to the client.

To improve query performance, consider how MongoDB builds and executes the plan for your specific queries and identify problem areas, such as fields that would benefit from an index, inefficient filters, and issues at scale.

### Indexes

Indexes store values from individual fields or sets of fields from a collection in a separate data structure. In read operations, they allow MongoDB to search in the index to identify relevant documents instead of the entire collection. In write operations, MongoDB must both write the change to the collection and update the index.

In many cases the use of indexes can speed up your query. This improvement depends on which fields are indexed and what your queries use for filters. For example, if a query applies no projections or filters, a collection scan can be more efficient than an index scan.

For more information, see `indexes`.

## Tasks

### Troubleshooting

- `manual-find-slow-queries-with-database-profiler`
- `manual-monitor-slow-queries`
- `manual-explain-slow-queries`
### Solutions

- `manual-create-an-index`
## Details

### Atlas Query Profiler

The Atlas Query Profiler helps diagnose and monitor slow-running queries using log data from your cluster. It aggregates, filters, and visualizes performance statistics in a scatterplot chart through the Query Insights interface.

You may find this visualization more convenient in identifying slow queries and performance outliers than the `manual-qp-database-profiler`.

With the Query Profiler, you get a macro view of your application load. This can help you identify which queries are slow and provide some insights into how you can improve their performance, such as:

- How long the query takes to run
- The number of documents examined by the query
- Whether the query uses an index
For more information, see `query-profiler`.

### Database Profiler

The database profiler collects detailed information about the queries that run on MongoDB, which it stores in the capped `system.profile <<database>.system.profile>` collection.

> **Important:** The database profiler can affect database performance and
disk usage. Consider the performance and storage implications
before enabling it on a production deployment.
For more information, see `database-profiling-overhead`.

With the database profiler, you get a micro view of slow queries in the current application load. This can provide some insights into how you can improve query performance, such as:

- How long the query takes to run
- The number of documents examined by the query
- Whether the query uses an index
For more information, see `profiler`.

> **Note:** The database profiler is not available on :program:`mongos`.
If you need to find slow queries on a sharded cluster, see
`manual-qp-currentOp`.

### Monitor Current Operations

The :pipeline:`$currentOp` aggregation stage returns information on operations currently running on a MongoDB server or cluster. `$currentOp` can help you identify performance issues, such as:

- How long the query takes to run
- Whether the query is waiting on a lock
- Whether the query uses an index
For more information, see `manual-monitor-slow-queries`.

### Explain

The :method:`~db.collection.explain` method retrieves query plan information and execution statistics on queries and aggregation pipelines. It is available for use with these query methods:

.. include:: /includes/fact-explain-methods-support

The :method:`~db.collection.explain` method can help you to identify potential issues with specific queries, such as:

- Inefficient filters
- Ineffective index usage
- Potential performance issues at scale
For more information, see `manual-explain-slow-queries`.

### Collection Stats

The :pipeline:`$collStats` aggregation stage provides statistical information on specific collections and their usage. You may find this useful in identifying index and performance issues.

This can provide useful information, such as:

- Storage usage for the collection and its indexes
- The average size of documents
### Index Stats

The :pipeline:`$indexStats` aggregation stage provides statistical information on index usage by a collection. This can help you identify specific index usage issues, such as:

- Whether queries use the index and how often
- Whether an index is redundant
## Learn More

- `Atlas Query Profiler <query-profiler>`
- `profiler`
- `indexes`
- :method:`db.collection.explain`
- :pipeline:`$collStats`
- :pipeline:`$indexStats`
