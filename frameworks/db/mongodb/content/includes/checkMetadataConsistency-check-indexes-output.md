---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/checkMetadataConsistency-check-indexes-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
