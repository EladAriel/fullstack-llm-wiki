---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetGetConfig.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# replSetGetConfig (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

To run, :dbcommand:`replSetGetConfig` must be issued against the `admin` database. The command has the following syntax:

```javascript
db.adminCommand( 
   {
     replSetGetConfig: 1,
     commitmentStatus: <boolean>,
     comment: <any>
   } 
)
```

## Command Fields

:binary:`~bin.mongosh` provides the :method:`rs.conf()` method that wraps the :dbcommand:`replSetGetConfig` command:

```javascript
rs.conf();
```

## Output Example

The following is an example output of the :dbcommand:`replSetGetConfig` command run with `commitmentStatus: true <replSetGetConfig-commitmentStatus>` on the primary:

```javascript
{
   "config" : {
      "_id" : "myRepl",
      "version" : 180294,
      "term" : 1,
      "protocolVersion" : Long(1),
      "writeConcernMajorityJournalDefault" : true,
      "members" : [
         {
            "_id" : 0,
            "host" : "m1.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : Long(0),
            "votes" : 1
         },
         {
            "_id" : 1,
            "host" : "m2.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : Long(0),
            "votes" : 1
         },
         {
            "_id" : 2,
            "host" : "m3.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : Long(0),
            "votes" : 1
         }
      ],
      "settings" : {
         "chainingAllowed" : true,
         "heartbeatIntervalMillis" : 2000,
         "heartbeatTimeoutSecs" : 10,
         "electionTimeoutMillis" : 10000,
         "catchUpTimeoutMillis" : -1,
         "catchUpTakeoverDelayMillis" : 30000,
         "getLastErrorModes" : {

         },
         "getLastErrorDefaults" : {
            "w" : 1,
            "wtimeout" : 0
         },
         "replicaSetId" : ObjectId("5eaa1e9ac4d650aa7817623d")
      }
   },
   "commitmentStatus" : true, 
   "ok" : 1,
   "$clusterTime" : {
      "clusterTime" : Timestamp(1588212091, 1),
      "signature" : {
         "hash" : BinData(0,"veOHa2mOeRTzuR0LKqnzGxWV77k="),
         "keyId" : Long("6821298283919441923")
      }
   },
   "operationTime" : Timestamp(1588212091, 1)
}
```

> **Seealso:** - :method:`rs.conf()`
- :method:`rs.reconfig()`
