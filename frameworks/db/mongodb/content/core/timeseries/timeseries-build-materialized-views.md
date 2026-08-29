---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-build-materialized-views.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.793122Z"
---
.. _manual-timeseries-collection-materialized-views:

# Build Materialized Views on Top of Time Series Data

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

**meta:** :keywords: IOT
   :description: Create materialized views on time series data using the `$merge` aggregation pipeline stage for archiving, analytics, and controlled data access.

Materialized views on time series data are useful for:

- archiving
- analytics
- facilitating data access for teams that cannot access the raw data

To create an :doc:`On-Demand Materialized view
</core/materialized-views>`, use the :pipeline:`$merge` aggregation
pipeline stage to transform and store your data:

.. code-block:: javascript

   db.weather.aggregate([
     {
        $project: {
           date: {
              $dateToParts: { date: "$timestamp" }
           },
           temp: 1
        }
     },
     {
        $group: {
           _id: {
              date: {
                 year: "$date.year",
                 month: "$date.month",
                 day: "$date.day"
              }
           },
           avgTmp: { $avg: "$temp" }
        }
     }, {
        $merge: { into: "dailytemperatureaverages", whenMatched: "replace" }
     }
   ])

The preceding pipeline, will create or update the
``dailytemperatureaverages`` collection with all daily temperature
averages based on the ``weather`` collection.

**note:** It is not possible to natively schedule the refreshing of these
   materialized views.

For more information on materialized views, see
:doc:`/core/materialized-views`.