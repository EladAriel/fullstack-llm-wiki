---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-build-materialized-views.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================================

# Build Materialized Views on Top of Time Series Data

Materialized views on time series data are useful for:

- archiving
- analytics
- facilitating data access for teams that cannot access the raw data
To create an `On-Demand Materialized view </core/materialized-views>`, use the :pipeline:`$merge` aggregation pipeline stage to transform and store your data:

```javascript
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
```

The preceding pipeline, will create or update the `dailytemperatureaverages` collection with all daily temperature averages based on the `weather` collection.

> **Note:** It is not possible to natively schedule the refreshing of these
materialized views.

For more information on materialized views, see `/core/materialized-views`.
