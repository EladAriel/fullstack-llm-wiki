---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/text-search.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========

# Text Search

MongoDB provides text search capabilities for both :atlas:`MongoDB Atlas </>` and self-managed deployments.

> **Note:** :pipeline:`$search`, :pipeline:`$searchMeta`, and :expression:`$vectorSearch`
are now available in self-managed deployments. We recommend using these
aggregation stages instead of the :query:`$text` operator, as they offer an
improved full-text-query solution.

## {+fts+}

To perform text search, use :atlas:`{+fts+}  </atlas-search>`. {+fts+} supports fine-grained text indexing and a rich query language for fast, relevant search results.

To learn more and get started with {+fts+}, see:

- :atlas:`{+fts+} Aggregation Pipeline Stages
</reference/atlas-search/query-syntax/>`

- :atlas:`Defining {+fts+} Indexes
</reference/atlas-search/index-definitions/>`

- :atlas:`Running {+fts+} Queries
</reference/atlas-search/searching/>`

.. include:: /includes/fact-atlas-search-languages.rst

## {+avs+}

To perform vector search on your data hosted on MongoDB, use :atlas:`{+avs+} </atlas-vector-search/vector-search-overview/>`. {+avs+} extends your text search capabilities to include semantic, hybrid, and generative search.

To learn more and get started with {+avs+}, see:

- :atlas:`{+avs+} Quick Start
</atlas-vector-search/tutorials/vector-search-quick-start/>`

- :atlas:`Run Vector Search Queries
</atlas-vector-search/vector-search-stage>`

## Queries with the `$text` Operator

MongoDB also provides the :query:`$text` operator. However, we recommend using the :pipeline:`$search` aggregation stage as it offers advanced full-text search options, including:

- Fuzzy matching and autocomplete.
- Relevance scoring.
- Support for search using synonyms and facets.
- Search term highlighting.
- More language analyzers.
To learn more about `$text` queries, see `text-search-on-prem`.

## Contents

- {+fts+} <https://www.mongodb.com/docs/atlas/atlas-search/>
- {+avs+} <https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/>
