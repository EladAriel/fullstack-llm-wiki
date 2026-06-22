---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/find-slow-queries-with-database-profiler.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Find Slow Queries

MongoDB includes the `database-profiler`, which can identify slow queries and help you determine how to improve query performance.

## About This Task

### Performance, Storage, and Security

This task uses the database profiler to identify slow queries on a running :program:`mongod` instance. When enabled, the database profiler can affect performance and disk usage and expose unencrypted query data.

> **Warning:** Consider the performance, storage, and security implications
before using the database profiler on a production
deployment.

### Atlas Query Profiler

Atlas users can take advantage of the Atlas Query Profiler to identify slow queries with the convenience of visualization through a scatterplot chart.

For more information, see `query-profiler`.

### Slow Queries

A slow query is one that takes longer than a specified amount of time to run. For this task, the slow query threshold is set to 100 milliseconds.

In some use cases, you may require queries run faster. In others, you may need to raise the threshold to focus only on those queries that are the slowest.

Choose a slow query threshold that reflects your specific application and database needs.

### Context

When enabled, the database profiler monitors queries at a database-level only. If you need the profiler to monitor slow queries on multiple databases, run the :method:`db.setProfilingLevel` method on each database.

### Sharded Clusters

The database profiler is not available through :program:`mongos`.

## Steps

## Examples

### Ignore Indexes

To evaluate performance on a collection with an index, you can set the query to ignore indexes using the :method:`hint( { $natural: 1 } ) <cursor.hint>` method.

```javascript
db.listingsAndReviews.find( {
   $or: [
      { "address.market": "Berlin" },
      { "review_scores.review_scores_cleanliness": { $lt: 5 } }
   ],
   $where: function () {
      return this.amenities && this.amenities.length > 15;
   } 
} ).sort( { description: 1 } ).hint( { $natural: 1 } );
```

You may find this useful in cases where you want to compare how queries perform with a collection scan to that of an index scan.

## Next Steps

- `manual-create-an-index`
## Learn More

- `query-performance`
- `Atlas Query Profiler <query-profiler>`
- `database-profiler`
- `indexes`
