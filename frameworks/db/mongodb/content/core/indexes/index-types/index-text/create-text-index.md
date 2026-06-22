---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text/create-text-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Create a Text Index on Self-Managed Deployments

.. include:: /includes/fact-fts-avs-text-index.rst

.. include:: /includes/indexes/text-index-intro.rst

To create a text index, use the :method:`db.collection.createIndex()` method. To index a field that contains a string or an array of string elements, specify the string `"text"` as the index key:

.. include:: /includes/indexes/code-examples/create-text-index.rst

## About this Task

- .. include:: /includes/fact-text-index-limit-one.rst
- You can index multiple fields in a single text index. A text index can
contain up to 32 fields. To see an example, see `compound-text-index-example`.

## Before You Begin

.. include:: /includes/indexes/text-search-blog-example-documents.rst

## Procedures

The following examples show you how to:

- `single-text-index-example`
- `compound-text-index-example`
### Create a Single-Field Text Index

Create a text index on the `content` field:

```javascript
db.blog.createIndex( { "content": "text" } )
```

The index supports `$text` queries on the `content` field. For example, the following query returns documents where the `content` field contains the string `coffee`:

```javascript
db.blog.find(
   {
      $text: { $search: "coffee" }
   }
)
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

Matches on Non-Indexed Fields `````````````````````````````

The `{ "content": "text" }` index only includes the `content` field, and does not return matches on non-indexed fields. For example, the following query searches the `blog` collection for the string `food`:

```javascript
db.blog.find(
   {
      $text: { $search: "food" }
   }
)
```

The preceding query returns no documents. Although the string `food appears in documents id: 2 and id: 3`, it appears in the `about` and `keywords` fields respectively. The `about` and `keywords` fields are not included in the text index, and therefore do not affect `$text` query results.

### Create a Compound Text Index

> **Note:** Before you can create the index in this example, you must :ref:`drop
any existing text indexes <drop-an-index>` on the `blog`
collection.

Create a compound text index on the `about` and `keywords` fields in the `blog` collection:

```javascript
db.blog.createIndex(
   {
      "about": "text",
      "keywords": "text"
   }
)
```

The index supports `$text` queries on the `about` and `keywords` fields. For example, the following query returns documents where the string `food` appears in either the `about` or `keywords` field:

```javascript
db.blog.find(
   {
      $text: { $search: "food" }
   }
)
```

Output:

```javascript
[
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
