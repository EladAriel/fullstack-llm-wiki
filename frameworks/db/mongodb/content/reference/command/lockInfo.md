---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/lockInfo.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# lockInfo (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     lockInfo: 1 
   } 
)
```

## Output Example

The following is an example of the output from the :dbcommand:`lockInfo`:

```javascript
{
   "lockInfo" : [
      {
         "resourceId" : "{2305843009213693953: ParallelBatchWriterMode, 1}",
         "granted" : [
            {
               "mode" : "IS",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            }
         ],
         "pending" : [ ]
      },
      {
         "resourceId" : "{6917529027641081857: Global, 1}",
         "granted" : [
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            },
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "index build: 29d48366-63ad-41e2-a689-69255a89c094",
               "clientInfo" : {
                  "desc" : "IndexBuildsCoordinatorMongod-0",
                  "opid" : 27437
               }
            }
         ],
         "pending" : [ ]
      },
      {
         "resourceId" : "{4611686018427387905: ReplicationStateTransition, 1}",
         "granted" : [
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            },
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "index build: 29d48366-63ad-41e2-a689-69255a89c094",
               "clientInfo" : {
                  "desc" : "IndexBuildsCoordinatorMongod-0",
                  "opid" : 27437
               }
            }
         ],
         "pending" : [ ]
      },
      {
         "resourceId" : "{10123292395995783581: Database, 899920359141007773, test}",
         "granted" : [
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            },
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "index build: 29d48366-63ad-41e2-a689-69255a89c094",
               "clientInfo" : {
                  "desc" : "IndexBuildsCoordinatorMongod-0",
                  "opid" : 27437
               }
            }
         ],
         "pending" : [ ]
      },
      {
         "resourceId" : "{12576221391967629173: Collection, 1047006345899159413, test.hugeindex}",
         "granted" : [
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            },
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "index build: 29d48366-63ad-41e2-a689-69255a89c094",
               "clientInfo" : {
                  "desc" : "IndexBuildsCoordinatorMongod-0",
                  "opid" : 27437
               }
            }
         ],
         "pending" : [ ]
      }
   ],
   "ok" : 1
}
```

## Output Fields

### Lock Information

For each `lockInfo.granted` or `lockInfo.pending` lock document, information include:
