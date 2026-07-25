---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-wildcard/reference/wildcard-projection-signature.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================

# Wildcard Index Signature

Starting in MongoDB 5.0, the `wildcardProjection` option for `wildcard indexes <wildcard-index-core>` is included in the `index signature`. This means that you can create multiple wildcard indexes with the same `key pattern <key_patterns>` as long as the `wildcardProjection` options do not contain the same fields.

## Projection Signature Display

.. include:: /includes/indexes/fact-wildcard-index-ordering.rst

## Example

Consider the following wildcard index on a `books` collection:

```javascript
db.books.createIndex( 
   {
      "$**": 1
   }, 
   {
      wildcardProjection: {
         "author.name": 1,
         "author.website": 1   
      },
      name: "authorWildcard"
   }
)
```

The index key pattern is `"$**"`. You can create another wildcard index with the same key pattern if you specify a different `wildcardProjection`. For example:

```javascript
db.books.createIndex( 
   {
      "$**": 1
   }, 
   {
      wildcardProjection: {
         "publisher.name": 1
      },
      name: "publisherWildcard"
   }
)
```

To view the created indexes, run the :method:`~db.collection.getIndexes()` method:

```javascript
db.books.getIndexes()
```

Output:

```javascript
[
   { v: 2, key: { _id: 1 }, name: '_id_' },
   {
      v: 2,
      key: { '$**': 1 },
      name: 'authorWildcard',
      wildcardProjection: { author: { website: true, name: true }, _id: false }
   },
   {
      v: 2,
      key: { '$**': 1 },
      name: 'publisherWildcard',
      wildcardProjection: { publisher: { name: true }, _id: false }
   }
]
```

## Learn More

- `createIndex-method-wildcard-option`
- `wildcard-index-restrictions`
