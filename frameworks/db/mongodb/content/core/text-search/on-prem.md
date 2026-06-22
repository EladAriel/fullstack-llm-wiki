---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/text-search/on-prem.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============

# $text Queries

.. include:: /includes/extracts/fact-text-search-legacy-atlas.rst

.. include:: /includes/fact-text-index.rst

See the `<index-type-text>` section for a full reference on text indexes, including behavior, tokenization, and properties.

## Examples

This example demonstrates how to build a text index and use it to find coffee shops, given only text fields.

### Create a Collection

Create a collection `stores` with the following documents:

```javascript
db.stores.insertMany(
   [
     { _id: 1, name: "Java Hut", description: "Coffee and cakes" },
     { _id: 2, name: "Burger Buns", description: "Gourmet hamburgers" },
     { _id: 3, name: "Coffee Shop", description: "Just coffee" },
     { _id: 4, name: "Clothes Clothes Clothes", description: "Discount clothing" },
     { _id: 5, name: "Java Shopping", description: "Indonesian goods" },
     { _id: 6, name: "NYC_Coffee Shop", description: "local NYC coffee" }
   ]
)
```

### Create a Text Index

.. include:: /includes/fact-create-text-index.rst

### Search for an Exact String

You can search for exact multi-word strings by wrapping them in double-quotes. `$text` queries only match documents that include the whole string.

For example, the following query finds all documents that contain the string "coffee shop":

```javascript
db.stores.find( { $text: { $search: "\"coffee shop\"" } } )
```

This query returns the following documents:

```javascript
[
   { _id: 3, name: 'Coffee Shop', description: 'Just coffee' },
   { _id: 6, name: 'NYC_Coffee Shop', description: 'local NYC coffee' }
]
```

Unless specified, exact string search is not case sensitive or diacritic sensitive. For example, the following query returns the same results as the previous query:

```javascript
db.stores.find( { $text: { $search: "\"COFFEé SHOP\"" } } )
```

Exact string search does not handle stemming or stop words.

### Exclude a Term

To exclude a word, you can prepend a "`-`" character. For example, to find all stores containing "java" or "shop" but not "coffee", use the following:

```javascript
db.stores.find( { $text: { $search: "java shop -coffee" } } )
```

### Sort the Results

MongoDB returns its results in unsorted order by default. However, `$text` queries compute a relevance score for each document that specifies how well a document matches the query.

To sort the results in order of relevance score, you must explicitly project the :expression:`$meta` `textScore` field and sort on it:

```javascript
db.stores.find(
   { $text: { $search: "java coffee shop" } },
   { score: { $meta: "textScore" } }
).sort( { score: { $meta: "textScore" } } )
```

`$text` is also available in the aggregation pipeline.

## Contents

- $text Query Operators </core/text-search-operators>
- Aggregation Pipeline </tutorial/text-search-in-aggregation>
- Languages </reference/text-search-languages>
- Text Indexes </core/indexes/index-types/index-text>
