---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text/text-index-versions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Text Index Versions on Self-Managed Deployments

.. include:: /includes/fact-fts-avs-text-index.rst

Text indexes are available in the following versions:

## Change Index Version

> **Important:** .. include:: /includes/indexes/index-version-callout.rst

To override the default version and specify a different version for your text index, set the `textIndexVersion` option when you create an index:

```javascript
db.<collection>.createIndex( 
   { <field>: "text" }, 
   { "textIndexVersion": <version> } 
)
```

### Example

The following command creates a version 2 text index on the `content` field:

```javascript
db.test.createIndex(
   { "content": "text" },
   { "textIndexVersion": 2 }
 )
```
