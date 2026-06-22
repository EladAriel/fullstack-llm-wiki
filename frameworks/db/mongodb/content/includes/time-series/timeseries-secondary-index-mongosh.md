---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/timeseries-secondary-index-mongosh.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You may wish to create additional secondary indexes. Consider a weather data collection with the configuration:

```javascript
   db.createCollection(
   "weather",
   { 
      timeseries: {
         timeField: "timestamp",
         metaField: "metadata"
   }})
```

In each weather data document, the `metadata` field value is a subdocument with fields for the weather sensor ID and type:

```javascript
 {
     "timestamp": ISODate("2021-05-18T00:00:00.000Z"),
     "metadata": { 
     "sensorId": 5578, 
     "type": "temperature" 
     },
     "temp": 12
 }
```

The default compound index for the collection indexes the entire `metadata` subdocument, so the index is only used with :expression:`$eq` queries. By indexing specific `metadata` fields, you improve query performance for other query types.

For example, this :expression:`$in` query benefits from a secondary index on `metadata.type`:

```javascript
 { metadata.type:{ $in: ["temperature", "pressure"] }}
```

## Use Secondary Indexes to Improve Sort Performance

Sort operations on time series collections can use secondary indexes on the `timeField` field. Under certain conditions, sort operations can also use compound secondary indexes on the `metaField` and `timeField` fields.

The aggregation pipeline stages :pipeline:`$match` and :pipeline:`$sort` determine which indexes a time series collection can use. An index can be used in the following scenarios:

- Sort on `{ <timeField>: ±1 }` uses a secondary index on
`<timeField>`

- Sort on `{ <metaField>: ±1, timeField: ±1 }` uses the default
compound index on `{ <metaField>: ±1, timeField: ±1 }`

- Sort on `{ <timeField>: ±1 }` uses a secondary index on
`{ metaField: ±1, timeField: ±1 }` when there is a point predicate on `<metaField>`

For example, the following `sensorData` collection contains measurements from weather sensors:

```javascript
 db.sensorData.insertMany( [ {
     "metadata": {
         "sensorId": 5578,
         "type": "omni",
         "location": {
             type: "Point",
             coordinates: [-77.40711, 39.03335]
         }
     },
     "timestamp": ISODate("2022-01-15T00:00:00.000Z"),
     "currentConditions": {
         "windDirection": 127.0,
         "tempF": 71.0,
         "windSpeed": 2.0,
         "cloudCover": null,
         "precip": 0.1,
         "humidity": 94.0,
     }
     },
     {
     "metadata": {
         "sensorId": 5578,
         "type": "omni",
         "location": {
             type: "Point",
             coordinates: [-77.40711, 39.03335]
         }
     },
     "timestamp": ISODate("2022-01-15T00:01:00.000Z"),
     "currentConditions": {
         "windDirection": 128.0,
         "tempF": 69.8,
         "windSpeed": 2.2,
         "cloudCover": null,
         "precip": 0.1,
         "humidity": 94.3,
     }
     },
     {
     "metadata": {
         "sensorId": 5579,
         "type": "omni",
         "location": {
             type: "Point",
             coordinates: [-80.19773, 25.77481]
         }
     },
     "timestamp": ISODate("2022-01-15T00:01:00.000Z"),
     "currentConditions": {
         "windDirection": 115.0,
         "tempF": 88.0,
         "windSpeed": 1.0,
         "cloudCover": null,
         "precip": 0.0,
         "humidity": 99.0,
     }
     } 
 ] 
 )
```

Create a secondary single-field index on the `timestamp` field:

```javascript
 db.sensorData.createIndex( { "timestamp": 1 } ) 
```

The following sort operation on the `timestamp` field uses the Secondary Index to improve performance:

```javascript
 db.sensorData.aggregate( [
     { $match: { "timestamp" : { $gte: ISODate("2022-01-15T00:00:00.000Z") } } },
     { $sort: { "timestamp": 1 } } 
 ] )
```

To confirm that the sort operation used the Secondary Index, run the operation again with the `.explain( "executionStats" )` option:

```javascript
 db.sensorData.explain( "executionStats" ).aggregate( [
     { $match: { "timestamp": { $gte: ISODate("2022-01-15T00:00:00.000Z") } } },
     { $sort: { "timestamp": 1 } } 
 ] )
```

### Last Point Queries on Time Series Collections

In time series data, a last point query returns the data point with the latest timestamp for a given field. For time series collections, a last point query fetches the latest measurement for each unique metadata value. For example, you may want to get the latest temperature reading from all sensors. Improve performance on last point queries by creating any of the following indexes:

```javascript
 { "metadata.sensorId": 1,  "timestamp": 1 }
 { "metadata.sensorId": 1,  "timestamp": -1 }
 { "metadata.sensorId": -1, "timestamp": 1 }
 { "metadata.sensorId": -1, "timestamp": -1 }  
```

> **Note:**  Last point queries are most performant when they use the :ref:`DISTINCT_SCAN
 optimization <explain-results>`. This optimization is only available when an
 index on `timeField` is descending.

The following command creates a compound secondary index on `metaField` (ascending) and `timeField` (descending):

```javascript
 db.sensorData.createIndex( { "metadata.sensorId": 1,  "timestamp": -1 } ) 
```

The following last point query example uses the descending `timeField` compound secondary index created above:

```javascript
 db.sensorData.aggregate( [
     { 
         $sort: { "metadata.sensorId": 1, "timestamp": -1 } 
     },
     { 
         $group: {
             _id: "$metadata.sensorId",
             ts: { $first: "$timestamp" },
             temperatureF: { $first: "$currentConditions.tempF" }
         }  
     }
 ] )
```

To confirm that the last point query used the secondary index, run the operation again using `.explain( "executionStats" )`:

```javascript
 db.getCollection( 'sensorData' ).explain( "executionStats" ).aggregate( [
     {
         $sort: { "metadata.sensorId": 1, "timestamp": -1 }
     },
     {
         $group: {
             _id: "$metadata.sensorId",
             ts: { $first: "$timestamp" },
             temperatureF: { $first: "$currentConditions.tempF" }
         }
     }
 ] )
```

The `winningPlan.queryPlan.inputStage.stage` is `DISTINCT_SCAN`, which indicates that the index was used. For more information on the explain plan output, see `explain-results`.

### Specify Index Hints for Time Series Collections

Index hints cause MongoDB to use a specific index for a query. Some operations on time series collections can only take advantage of an index if that index is specified in a hint.

For example, the following query causes MongoDB to use the `timestamp_1_metadata.sensorId_1` index:

```javascript
 db.sensorData.find( { "metadata.sensorId": 5578 } ).hint( "timestamp_1_metadata.sensorId_1" )
```

On a time series collection, you can specify hints using either the index name or the index key pattern. To get the names of the indexes on a collection, use `GetIndexes()`.

### Create 2dsphere Indexes

Starting in version 6.0 you can create `2dsphere` indexes. For example, the following operation creates a 2dsphere index on the `location` field:

> **Note:**  .. include:: /includes/time-series-secondary-indexes-downgrade-FCV.rst
