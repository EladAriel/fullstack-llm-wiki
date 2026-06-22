---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/atlas-search-commands/vector-search-index-definition-fields.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The vector search index definition takes the following fields:

```javascript
{
  "fields": [ 
    {
      "type": "vector" | "filter",
      "path": "<field-to-index>",
      "numDimensions": <number-of-dimensions>,
      "similarity": "euclidean" | "cosine" | "dotProduct"
    }
  ]
}
```

For explanations of vector search index definition fields, see `avs-types-vector-search`.
