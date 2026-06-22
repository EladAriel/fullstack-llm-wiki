---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/clearJumboFlag.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# clearJumboFlag (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

Th command has the following syntax:

```javascript
db.adminCommand( 
   {
     clearJumboFlag: "<database>.<collection>",
     bounds: <array>
   } 
)
```

**-OR-**

```javascript
// Cannot use for collections with hashed shard keys

db.adminCommand( 
   {
     clearJumboFlag: "<database>.<collection>",
     find: <query>
   } 
)
```

### Command Fields

The :dbcommand:`clearJumboFlag` command takes the following fields as arguments:

## Access Control

On systems running with :setting:`~security.authorization`, the user must have the :authaction:`clearJumboFlag` privilege actions on the `{ db: "", collection: "" }` `resource <resource-all-but-system-collections>`.

The built-in role :authrole:`clusterManager` provides the appropriate privileges.

## Example

### Clear Jumbo Flag for a Chunk (Range-Based Shard Key)

The :method:`sh.status()` includes the following `sh.status.databases.<collection>.chunk-details` for the `test.jumbo` collection.

```javascript
... // Content omitted for brevity

test.jumbo
         shard key: { "x" : 1 }
         unique: false
         balancing: true
         chunks:
                  shardA   2
                  shardB   2
         { "x" : { "$minKey" : 1 } } -->> { "x" : 1 } on : shardB Timestamp(3, 0) 
         { "x" : 1 } -->> { "x" : 2 } on : shardA Timestamp(6, 1) jumbo 
         { "x" : 2 } -->> { "x" : 3 } on : shardA Timestamp(5, 1) jumbo 
         { "x" : 3 } -->> { "x" : { "$maxKey" : 1 } } on : shardB Timestamp(6, 0) 
```

The following :dbcommand:`clearJumboFlag` command specifies the `bounds <clearJumboFlag-bounds>` of the `{ "x" : 1 } -->> { "x" : 2 }` chunk:

```javascript
db.adminCommand( {
   clearJumboFlag: "test.jumbo",
   bounds: [{ "x" : 1 }, { "x" : 2 }]
} )
```

Upon success, the command returns `"ok": 1` in its output:

```javascript
{
   "ok" : 1,
   "operationTime" : Timestamp(1580190080, 5),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1580190080, 5),
      "signature" : {
         "hash" : BinData(0,"0cYT49s72MHUYV1F2WpoEwlyeVs="),
         "keyId" : Long("6786859092951433239")
      }
   }
}
```

The following :dbcommand:`clearJumboFlag` command specifies the `find <clearJumboFlag-bounds>` field to find the chunk that contains the shard key `{ "x" : 2 }` :

```javascript
db.adminCommand( {
   clearJumboFlag: "test.jumbo",
   find: { "x" : 2 }
} )
```

Upon success, the command returns `"ok": 1` in its output:

```javascript
{
   "ok" : 1,
   "operationTime" : Timestamp(1580191819, 5),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1580191819, 5),
      "signature" : {
         "hash" : BinData(0,"N6x6drN7HUq5MR5ezUJns1rfeqY="),
         "keyId" : Long("6786859092951433239")
      }
   }
}
```

To verify the operation, run :method:`sh.status()` again. The `jumbo` flag should no longer appear in its output.

```javascript
... // Content omitted for brevity

test.jumbo
         shard key: { "x" : 1 }
         unique: false
         balancing: true
         chunks:
                  shardA   2
                  shardB   2
         { "x" : { "$minKey" : 1 } } -->> { "x" : 1 } on : shardB Timestamp(3, 0) 
         { "x" : 1 } -->> { "x" : 2 } on : shardA Timestamp(7, 0) 
         { "x" : 2 } -->> { "x" : 3 } on : shardA Timestamp(8, 0) 
         { "x" : 3 } -->> { "x" : { "$maxKey" : 1 } } on : shardB Timestamp(6, 0) 
```

### Clear Jumbo Flag for a Chunk (Hashed Shard Key)

The :method:`sh.status()` includes the following `sh.status.databases.<collection>.chunk-details` for the `test.jumboHashed` collection. The collection uses a hashed shard key.

```javascript
... // Content omitted for brevity

test.jumboHashed
         shard key: { "x" : "hashed" }
         unique: false
         balancing: true
         chunks:
                  shardA   2
                  shardB   2
         { "x" : { "$minKey" : 1 } } -->> { "x" : Long(0) } on : shardA Timestamp(1, 0) 
         { "x" : Long(0) } -->> { "x" : Long("848411777775835583") } on : shardA Timestamp(4, 0) 
         { "x" : Long("848411777775835583") } -->> { "x" : Long("5902408780260971510") } on : shardB Timestamp(4, 1) jumbo 
         { "x" : Long("5902408780260971510") } -->> { "x" : { "$maxKey" : 1 } } on : shardB Timestamp(2, 2) 
```

To clear the `jumbo` flag for a chunk if the collection uses a `hashed shard key`, use :dbcommand:`clearJumboFlag` with the `bounds <clearJumboFlag-bounds>` field:

```javascript
db.adminCommand( {
   clearJumboFlag: "test.jumboHashed",
   bounds: [{ "x" : Long("848411777775835583") }, { "x" : Long("5902408780260971510") }]
} )
```

Upon success, the command returns `"ok": 1` in its output:

```javascript
{
   "ok" : 1,
   "operationTime" : Timestamp(1580194290, 5),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1580194290, 5),
      "signature" : {
         "hash" : BinData(0,"nWCqOYVrab7NEGHWoo2NYENqHR4="),
         "keyId" : Long("6786875525496307742")
      }
   }
}
```

To verify the operation, run :method:`sh.status()` again. The `jumbo` flag should no longer appear in its output.

```javascript
... // Content omitted for brevity

test.jumboHashed
         shard key: { "x" : "hashed" }
         unique: false
         balancing: true
         chunks:
                  shardA	2
                  shardB	2
         { "x" : { "$minKey" : 1 } } -->> { "x" : Long(0) } on : shardA Timestamp(1, 0) 
         { "x" : Long(0) } -->> { "x" : Long("848411777775835583") } on : shardA Timestamp(4, 0) 
         { "x" : Long("848411777775835583") } -->> { "x" : Long("5902408780260971510") } on : shardB Timestamp(5, 0) 
         { "x" : Long("5902408780260971510") } -->> { "x" : { "$maxKey" : 1 } } on : shardB Timestamp(2, 2)
```

> **Seealso:** `/tutorial/clear-jumbo-flag`
