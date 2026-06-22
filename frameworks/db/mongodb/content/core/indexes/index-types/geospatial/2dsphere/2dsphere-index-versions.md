---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2dsphere/2dsphere-index-versions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# 2dsphere Index Versions

2dsphere indexes are available in the following versions:

## Change Index Version

> **Important:** .. include:: /includes/indexes/index-version-callout.rst

To override the default version and specify a different version for your 2dsphere index, set the `2dsphereIndexVersion` option when you create an index:

```javascript
db.<collection>.createIndex( 
   { <field>: "2dsphere" }, 
   { "2dsphereIndexVersion": <version> } 
)
```

### Example

The following command creates a version 2 2dsphere index on the `address` field:

```javascript
db.test.createIndex(
   { "address": "2dsphere" },
   { "2dsphereIndexVersion": 2 }
 )
```
