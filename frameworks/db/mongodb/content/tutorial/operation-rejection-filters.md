---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/operation-rejection-filters.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================================

# Block Slow Queries with Operation Rejection Filters

.. versionadded:: 8.0

To prevent an operation from causing excessive workload, you can temporarily reject all operations associated with that `query shape <query-shapes>`. To do that, use :dbcommand:`setQuerySettings` to set the `reject` field to `true` for the operation's query shape. A rejected query shape is also known as an `operation rejection filter`.

The `query optimizer` uses the query settings as an additional input during query planning, which affects the plan selected to run the query.

The steps on this page create an example collection and use an operation rejection filter to block a query shape.

## About this Task

Assume a cluster has excessive workload because an application has an inefficient query. To prevent the query from consuming excessive cluster resources, use an operation rejection filter to block the query and similar queries from running.

## Before you Begin

To identify an inefficient query, use various methods that include:

- :atlas:`Atlas Monitoring </performance-advisor>`
- :atlas:`Atlas Alerts </alerts>`
- :atlas:`Atlas Query Profiler </tutorial/profile-database>`
- `Log Messages <log-message-slow-ops>`
> **Note:** You can't set an operation rejection filter on Atlas Free or
`Flex <atlas-choose-flex>` clusters.

## Steps

## Next Steps

After you block an inefficient operation using an operation rejection filter, your cluster performance should return to how it was before the inefficient query was introduced. Next steps:

1. Resolve the performance problem with the query. This may require an
index or a query rewrite. #. Deploy the updated application.

To re-enable query settings that aren't deleted, use `setQuerySettings` and set the `reject` field to `false`.

## Learn More

- :dbcommand:`setQuerySettings`
- :dbcommand:`removeQuerySettings`
- :pipeline:`$querySettings`
- `query-shapes`
- `Query Statistics for Query Shapes <queryStats-queryShape>`
- `aggregation-pipeline`
- `query-plans-query-optimization`
- `indexes`
- `Slow Queries <log-message-slow-ops>`
- `Database Profiler <database-profiling-specify-slowms-threshold>`
- :atlas:`Atlas Monitoring </performance-advisor>`
- :atlas:`Atlas Alerts </alerts>`
