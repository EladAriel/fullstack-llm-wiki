---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/checkMetadataConsistency-check-indexes-output.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

```javascript
{
  cursor: {
    id: Long('0'),
    ns: 'test.$cmd.aggregate',
    firstBatch: [
      {
        type: 'InconsistentIndex',
        description: 'Found an index of a sharded collection that is inconsistent between different shards',
        details: {
          namespace: 'test.reviews',
          info: { 
            missingFromShards: [],
            inconsistentProperties: [
              { k: 'expireAfterSeconds', v: Long('600') },
              { k: 'expireAfterSeconds', v: 3600 }
            ],
            indexName: 'reviewDt_1'
          }
        }
      },
      {
        type: 'InconsistentIndex',
        description: 'Found an index of a sharded collection that is inconsistent between different shards',
        details: {
          namespace: 'test.reviews',
          info: {
            missingFromShards: [ 'shard02' ],
            inconsistentProperties: [],
            indexName: 'page_1_score_1'
          }
        }
      }
    ]
  },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1752574769, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1752574760, i: 1 })
}
```
