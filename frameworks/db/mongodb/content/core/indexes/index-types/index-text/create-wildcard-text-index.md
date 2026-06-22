---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text/create-wildcard-text-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================================

# Create a Wildcard Text Index on Self-Managed Deployments

> **Note:** :atlas:`{+fts+} </atlas-search/>` offers advanced full-text search
capabilities, including :ref:`configurable dynamic indexing
<fts-configure-dynamic-mappings>`. We recommend using
`{+fts+} indexes <fts-manage-indexes>` instead of text indexes.

You can create a text index that contains every document field with string data in a collection. These text indexes are called **wildcard text indexes**. Wildcard text indexes support :query:`$text` `queries <text-search-on-prem>` on unknown, arbitrary, or dynamically generated fields.

To create a wildcard text index, set the index key to the wildcard specifier (`$**`) and set the index value to `text`:

```javascript
db.<collection>.createIndex( { "$**": "text" } )
```

## About this Task

Wildcard text indexes are distinct from `wildcard indexes <wildcard-index-core>`. Wildcard text indexes support queries that use the :query:`$text` operator, while wildcard indexes do not.

.. include:: /includes/text-search-legacy-atlas-section.rst

After you create a wildcard text index, when you insert or update documents, the index updates to include any new string field values. As a result, wildcard text indexes negatively impact performance for inserts and updates.

Only use wildcard text indexes when the fields you want to index are unknown or may change. Wildcard text indexes don't perform as well as targeted text indexes on specific fields. If your collection contains arbitrary field names that prevent targeted indexes, consider remodeling your schema to have consistent field names. To learn more about targeted indexes, see `create-indexes-to-support-queries`.

## Before You Begin

.. include:: /includes/indexes/text-search-blog-example-documents.rst

## Procedure

Create a wildcard text index on the `blog` collection:

```javascript
db.blog.createIndex( { "$**": "text" } )
```

## Results

The wildcard text index supports `$text` queries on all fields in the collection. Consider the following queries:

### Search for a Single Word

Query the `blog` collection for the string `coffee`:

```javascript
db.blog.find( { $text: { $search: "coffee" } } )
```

Output:

```javascript
[
  {
    _id: 1,
    content: 'This morning I had a cup of coffee.',
    about: 'beverage',
    keywords: [ 'coffee' ]
  },
  {
    _id: 3,
    content: 'My favorite flavors are strawberry and coffee',
    about: 'ice cream',
    keywords: [ 'food', 'dessert' ]
  }
]
```

The preceding query returns all documents that contain the string `coffee` in any field.

### Search for Multiple Terms

Query the `blog` collection for documents that contain the string `poll` **or** `coffee`:

```javascript
db.blog.find( { $text: { $search: "poll coffee" } } )
```

Output:

```javascript
[
  {
    _id: 1,
    content: 'This morning I had a cup of coffee.',
    about: 'beverage',
    keywords: [ 'coffee' ]
  },
  {
    _id: 3,
    content: 'My favorite flavors are strawberry and coffee',
    about: 'ice cream',
    keywords: [ 'food', 'dessert' ]
  },
  {
    _id: 2,
    content: 'Who likes chocolate ice cream for dessert?',
    about: 'food',
    keywords: [ 'poll' ]
  }
]
```

The preceding query returns documents that contain the string `poll` or `coffee` in any field.

### Search for an Exact String

Query the `blog` collection for documents that contain the exact string `chocolate ice cream`:

```javascript
db.blog.find( { $text: { $search: "\"chocolate ice cream\"" } } )
```

Output:

```javascript
[
  {
    _id: 2,
    content: 'Who likes chocolate ice cream for dessert?',
    about: 'food',
    keywords: [ 'poll' ]
  }
]
```

The preceding query returns documents that contain the exact string `chocolate ice cream` in any field.

## Learn More

- To learn how to control the ranking of `$text` query results, see
`specify-weights`.

- You can include a wildcard text index as part of a compound text
index. To learn more about compound text indexes, see `compound-text-index-example`.

- To see examples of `$text` queries, see :query:`$text`.
.. include:: /includes/text-search-legacy-atlas-section.rst

- To learn about text index properties such as case sensitivity, see
`text-index-properties`.
