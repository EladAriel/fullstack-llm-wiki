---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/search.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $search (aggregation stage)

`$search` aggregation pipeline stage performs a full-text search of the field or fields in an Atlas collection. The fields must be covered by a :atlas:`{+fts+} </reference/atlas-search/index-definitions/>` index.

> **Important:** The `$search` aggregation pipeline stage is available for collections
hosted on:
- :atlas:`MongoDB Atlas </>`.
- `MongoDB Enterprise <install-mdb-enterprise>` deployments running
  version 8.2 or later with the `{+k8s-op-short+} <k8s-operator>`.
- `MongoDB Community <install-mdb-community-edition>` deployments
  running version 8.2 or later.
To learn more, see :atlas:`{+fts+} </atlas-search/>`.

For example, you can use `$search` to perform the following types of operations:

- Searches to match text fields with various patterns.
- Fuzzy matches to find terms with spelling variations.
- Compound queries to combine multiple search conditions.
- Relevance scoring to rank results.
- Return snippets of matching text.
- Vector searches to find documents using vector similarities.
For more details, see:

- :atlas:`Index Definitions
</reference/atlas-search/index-definitions/>` to learn more about creating and managing {+fts+} indexes.

- :atlas:`{+fts+} Aggregation Pipeline Stages
</reference/atlas-search/query-syntax/>` to learn more about the `$search` pipeline stage syntax and usage.

- :atlas:`$search Operators </reference/atlas-search/operators/>` to
learn more about the `$search` aggregation pipeline stage operators.
