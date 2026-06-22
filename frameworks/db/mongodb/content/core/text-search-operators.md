---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/text-search-operators.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================

# $text Query Operators

.. include:: /includes/extracts/fact-text-search-legacy-atlas.rst

## Query Framework

.. include:: /includes/fact-use-text-operator.rst

Use the :expression:`$meta` query operator to obtain and sort by the relevance score of each matching document. For example, to order a list of coffee shops in order of relevance, run the following:

```javascript
db.stores.find(
   { $text: { $search: "coffee shop cake" } },
   { score: { $meta: "textScore" } }
).sort( { score: { $meta: "textScore" } } )
```

For more information on the :query:`$text` and :expression:`$meta` operators, including restrictions and behavior, see:

- :query:`$text Reference Page <$text>`
- `$text Query Examples <text-query-examples>`
- `$meta as a projection operator <meta-projection-usage>`
## Aggregation Pipeline

When working with `aggregation <aggregation>` pipelines, use :pipeline:`$match` with a `$text` expression. To sort the results in order of relevance score, use the :expression:`$meta` aggregation operator in the :pipeline:`$sort` stage.

For more information and examples, see `text-agg`.

.. include:: /includes/fact-atlas-search-search-stage.rst

## Contents

- $text </reference/operator/query/text>
