---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-meta-syntax.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A |meta-object| expression has the following syntax:

```javascript
{ $meta: <metaDataKeyword> }
```

The |meta-object| expression can specify the following values as the `<metaDataKeyword>`:

:atlas:`{+fts+} </full-text-search>` provides additional `$meta` keywords, such as:

- :atlas:`"searchScore" </atlas-search/scoring>`
- :atlas:`"searchHighlights" </atlas-search/highlighting>`
- :atlas:`"searchScoreDetails" </atlas-search/scoring>`
- :atlas:`"searchSequenceToken" </atlas-search/paginate-results>`
- :atlas:`"vectorSearchScore" </atlas-vector-search/vector-search-stage/#mongodb-vector-search-score>`
Refer to the {+fts+} documentation for details.
