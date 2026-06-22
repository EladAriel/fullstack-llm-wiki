---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/merge-chunks-in-sharded-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# Merge Chunks in a Sharded Cluster

## Overview

The :dbcommand:`mergeChunks` command allows you to combine continuous chunks on the same shard into a single chunk. This tutorial explains how to merge neighboring chunks in a sharded cluster.

## Procedure

> **Note:** Examples in this procedure use a `members` `collection` in the
`test` `database`, using the `username` field as the
`shard key`.

### Identify Chunk Ranges

In :binary:`~bin.mongosh`, identify the `chunk` ranges with the following operation:

```javascript
sh.status()
```

In the output, the chunk ranges appear after the chunk counts for each sharded collection, as in the following example:

```none
--- Sharding Status ---
  sharding version: {
     "_id" : 1,
     "minCompatibleVersion" : 5,
     "currentVersion" : 6,
     "clusterId" : ObjectId("5ebf0bfd3eeb6037ec7cbba9")
  }
  shards:
        {  "_id" : "shardA",  "host" : "shardA/shardA-m1.example.net:27018,shardA-m2.example.net:27018,shardA-m3.example.net:27018",  "state" : 1 }
        {  "_id" : "shardB",  "host" : "shardB/shardB-m1.example.net:27018,shardB-m2.example.net:27018,shardB-m3.example.net:27018",  "state" : 1 }
  active mongoses:
        "4.4.0" : 1
  autosplit:
        Currently enabled: yes
  balancer:
        Currently enabled:  yes
        Currently running:  no
        Failed balancer rounds in last 5 attempts:  0
        Migration Results for the last 24 hours: 
                519 : Success
  databases:
        { "_id" : "config", "primary" : "config" }
                config.system.sessions
                        shard key: { "_id" : 1 }
                        unique: false
                        balancing: true
                        chunks:
                                shardA   512
                                shardB   512
                        too many chunks to print, use verbose if you want to force print
        { "_id" : "test", "primary" : "shardA", "version" : { "uuid" : UUID("22c042fc-7e3d-4c6d-992d-f3d714759781"), "lastMod" : 1 } }
                test.members
                        shard key: { "username" : 1 }
                        unique: false
                        balancing: true
                        chunks:
                                shardA   7
                                shardB   7
                        { "username" : { "$minKey" : 1 } } -->> { "username" : "user16643" } on : shardB Timestamp(13, 0)
                        { "username" : "user16643" } -->> { "username" : "user2329" } on : shardB Timestamp(16, 0)
                        { "username" : "user2329" } -->> { "username" : "user29937" } on : shardB Timestamp(17, 0)
                        { "username" : "user29937" } -->> { "username" : "user36583" } on : shardB Timestamp(18, 0)
                        { "username" : "user36583" } -->> { "username" : "user43229" } on : shardB Timestamp(19, 0)
                        { "username" : "user43229" } -->> { "username" : "user49877" } on : shardB Timestamp(20, 0)
                        { "username" : "user49877" } -->> { "username" : "user56522" } on : shardB Timestamp(21, 0)
                        { "username" : "user56522" } -->> { "username" : "user63169" } on : shardA Timestamp(21, 1)
                        { "username" : "user63169" } -->> { "username" : "user69816" } on : shardA Timestamp(10, 1)
                        { "username" : "user69816" } -->> { "username" : "user76462" } on : shardA Timestamp(11, 1)
                        { "username" : "user76462" } -->> { "username" : "user83108" } on : shardA Timestamp(12, 1)
                        { "username" : "user83108" } -->> { "username" : "user89756" } on : shardA Timestamp(14, 1)
                        { "username" : "user89756" } -->> { "username" : "user96401" } on : shardA Timestamp(15, 1)
                        { "username" : "user96401" } -->> { "username" : { "$maxKey" : 1 } } on : shardA Timestamp(15, 2)
```

The chunk ranges appear after the chunk counts for each sharded collection. For example, the following are the chunk ranges for the `test.members` collection:

```none
{ "username" : { "$minKey" : 1 } } -->> { "username" : "user16643" } on : shardB Timestamp(13, 0)
{ "username" : "user16643" } -->> { "username" : "user2329" } on : shardB Timestamp(16, 0)
{ "username" : "user2329" } -->> { "username" : "user29937" } on : shardB Timestamp(17, 0)
{ "username" : "user29937" } -->> { "username" : "user36583" } on : shardB Timestamp(18, 0)
{ "username" : "user36583" } -->> { "username" : "user43229" } on : shardB Timestamp(19, 0)
{ "username" : "user43229" } -->> { "username" : "user49877" } on : shardB Timestamp(20, 0)
{ "username" : "user49877" } -->> { "username" : "user56522" } on : shardB Timestamp(21, 0)
{ "username" : "user56522" } -->> { "username" : "user63169" } on : shardA Timestamp(21, 1)
{ "username" : "user63169" } -->> { "username" : "user69816" } on : shardA Timestamp(10, 1)
{ "username" : "user69816" } -->> { "username" : "user76462" } on : shardA Timestamp(11, 1)
{ "username" : "user76462" } -->> { "username" : "user83108" } on : shardA Timestamp(12, 1)
{ "username" : "user83108" } -->> { "username" : "user89756" } on : shardA Timestamp(14, 1)
{ "username" : "user89756" } -->> { "username" : "user96401" } on : shardA Timestamp(15, 1)
{ "username" : "user96401" } -->> { "username" : { "$maxKey" : 1 } } on : shardA Timestamp(15, 2)
```

### Merge Chunks

Merge contiguous `chunks <chunk>` on the same shard.

For example, consider the following chunk ranges on `shardA`:

> **Note:** The chunks to be merged are highlighted.

```javascript
{ "username" : "user56522" } -->> { "username" : "user63169" } on : shardA Timestamp(21, 1)
{ "username" : "user63169" } -->> { "username" : "user69816" } on : shardA Timestamp(10, 1)
{ "username" : "user69816" } -->> { "username" : "user76462" } on : shardA Timestamp(11, 1)
{ "username" : "user76462" } -->> { "username" : "user83108" } on : shardA Timestamp(12, 1)
{ "username" : "user83108" } -->> { "username" : "user89756" } on : shardA Timestamp(14, 1)
{ "username" : "user89756" } -->> { "username" : "user96401" } on : shardA Timestamp(15, 1)
{ "username" : "user96401" } -->> { "username" : { "$maxKey" : 1 } } on : shardA Timestamp(15, 2)
```

To merge the highlighted contiguous chunks, issue the :dbcommand:`mergeChunks` command against the `admin` database:

```javascript
db.adminCommand( {
   mergeChunks: "test.members",
   bounds: [ { "username" : "user69816" },
             { "username" : "user96401" } ]
} )
```

On success, :dbcommand:`mergeChunks` produces the following output:

```javascript
{
   "ok" : 1,
   "operationTime" : Timestamp(1589580356, 14),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1589580356, 14),
      "signature" : {
         "hash" : BinData(0,"up5VKd49G/uPCq1iger2nOtfIHw="),
         "keyId" : Long("6827188741371592725")
      }
   }
}
```

On any failure condition, :dbcommand:`mergeChunks` returns a document where the value of the `ok` field is `0`.

### View Merged Chunks Ranges

After merging the identified chunks, confirm the new chunk, as follows:

```javascript
sh.status()
```

The output of :method:`sh.status()` should resemble:

```none
--- Sharding Status ---
  sharding version: {
     "_id" : 1,
     "minCompatibleVersion" : 5,
     "currentVersion" : 6,
     "clusterId" : ObjectId("5ebef5447fa151d4bd79dd72")
  }
  shards:
        { "_id" : "shardA", "host" : "shardA/shardA-m1.example.net:27018,shardA-m2.example.net:27018,shardA-m3.example.net:27018", "state" : 1 }
        { "_id" : "shardB", "host" : "shardB/shardB-m1.example.net:27018,shardB-m2.example.net:27018,shardB-m3.example.net:27018", "state" : 1 }
  active mongoses:
        "4.4.0" : 1
  autosplit:
        Currently enabled: yes
  balancer:
        Currently enabled:  yes
        Currently running:  no
        Failed balancer rounds in last 5 attempts:  0
        Migration Results for the last 24 hours: 
                519 : Success
  databases:
        { "_id" : "config", "primary" : "config" }
                config.system.sessions
                        shard key: { "_id" : 1 }
                        unique: false
                        balancing: true
                        chunks:
                                shardA   512
                                shardB   512
                       too many chunks to print, use verbose if you want to force print
        { "_id" : "test", "primary" : "shardA", "version" : { "uuid" : UUID("22c042fc-7e3d-4c6d-992d-f3d714759781"), "lastMod" : 1 } }
                test.members
                        shard key: { "username" : 1 }
                        unique: false
                        balancing: true
                        chunks:
                                shardA	5
                                shardB	6
                        { "username" : { "$minKey" : 1 } } -->> { "username" : "user16643" } on : shardA Timestamp(22, 0) 
                        { "username" : "user16643" } -->> { "username" : "user2329" } on : shardB Timestamp(22, 1) 
                        { "username" : "user2329" } -->> { "username" : "user29937" } on : shardB Timestamp(17, 0) 
                        { "username" : "user29937" } -->> { "username" : "user36583" } on : shardB Timestamp(18, 0) 
                        { "username" : "user36583" } -->> { "username" : "user43229" } on : shardB Timestamp(19, 0) 
                        { "username" : "user43229" } -->> { "username" : "user49877" } on : shardB Timestamp(20, 0) 
                        { "username" : "user49877" } -->> { "username" : "user56522" } on : shardB Timestamp(21, 0) 
                        { "username" : "user56522" } -->> { "username" : "user63169" } on : shardA Timestamp(21, 1) 
                        { "username" : "user63169" } -->> { "username" : "user69816" } on : shardA Timestamp(10, 1) 
                        { "username" : "user69816" } -->> { "username" : "user96401" } on : shardA Timestamp(21, 2) 
                        { "username" : "user96401" } -->> { "username" : { "$maxKey" : 1 } } on : shardA Timestamp(15, 2)
```

After the merge, the `balancer <sharding-balancing>` may migrate chunks across shards to ensure a more even distribution of chunks.
