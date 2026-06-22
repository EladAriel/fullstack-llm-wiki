---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.createStreamProcessor.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# sp.createStreamProcessor() (mongosh method)

## Definition

.. versionadded:: 7.0

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.createStreamProcessor()` method has the following syntax:

```json
sp.createStreamProcessor(
  <name>,
  [
    <pipeline>
  ],
  {
    <options>
  }
)
```

## Command Fields

`sp.createStreamProcessor()` takes these fields:

## Behavior

`sp.createStreamProcessor()` creates a persistent, named stream processor on the current stream processing workspace. You can initialize this stream processor with :method:`sp.processor.start()`. If you try to create a stream processor with the same name as an existing stream processor, `mongosh` will return an error.

## Access Control

The user running `sp.createStreamProcessor()` must have the :atlasrole:`atlasAdmin` role.

## Example

The following example creates a stream processor named `solarDemo` which ingests data from the `sample_stream_solar` connection. The processor excludes all documents where the value of the `device_id` field is `device_8`, passing the rest to a :atlas:`tumbling window </atlas-sp/overview/#tumbling-windows>` with a 10-second duration. Each window groups the documents it receives, then returns various useful statistics of each group. The stream processor then merges these records to `solar_db.solar_coll` over the `mongodb1` connection.

```json
sp.createStreamProcessor(
  'solarDemo',
  [
    {
      $source: {
connectionName: 'sample_stream_solar',
timeField: {
$dateFromString: {
dateString: '$timestamp'
}
}
}
    },
    {
      $match: {
$expr: {
$ne: [
"$device_id",
"device_8"
]
}
}
    },
    {
      $tumblingWindow: {
interval: {
size: Int32(10),
unit: "second"
},
"pipeline": [
{
$group: {
"_id": {  "device_id": "$device_id" },
"max_temp": { $max: "$obs.temp" },
"max_watts": { $max: "$obs.watts" },
"min_watts": { $min: "$obs.watts" },
"avg_watts": { $avg: "$obs.watts" },
"median_watts": {
$median: {
input: "$obs.watts",
method: "approximate"
}
}
}
}
]
}
    },
    {
      $merge: {
into: {
connectionName: "mongodb1",
db: "solar_db",
coll: "solar_coll"
},
on: ["_id"]
}
    }
  ]
)
```

## Learn More

- :atlas:`Stream Aggregation </atlas-sp/stream-aggregation>`
- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
