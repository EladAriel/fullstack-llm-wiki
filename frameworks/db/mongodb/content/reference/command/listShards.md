---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/listShards.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
