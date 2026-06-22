---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.reconfigForPSASet.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# rs.reconfigForPSASet() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`rs.reconfigForPSASet()` method has the following syntax:

```bash
rs.reconfigForPSASet(
  memberIndex: <num>,
  config: <configuration>,
  {
    "force" : <boolean>,
    "maxTimeMS" : <int>
  }
)
```

## Behavior

The :method:`rs.reconfigForPSASet()` method reconfigures your replica set in two steps:

1. The method reconfigures your replica set to add or modify a secondary
with  `{ votes: 1, priority: 0 }`.

2. Once the added or modified secondary has caught up with all committed
writes, the method reconfigures the secondary to have the :rsconf:`priority <members[n].priority>` specified in the :method:`rs.reconfigForPSASet()` command (`{ votes: 1, priority: <num> }`).

The two-step approach avoids the possibility of rolling back committed writes in the case of a failover to the new secondary before the new secondary has all committed writes from the previous configuration.

## Example

A replica set named `rs0` has the following configuration:

```javascript
{
   "_id" : "rs0",
   "version" : 1,
   "term": 1,
   "members" : [
      {
         "_id" : 0,
         "host" : "mongodb0.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {},
         "secondaryDelaySecs" : Long("0"),
         "votes" : 1
      },
      {
         "_id" : 2,
         "host" : "mongodb1.example.net:27017",
         "arbiterOnly" : true,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 0,
         "tags" : {},
         "secondaryDelaySecs" : Long("0"),
         "votes" : 1
      }
   ],
   "protocolVersion" : Long("1"),
   "writeConcernMajorityJournalDefault": true,
   "settings" : {
      "chainingAllowed" : true,
      "heartbeatIntervalMillis" : 2000,
      "heartbeatTimeoutSecs" : 10,
      "electionTimeoutMillis" : 10000,
      "catchUpTimeoutMillis" : 2000,
      "getLastErrorModes" : {},
      "getLastErrorDefaults" : {
         "w" : 1,
         "wtimeout" : 0
      },
      "replicaSetId" : ObjectId("60e6f83923193faa336889d2")
   }
}
```

The following sequence of operations add a new secondary to the replica set. The operations are issued in the :binary:`~bin.mongosh` shell while connected to the primary.

```javascript
cfg = rs.conf();
cfg["members"] = [
  {
     "_id" : 0,
     "host" : "mongodb0.example.net:27017",
     "arbiterOnly" : false,
     "buildIndexes" : true,
     "hidden" : false,
     "priority" : 1,
     "tags" : {},
     "secondaryDelaySecs" : Long("0"),
     "votes" : 1
  },
  {
     "_id" : 1,
     "host" : "mongodb1.example.net:27017",
     "arbiterOnly" : false,
     "buildIndexes" : true,
     "hidden" : false,
     "priority" : 2,
     "tags" : {},
     "secondaryDelaySecs" : Long("0"),
     "votes" : 1
  },
  {
     "_id" : 2,
     "host" : "mongodb2.example.net:27017",
     "arbiterOnly" : true,
     "buildIndexes" : true,
     "hidden" : false,
     "priority" : 0,
     "tags" : {},
     "secondaryDelaySecs" : Long("0"),
     "votes" : 1
  }
]
rs.reconfigForPSASet(1, cfg);
```

#. The first statement uses the :method:`rs.conf()` method to retrieve a document containing the current `configuration <replSetGetConfig-output>` for the replica set and stores the document in the local variable `cfg`.

#. The second statement adds the new secondary to the `members` array. In this configuration the new secondary is added at `memberIndex` `1`. The `memberIndex` is the same as the array index. For additional settings, see `replica set configuration settings <replSetGetConfig-output>`.

#. The last statement calls the :method:`rs.reconfigForPSASet()` method with the `memberIndex` `1` and the modified `cfg`. The `memberIndex` is the array position of the new member in the `members` array. Upon successful reconfiguration, the replica set configuration resembles the following:

```javascript
   {
      "_id" : "rs0",
      "version" : 1,
      "term": 1,
      "members" : [
         {
            "_id" : 0,
            "host" : "mongodb0.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {},
            "secondaryDelaySecs" : Long("0"),
            "votes" : 1
         },
         {
            "_id" : 1,
            "host" : "mongodb1.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 2,
            "tags" : {},
            "secondaryDelaySecs" : Long("0"),
            "votes" : 1
         },
         {
            "_id" : 2,
            "host" : "mongodb2.example.net:27017",
            "arbiterOnly" : true,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 0,
            "tags" : {},
            "secondaryDelaySecs" : Long("0"),
            "votes" : 1
         }
      ],
      "protocolVersion" : Long("1"),
      "writeConcernMajorityJournalDefault": true,
      "settings" : {
         "chainingAllowed" : true,
         "heartbeatIntervalMillis" : 2000,
         "heartbeatTimeoutSecs" : 10,
         "electionTimeoutMillis" : 10000,
         "catchUpTimeoutMillis" : 2000,
         "getLastErrorModes" : {},
         "getLastErrorDefaults" : {
            "w" : 1,
            "wtimeout" : 0
         },
         "replicaSetId" : ObjectId("60e6f83923193faa336889d2")
      }
   }
```

> **Seealso:** - :method:`rs.conf()`
- :method:`rs.reconfig()`
- `replSetGetConfig-output`
- `/administration/replica-set-member-configuration`
- `/administration/replica-set-maintenance`
