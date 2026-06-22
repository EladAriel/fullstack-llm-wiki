---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.getDBs.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# Mongo.getDBs() (mongosh method)

## Description

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Example

To list the available databases and metadata for the local MongoDB instance:

```javascript
db.getMongo().getDBs()
```

The :method:`db.getMongo()` method returns the connection to the current MongoDB instance. The :method:`Mongo.getDBs()` output resembles:

```javascript
{
 databases: [
   { name: 'admin', sizeOnDisk: Long("225280"), empty: false },
   { name: 'config', sizeOnDisk: Long("212992"), empty: false },
   { name: 'local', sizeOnDisk: Long("2400256"), empty: false },
   { name: 'test', sizeOnDisk: Long("303104"), empty: false }
 ],
 totalSize: Long("3141632"),
 totalSizeMb: Long("2"),
 ok: 1,
 '$clusterTime': {
   clusterTime: Timestamp({ t: 1640186473, i: 1 }),
   signature: {
     hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
     keyId: Long("0")
   }
 },
 operationTime: Timestamp({ t: 1640186473, i: 1 })
 } 
```

The databases are listed in the highlighted lines.
