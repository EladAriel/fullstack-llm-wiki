---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshardCollection-syntax.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```javascript
db.adminCommand(
   {
     reshardCollection: "<database>.<collection>",
     key: { "<shardkey>" },
     unique: <boolean>,
     numInitialChunks: <integer>,
     numSamplesPerChunk: <integer>,  // New in MongoDB 8.0.20
     collation: { locale: "simple" },
     zones: [
         {
             min: { "<document with same shape as shardkey>" },
             max: { "<document with same shape as shardkey>" },
             zone: <string> | null
         },
     ],
     forceRedistribution: <bool>
   }
)
```
