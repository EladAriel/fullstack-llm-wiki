---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/create-index/specify-index-name.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================

# Specify an Index Name

When you create an index, you can give the index a custom name. Giving your index a name helps distinguish different indexes on your collection. For example, you can more easily identify the indexes used by a query in the query plan's `explain results <explain-results>` if your indexes have distinct names.

To specify the index name, include the `name` option when you create the index:

```javascript
db.<collection>.createIndex( 
   { <field>: <value> }, 
   { name: "<indexName>" } 
)
```

## About this Task

Before you specify an index name, consider the following:

- Index names must be unique. Creating an index with
the name of an existing index returns an error.

- You can't rename an existing index. Instead, you must :ref:`drop
<drop-an-index>` and recreate the index with a new name.

### Default Index Names

If you don't specify a name during index creation, the system generates the name by concatenating each index key field and value with underscores. For example:

## Procedure

A `blog` collection contains data about blog posts and user interactions.

Create a text index on the `content`, `users.comments`, and `users.profiles` fields. Set the index `name` to `InteractionsTextIndex`:

```javascript
db.blog.createIndex(
   {
     content: "text",
     "users.comments": "text",
     "users.profiles": "text"
   },
   {
     name: "InteractionsTextIndex"
   }
)
```

## Results

After you create the index, you can use the :method:`db.collection.getIndexes()` method to get the index name:

```javascript
db.blog.getIndexes()
```

Output:

```javascript
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  {
    v: 2,
    key: { _fts: 'text', _ftsx: 1 },
    name: 'InteractionsTextIndex',
    weights: { content: 1, 'users.comments': 1, 'users.profiles': 1 },
    default_language: 'english',
    language_override: 'language',
    textIndexVersion: 3
  }
]
```

## Learn More

- To learn how to create an index, see `manual-create-an-index`.
- For more information about index properties, see `index-properties`.
