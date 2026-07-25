---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text/text-index-versions.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
