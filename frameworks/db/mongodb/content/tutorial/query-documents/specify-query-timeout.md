---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/query-documents/specify-query-timeout.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.852871Z"
---
.. _manual-query-timeout:

# Query Timeouts

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1

You can specify a timeout for read operations to complete. If a query
exceeds the specified time limit, MongoDB stops the query and the query
does not return any results.

To prevent ongoing queries from negatively impacting deployment
performance for long periods of time, specify a suitable query timeout
for your application.

For details on how MongoDB stops queries that exceed a specified
timeout, see :ref:`cursor.maxTimeMS Behaviors
<cursor-maxtimems-behaviors>`.

## Specify a Time Limit for Queries

To specify a time limit for a query, perform one of these actions:

- Specify the :method:`~cursor.maxTimeMS()` option for a query. The
  ``maxTimeMS`` option lets you specify a query timeout at the operation
  level, meaning you can specify different time limits for different
  queries.

- Specify a global default time limit for all queries. The
  :parameter:`defaultMaxTimeMS` cluster parameter specifies a default
  time limit for individual read operations to complete, and applies to
  all queries that do not include the :method:`~cursor.maxTimeMS()`
  option. If a query specifies a ``maxTimeMS()`` option, that value
  overrides the ``defaultMaxTimeMS`` value.

## Learn More

- :ref:`tutorial-long-running-queries`

- :ref:`server-diagnose-queries`

- :ref:`cursor-noCursorTimeout`