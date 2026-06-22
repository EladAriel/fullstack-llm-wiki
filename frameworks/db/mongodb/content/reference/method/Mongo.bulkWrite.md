---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.bulkWrite.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# Mongo.bulkWrite() (mongosh method)

## Definition

`Mongo.bulkWrite()` performs multiple write operations across multiple databases and collections in a single call, unlike :method:`db.collection.bulkWrite()` which operates on a single collection.

> **Note:** Requires MongoDB 8.0 or later.

## Syntax

You can call `bulkWrite()` on the current :method:`Mongo` instance by using the following syntax:

```javascript
db.getMongo().bulkWrite( 
  [
    { 
      namespace: "<db1.collection1>",
      name: "insertOne",
      document: { ... }
    },
    {
      namespace: "<db2.collection2>",
      name: "replaceOne",
      filter: { ... }
    }
  ],
  {
    ordered: boolean,
    verboseResults: boolean,
    bypassDocumentValidation: boolean,
    let: Document
  }
)
```

You can also call it on a different `Mongo` instance, like in the following example:

```javascript
const otherMongo = Mongo("<other connection string>");

otherMongo.bulkWrite([{ namespace: "<db.collection>", ... }]);
```

`bulkWrite()` accepts two parameters:

A document in `operations` can represent one of six operations:

- insert one
- replace one
- update one
- update many
- delete one
- delete many
The following sections describe the syntax you must use for documents that represent each operation.

### Insert One

```javascript
{
   namespace: '<db.collection>',
   name: 'insertOne',
   document: Document
}
```

> **Note:** If the document does not include an `_id` field,
`mongosh` automatically generates one.

### Update One and Update Many

`updateOne` updates the first document matching the filter. `updateMany` updates all documents matching the filter.

```javascript
{
   namespace: '<db>.<collection>',
   name: 'updateOne' | 'updateMany',
   filter: Document,
   update: Document | Document[],
   arrayFilters?: Document[],
   hint?: Document | string,
   collation?: Document,
   upsert?: boolean
}
```

### Replace One

```javascript
{
   namespace: '<db>.<collection>',
   name: 'replaceOne',
   filter: Document,
   replacement: Document,
   hint?: Document | string,
   collation?: Document
}
```

### Delete One or Many

`deleteOne` deletes the first document matching the filter. `deleteMany` deletes all documents matching the filter.

```javascript
{
   namespace: '<db>.<collection>',
   name: 'deleteOne' | 'deleteMany',
   filter: Document,
   hint?: Document | string,
   collation?: Document
}
```

### Options

```javascript
{
   ordered?: boolean,
   verboseResults?: boolean,
   bypassDocumentValidation?: boolean,
   let?: Document
}
```

## Output

`bulkWrite()` returns an object with the following fields:

```javascript
{
   acknowledged: boolean,
   insertedCount: int,
   matchedCount: int,
   modifiedCount: int,
   deletedCount: int,
   upsertedCount: int,
   insertResults?: map(int, document),
   updateResults?: map(int, document),
   deleteResults?: map(int, document)
}
```

## Examples

.. include:: /includes/reference/mongo-bulkwrite-example.rst
