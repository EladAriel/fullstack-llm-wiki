---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dbHash.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# dbHash (database command)

## Definition

> **Warning:** The :dbcommand:`dbHash` command obtains a shared (S) lock on the
database, which prevents writes until the command completes.

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     dbHash: 1, 
     collections: [ <collection1>, ... ] 
   } 
)
```

## Command Fields

The command takes the following fields:

## Behavior

### Non-Existent Collection

If a collection in the `collections` array is non-existent, :dbcommand:`dbHash` does not return a hash value for that collection.

### Restrictions

The :dbcommand:`dbHash` command no longer support `afterClusterTime <afterClusterTime>`. As such, :dbcommand:`dbHash` cannot be associated with `causally consistent sessions <causal-consistency>`.

## Return Document

The command returns a document with the following fields:

## Examples

### Return Hash Values for All Collections in a Database

The following example returns the hash value for all collections in the database `test`:

```javascript
use test
db.runCommand( { dbHash: 1 } )
```

The operation returns the following document:

```json
{
   "host" : "myHostName.local:27017",
   "collections" : {
      "foo" : "d27b769230edc551d869060ec3fb68bd",
      "inventory" : "ec3d821581ea1bd3aa8196c94b946874",
      "log" : "d41d8cd98f00b204e9800998ecf8427e",
      "orders" : "0242c0a128c284ea9576a34db2306c12",
      "restaurants" : "5dc9b88091c36f0d529567b5b6e3fc92",
      "zipcodes" : "31ede812bf397509a87359c65bf2a08c"
   },
   "capped" : [
      "log"
   ],
   "uuids" : {
      "foo" : UUID("469592fe-3bfe-425e-975f-cedbe0c4741d"),
      "inventory" : UUID("0830e0ad-cc24-4fc7-80d0-8e22fe45e382"),
      "log" : UUID("4be024ff-711b-4ab8-836b-dee662e090f1"),
      "orders" : UUID("755be489-745f-400c-ac3b-f27525ad0108"),
      "restaurants" : UUID("520b56ec-3276-4904-b6e5-286bc9bfa648"),
      "zipcodes" : UUID("12e97b70-c174-40af-a178-5d83a241fe20")
   },
   "md5" : "0cb7417ae9d9eb865000b4debdc671da",
   "timeMillis" : 53,
   "ok" : 1,
   "operationTime" : Timestamp(1529208582, 4),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1529208582, 4),
      "signature" : {
         "hash" : BinData(0,"X3MmevDqUgCVvN1AhnT+fiOL/Lc="),
         "keyId" : Long("6567898567824900097")
      }
   }
}
```

### Return Hash Values for Specified Collections in a Database

The following example returns the hash value for the collections `inventory` and `orders` in the database `test`:

```javascript
use test
db.runCommand( { dbHash: 1, collections: [ "inventory", "orders" ] } )
```

The operation returns the following document:

```json
{
   "host" : "myHostName.local:27017",
   "collections" : {
      "inventory" : "ec3d821581ea1bd3aa8196c94b946874",
      "orders" : "0242c0a128c284ea9576a34db2306c12"
   },
   "capped" : [ ],
   "uuids" : {
      "inventory" : UUID("0830e0ad-cc24-4fc7-80d0-8e22fe45e382"),
      "orders" : UUID("755be489-745f-400c-ac3b-f27525ad0108")
   },
   "md5" : "cb4676f316ff2ff29c701a5edd18afe3",
   "timeMillis" : 0,
   "ok" : 1,
   "operationTime" : Timestamp(1529208801, 1),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1529208801, 1),
      "signature" : {
         "hash" : BinData(0,"I4z4a4Mgs+tcx0MP5xIU8DYAMB0="),
         "keyId" : Long("6567898567824900097")
      }
   }
}
```
