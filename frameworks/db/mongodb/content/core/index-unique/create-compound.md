---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/index-unique/create-compound.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# Create a Compound Unique Index

You enforce a unique constraint on `compound indexes <index-type-compound>`. A unique compound index enforces uniqueness on the combination of the index key values.

To create a unique index in the MongoDB Shell, use the :method:`db.collection.createIndex()` method with the `unique` option set to `true`.

```javascript
db.collection.createIndex(
   {
      <field1>: <sortOrder>,
      <field2>: <sortOrder>,
      ...
      <fieldN>: <sortOrder>
   },
   { unique: true }
 )
```

## About this Task

This example adds a unique compound index on the `groupNumber`, `lastname`, and `firstname` fields of a `members` collection. The index ensures that the combination of these field values is unique for each document in the collection.

## Steps

To create a unique index on `groupNumber`, `lastname`, and `firstname` fields of the `members` collection, run the following command in :binary:`~bin.mongosh`:

```javascript
db.members.createIndex(
   { groupNumber: 1, lastname: 1, firstname: 1 },
   { unique: true }
)
```

The created index enforces uniqueness for the combination of `groupNumber`, `lastname`, and `firstname` values.

## Compound Unique Indexes on Fields with Embedded Arrays

Consider a collection with the following document:

```javascript
db.myColl.insertOne(
   { _id: 1, a: [ { loc: "A", qty: 5 }, { qty: 10 } ] }
)
```

Create a unique compound `multikey <index-type-multikey>` index on `a.loc` and `a.qty`:

```javascript
db.myColl.createIndex( { "a.loc": 1, "a.qty": 1 }, { unique: true } )
```

The unique index permits the insertion of the following documents into the collection since the index enforces uniqueness for the combination of `a.loc` and `a.qty` values:

```javascript
db.myColl.insertMany( [
   { _id: 2, a: [ { loc: "A" }, { qty: 5 } ] },
   { _id: 3, a: [ { loc: "A", qty: 10 } ] }
] )
```

## Learn More

- `unique-separate-documents`
- `unique-index-and-missing-field`
