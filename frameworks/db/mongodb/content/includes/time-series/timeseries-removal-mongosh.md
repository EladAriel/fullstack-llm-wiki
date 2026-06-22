---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/timeseries-removal-mongosh.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you create a `time series collection <manual-timeseries-collection>`, you can set up automatic removal of documents older than a specified number of seconds by using the `expireAfterSeconds` parameter:

```javascript
db.createCollection(
    "weather24h",
    {
       timeseries: {
          timeField: "timestamp",
          metaField: "metadata",
          granularity: "hours"
       },
       expireAfterSeconds: 86400
    }
)
```

The expiration threshold is the `timeField` field value plus the specified number of seconds. Consider the following document in the `weather24h` collection:

```
{
   "metadata": {"sensorId": 5578, "type": "temperature"},
   "timestamp": ISODate("2021-05-18T10:00:00.000Z"),
   "temp": 12
}
```

The document would expire from the database at `"2021-05-19T10:00:00.000Z"`. Once all documents in a bucket are expired, the background task that removes expired buckets removes the bucket during the next run. See `timeseries-collection-delete-operations-timing` for more information.

## Enable Automatic Removal on a Collection

To enable automatic removal of documents for an existing `time series collection <manual-timeseries-collection>`, issue the following :dbcommand:`collMod` command:

```javascript
db.runCommand({
   collMod: "weather24h",
   expireAfterSeconds: 604801
})
```

## Change the `expireAfterSeconds` Parameter

To change the `expireAfterSeconds` parameter value, issue the following :dbcommand:`collMod` command:

```javascript
db.runCommand({
   collMod: "weather24h",
   expireAfterSeconds: 604801
})
```

## Retrieve the Current Value of `expireAfterSeconds`

To retrieve the current value of `expireAfterSeconds`, use the :dbcommand:`listCollections` command:

```javascript
db.runCommand( { listCollections: 1 } )
```

The result document contains a document for the time series collection which contains the `options.expireAfterSeconds` field.

```javascript
{
   cursor: {
      id: <number>,
      ns: 'test.$cmd.listCollections',
      firstBatch: [
        {
           name: <string>,
           type: 'timeseries',
           options: {
              expireAfterSeconds: <number>,
              timeseries: { ... }
           },
           ...
        },
        ...
      ]
   }
}
```

## Disable Automatic Removal

To disable automatic removal, use the :dbcommand:`collMod` command to set `expireAfterSeconds` to `off`:

```javascript
db.runCommand({
    collMod: "weather24h",
    expireAfterSeconds: "off"
})
```
