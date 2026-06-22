---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========

# Time Series

Time series data is a sequence of data points in which insights are gained by analyzing changes over time.

Time series data is generally composed of these components:

- **Time**: Indicates when the data point was recorded.
- **Metadata**: A label or tag that identifies a data series and rarely changes.
Metadata is stored in a `metaField`. You cannot add a `metaField` field to a time series document after you create it. Metadata is also known as `source`. For more information, see `timeseries-collections-metafield`.

- **Metrics**: Individual data points tracked at increments in time, often displayed
as key-value pairs that change over time. Metrics are also known as values.

- **Measurements**: Documents that contain data for all metrics at a
specific point in time. A measurement includes the time, metadata, and all metrics recorded at that moment.

This table shows examples of time series data:

For efficient time series data storage, MongoDB provides time series collections.

The following example shows a measurement document for weather data:

```javascript
{
  "timestamp": ISODate("2025-08-19T12:00:00Z"),
  "metaField": {
    "sensorId": "A1234",
    "location": {
      "city": "New York",
      "state": "NY"
    }
  },
  "temperature": 25.4,
  "humidity": 48.2,
  "pressure": 1012.5,
  "windSpeed": 5.2,
  "windDirection": "NW"
}
```

## Time Series Collections

.. versionadded:: 5.0

Time series collections efficiently store time series data. Writes are organized so that data from the same source is stored alongside other data points from a similar point in time.

> **Important:** .. include:: /includes/downgrade-for-timeseries-collections.rst

### Benefits

Compared to normal collections, storing time series data in time series collections improves query efficiency and reduces the disk usage for time series data and `secondary indexes <secondary index>`. MongoDB 6.3 and later automatically creates a `compound index <index-type-compound>` on the time and metadata fields for new time series collections.

Time series collections use an underlying columnar storage format and store data in time-order. This format provides the following benefits:

- Reduced complexity for working with time series data
- Improved query efficiency
- Reduced disk usage
- Reduced I/O for read operations
- Increased WiredTiger cache usage
### Example Use Cases

Time series collections are optimal for analyzing data over time. The following table illustrates use cases for time series data:

Time series collections are not intended for the following types of data:

- Unordered data
- Data that is not time-dependent
### Behavior

Time series collections generally behave like other MongoDB collections.

> **Warning:** Match expressions in update commands can only specify the
metaField. You can't update other fields in a time series document.
For more details, see :ref:`Time Series Update Limitations
<timeseries-limitations-updates>`.

MongoDB treats time series collections as writable non-materialized `views <views-landing-page>` backed by an internal collection. When you insert data, the internal collection automatically organizes time series data into an optimized storage format.

Starting in MongoDB 6.3: if you create a new time series collection, MongoDB also generates a `compound index <index-create-compound>` on the `metaField and timeField <time-series-fields>` fields. To improve query performance, queries on time series collections use the new compound index. The compound index also uses the optimized storage format.

.. include:: /includes/time-series/timeseries-timeField-deprecated.rst

Also, starting in MongoDB 8.0, if you create a time series collection with a shard key containing the `timeField`, a `log message <log-messages-ref>` is added to the `log file <log-message-destinations>` on the `primary shard <primary-shard>`. In addition, a log message is added every 12 hours on the primary node of the `config server replica set <csrs>`. The log messages state that using the `timeField` as a shard key in a time series collection is deprecated and you must reshard your collection using the `metaField`.

### metaFields

Time series documents can contain a `metaField`. MongoDB uses the `metaField` to group documents for storage optimization and query efficiency. For more information about the `metaField`, see `metaField Considerations <timeseries-metafield-considerations>`.

### Indexes

MongoDB automatically creates a `compound index <index-type-compound>` on both the metaField and timeField of a time series collection.

### Zone Sharding

.. include:: /includes/fact-zone-timeseries-support.rst

## Next Steps

To get started with time series collections, see the tutorials on the following pages:

- `timeseries-quick-start`
- `timeseries-create-query-procedures`
## Contents

- Quick Start <core/timeseries/timeseries-quick-start>
- Time Series Data </core/timeseries/timeseries-bucketing>
- Considerations <core/timeseries/timeseries-considerations>
- Create & Configure </core/timeseries/timeseries-create-configure>
- Query </core/timeseries/timeseries-querying>
- Indexes </core/timeseries/timeseries-index>
- Best Practices </core/timeseries/timeseries-best-practices>
- Limitations </core/timeseries/timeseries-limitations>
