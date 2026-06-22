---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-quick-start.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Time Series Quick Start

Configure, create, and query a time series collection with MongoDB Atlas or a self-managed deployment.

Time required: 30 minutes

## Sample Data

The following example shows the `stocks` time series collection structure used in this quick start.

```javascript
{
   _id: ObjectId(...),
   ticker: <string>,
   date: ISODate(...),
   close: <double>,
   volume: <double>
}
```

## Learning Summary

Time series collections are optimized for time data, so performance depends heavily on how you configure them at creation. For more information, see `Time Series Collection Considerations <manual-timeseries-considerations>`.

## Next Steps

- To migrate existing data into a time series collection, see :ref:`Migrate
Data into a Time Series Collection <migrate-data-into-a-timeseries-collection>`.

- To shard a time series collection, see :ref:`Shard a Time Series Collection
<manual-timeseries-shard-collection>`.

- For aggregation and query behaviors specific to time series
collections, see `Aggregation and Operator Considerations <manual-timeseries-aggregations-operators>`.

## Learn More

- To learn how MongoDB stores time series data internally, see
`About Time Series Data <timeseries-bucketing>`.

- To learn about custom bucketing parameters in MongoDB 6.3 and later,
see `Using Custom Bucketing Parameters <flexible-bucketing>`.
