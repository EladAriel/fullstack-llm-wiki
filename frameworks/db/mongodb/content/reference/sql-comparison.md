---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/sql-comparison.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# SQL to MongoDB Mapping Chart

In addition to the charts that follow, you might want to consider the `Frequently Asked Questions <faq-fundamentals>` section for a selection of common questions about MongoDB.

## Terminology and Concepts

The following table presents the various SQL terminology and concepts and the corresponding MongoDB terminology and concepts.

## Executables

The following table presents some database executables and the corresponding MongoDB executables. This table is not meant to be exhaustive.

## Examples

The following table presents the various SQL statements and the corresponding MongoDB statements. The examples in the table assume the following conditions:

- The SQL examples assume a table named `people`.
- The MongoDB examples assume a collection named `people` that contain
documents of the following prototype:

```javascript
  {
    _id: ObjectId("509a8fb2f3f4948bd2f983a0"),
    user_id: "abc123",
    age: 55,
    status: 'A'
  }
```

### Create and Alter

The following table presents the various SQL statements related to table-level actions and the corresponding MongoDB statements.

For more information on the methods and operators used, see:

- :method:`db.collection.insertOne()`
- :method:`db.collection.insertMany()`
- :method:`db.createCollection()`
- :method:`db.collection.updateMany()`
- :method:`db.collection.createIndex()`
- :method:`db.collection.drop()`
- :update:`$set`
- :update:`$unset`
### Insert

The following table presents the various SQL statements related to inserting records into tables and the corresponding MongoDB statements.

For more information, see :method:`db.collection.insertOne()`.

### Select

The following table presents the various SQL statements related to reading records from tables and the corresponding MongoDB statements.

> **Note:** The :method:`~db.collection.find() method always includes the id`
field in the returned documents unless specifically excluded through
`projection<projection>`. Some of the SQL queries below may include an
`_id` field to reflect this, even if the field is not included in the
corresponding :method:`~db.collection.find()` query.

For more information on the methods and operators used, see

- :method:`db.collection.find()`
- :method:`db.collection.distinct()`
- :method:`db.collection.findOne()`
- :method:`~cursor.limit()`
- :method:`~cursor.skip()`
- :method:`~cursor.explain()`
- :method:`~cursor.sort()`
- :method:`~cursor.count()`
- :query:`$ne`
- :query:`$and`
- :query:`$or`
- :query:`$gt`
- :query:`$lt`
- :query:`$exists`
- :query:`$lte`
- :query:`$regex`
### Update Records

The following table presents the various SQL statements related to updating existing records in tables and the corresponding MongoDB statements.

For more information on the method and operators used in the examples, see:

- :method:`db.collection.updateMany()`
- :query:`$gt`
- :update:`$set`
- :update:`$inc`
### Delete Records

The following table presents the various SQL statements related to deleting records from tables and the corresponding MongoDB statements.

For more information, see :method:`db.collection.deleteMany()`.
