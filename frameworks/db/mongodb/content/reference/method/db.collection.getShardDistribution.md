---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.getShardDistribution.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================================

# db.collection.getShardDistribution() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`~db.collection.getShardDistribution()` method has the following form:

```javascript
db.collection.getShardDistribution()
```

## Output

> **Note:** The behavior of `getShardDistribution()` changed in MongoDB Shell
version 2.3.3:
- Starting in MongoDB Shell version 2.3.3, `getShardDistribution()`
 only contains regular sharded data and does not account for
 `orphaned documents <orphaned document>`.
- Prior to MongoDB Shell version 2.3.3, `getShardDistribution()`
 accounts for both regular sharded data and orphaned documents
 pending deletion. If the collection contains orphaned documents,
 `getShardDistribution()` might indicate that the collection is
 unbalanced even if the collection is balanced in terms of regular
 data. The shard containing orphaned data has more documents and
 greater data size, but the same number of chunks compared to other
 shards.

### Sample Output

The following is a sample output for the distribution of a sharded collection:

```none
Shard shard01 at shard01/localhost:27018
{
  data: '38.14MB',
  docs: 1000003,
  chunks: 2,
  'estimated data per chunk': '19.07B',
  'estimated docs per chunk': 500001
}
---
Shard shard02 at shard02/localhost:27019
{
  data: '38.14B',
  docs: 999999,
  chunks: 3,
  'estimated data per chunk': '12.71B',
  'estimated docs per chunk': 333333
}
---
Totals
{
  data: '76.29B',
  docs: 2000002,
  chunks: 5,
  'Shard shard01': [ '50 % data', '50 % docs in cluster', '40B avg obj size on shard' ],
  'Shard shard02': [ '49.99 % data', '49.99 % docs in cluster', '40B avg obj size on shard' ]
}
```

### Output Fields

```none
Shard shard01 at <host-a>   {
  data: <size-a>,
  docs: <count-a>,
  chunks: <number of chunks-a>,
  'estimated data per chunk': <size-a>/<number of chunks-a>,
  'estimated docs per chunk': <count-a>/<number of chunks-a>
}
---
Shard shard02 at <host-b>
{
  data: <size-b>,
  docs: <count-b>,
  chunks: <number of chunks-b>,
  'estimated data per chunk': <size-b>/<number of chunks-b>,
  'estimated docs per chunk': <count-b>/<number of chunks-b>
}
---
Totals
{
  data: <stats.size>,
  docs: <stats.count>,
  chunks: <calc total chunks>,
  Shard shard01: [ <estDataPercent-a> % data, <estDocPercent-a> % docs in cluster, stats.shards[ <shard-a> ].avgObjSize avg obj size on shard ],
  Shard shard02: [ <estDataPercent-b> % data, <estDocPercent-b> % docs in cluster, stats.shards[ <shard-b> ].avgObjSize avg obj size on shard ]
}
```

The output information displays:

## Behavior

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst
