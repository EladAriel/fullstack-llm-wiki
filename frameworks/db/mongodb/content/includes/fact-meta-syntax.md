---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-meta-syntax.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
