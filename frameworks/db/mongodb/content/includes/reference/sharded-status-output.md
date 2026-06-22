---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/sharded-status-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```javascript
<dbname>.<collection>
   shard key: { <shard key> : <1 or hashed> }
   unique: <boolean>
   balancing: <boolean>
   allowMigrations: <boolean>
   chunks:
      <shard name1> <number of chunks>
      <shard name2> <number of chunks>
      ...
   { <shard key>: <min range1> } -->> { <shard key> : <max range1> } on : <shard name> <last modified timestamp>
   { <shard key>: <min range2> } -->> { <shard key> : <max range2> } on : <shard name> <last modified timestamp>
   ...
   tag: <tag1>  { <shard key> : <min range1> } -->> { <shard key> : <max range1> }
   ...
```
