---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-reshard-considerations.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Before you begin |operation| your collection, ensure that you meet the following requirements:

- .. include:: /includes/resharding-time-reqs.rst
- Your database meets these resource requirements:
- .. include:: /includes/reshard-storage-space.rst
- .. include:: /includes/resharding-mc-io.rst
- .. include:: /includes/resharding-mc-cpu.rst
.. include:: /includes/resharding-mc-important.rst

- You do not need to create an index on the new shard key before
resharding. The resharding operation builds the required indexes automatically during the index phase.

- No index builds are in progress. To check for running index builds,
use `$currentOp`:

```javascript
  db.getSiblingDB("admin").aggregate( [
     { $currentOp : { idleConnections: true } },
     { $match: {
           $or: [
               { "op": "command", "command.createIndexes": { $exists: true } },
               { "op": "none", "msg": /^Index Build/ }
           ]
        }
     }
  ] )

In the result document, if the ``inprog`` field value is an empty
array, there are no index builds in progress:

.. code-block:: javascript
  :copyable: false

  {
     inprog: [],
     ok: 1,
     '$clusterTime': { ... },
     operationTime: <timestamp>
  }
```
