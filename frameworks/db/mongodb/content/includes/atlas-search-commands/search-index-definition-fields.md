---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/atlas-search-commands/search-index-definition-fields.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The search index definition takes the following fields:

```javascript
{
   analyzer: "<analyzer-for-index>", 
   searchAnalyzer: "<analyzer-for-query>", 
   mappings: { 
      dynamic: <boolean>,
      fields: { <field-definition> } 
   },
   analyzers: [ <custom-analyzer> ],
   storedSource: <boolean> | {
      <stored-source-definition>
   },
   synonyms: [ {
      name: "<synonym-mapping-name>",
      source: {
         collection: "<source-collection-name>"
      },
      analyzer: "<synonym-mapping-analyzer>"
   } ]
}
```
