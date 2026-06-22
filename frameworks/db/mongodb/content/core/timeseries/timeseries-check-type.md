---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-check-type.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# List Time Series Collections in a Database

You can output a list of collections in a database and filter the results by a variety of properties, including collection type. You can use this functionality to list all time series collections in a database.

## Procedure

To list all time series collections in a database, use the :dbcommand:`listCollections` command with a filter for `{ type: "timeseries" }`:

```javascript
db.runCommand( {
   listCollections: 1,
   filter: { type: "timeseries" } 
} )
```

## Output

For time series collections, the output includes:

- `type: 'timeseries'`
- `options: { timeseries: { ... } }`
For example:

```javascript
{
  cursor: {
    id: Long("0"),
    ns: 'test.$cmd.listCollections',
    firstBatch: [
      {
        name: 'weather',
        type: 'timeseries',
        options: {
          timeseries: {
            timeField: 'timestamp',
            metaField: 'metadata',
            granularity: 'hours',
            bucketMaxSpanSeconds: 2592000
          }
        },
        info: { readOnly: false }
      }
    ]
  },
  ok: 1
}
```
