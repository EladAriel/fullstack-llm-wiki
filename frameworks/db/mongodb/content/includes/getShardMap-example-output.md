---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/getShardMap-example-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```json
{
  map: {
    shard01: 'shard01/localhost:27018,localhost:27019,localhost:27020',
    shard02: 'shard02/localhost:27021,localhost:27022,localhost:27023',
    shard03: 'shard03/localhost:27024,localhost:27025,localhost:27026',
    config: 'configRepl/localhost:27027'
  },
  hosts: {
    'localhost:27026': 'shard03',
    'localhost:27020': 'shard01',
    'localhost:27021': 'shard02',
    'localhost:27024': 'shard03',
    'localhost:27022': 'shard02',
    'localhost:27018': 'shard01',
    'localhost:27025': 'shard03',
    'localhost:27019': 'shard01',
    'localhost:27023': 'shard02',
    'localhost:27027': 'config'
 },
 connStrings: {
    'shard01/localhost:27018,localhost:27019,localhost:27020': 'shard01',
    'shard02/localhost:27021,localhost:27022,localhost:27023': 'shard02',
    'shard03/localhost:27024,localhost:27025,localhost:27026': 'shard03',
    'configRepl/localhost:27027': 'config'
 },
 ok: 1,
 '$clusterTime': {
    clusterTime: Timestamp({ t: 1760637565, i: 2 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
   }
 },
 operationTime: Timestamp({ t: 1760637565, i: 2 })
}
```
