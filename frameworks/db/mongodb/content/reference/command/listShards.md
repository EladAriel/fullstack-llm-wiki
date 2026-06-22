---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/listShards.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# listShards (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
  { 
    listShards: 1 
  }
)
```

## Command Fields

The command takes the following fields:

## Output Fields

:dbcommand:`listShards` returns a document that includes:

- A `shards` field which contains an array of documents, each
describing one shard. Each document may contain the following fields:

.. include:: /includes/list-shards-output.rst

- The `ok` status field, the `operationTime` field, and the
`$clusterTime` field for the operation. For details on these fields, see `command-response`.

## Example

The following operation runs :dbcommand:`listShards` against the :binary:`~bin.mongos` `admin` database:

```javascript
db.adminCommand({ listShards: 1 })
```

The following document is an example of the output from a :dbcommand:`listShards` command:

```javascript
{
 "shards": [
   {
     "_id": "shard01",
     "host": "shard01/host1:27018,host2:27018,host3:27018",
     "state": 1
   },
   {
     "_id": "shard02",
     "host": "shard02/host4:27018,host5:27018,host6:27018",
     "tags": [ "NYC" ],
     "state": 1
   },
   {
     "_id": "shard03",
     "host": "shard03/host7:27018,host8:27018,host9:27018",
     "state": 1
   }
 ],
 "ok": 1,
 "$clusterTime" : {
    "clusterTime" : Timestamp(1510716515, 1),
    "signature" : {
       "hash" : BinData(0,"B2ViX7XLzFLS5Fl9XEuFXbwKIM4="),
       "keyId" : Long("6488045157173166092")
    }
 },
 "operationTime" : Timestamp(1510716515, 1)
}
```
