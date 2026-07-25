---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/index-unique/create.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# Create a Single-Field Unique Index

Unique indexes ensure that a value appears at most once for a given field.

To create a unique index in the MongoDB Shell, use the :method:`db.collection.createIndex()` method with the `unique` option set to `true`.

```javascript
db.collection.createIndex(
   { <field>: <sortOrder> },
   { unique: true }
 )
```

## About this Task

This example adds a unique index on the `user_id` field of a `members` collection to ensure that there are no duplicate values in the `user_id` field.

## Steps

To create a unique index on the `user_id` field of the `members` collection, run the following command in :binary:`~bin.mongosh`:

```javascript
db.members.createIndex( { "user_id": 1 }, { unique: true } )
```

## Learn More

- `index-unique-compound-index`
- `index-convert-to-unique`
