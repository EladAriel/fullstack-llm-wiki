---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-compound/create-compound-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Create a Compound Index

**Compound indexes** are indexes that contain references to multiple fields. Compound indexes improve performance for queries on exactly the fields in the index or fields in the `index prefix <compound-index-prefix>`.

To create a compound index, use the :method:`db.collection.createIndex()` method:

.. include:: /includes/indexes/code-examples/create-compound-index.rst

## Restriction

You can specify up to 32 fields in a single compound index.

## Before You Begin

Create a `students` collection that contains these documents:

```javascript
db.students.insertMany([
   {
      "name": "Alice",
      "gpa": 3.6,
      "location": { city: "Sacramento", state: "California" }
   },
   {
      "name": "Bob",
      "gpa": 3.2,
      "location": { city: "Albany", state: "New York" }
   }
])
```

## Procedure

The following operation creates a compound index containing the `name` and `gpa` fields:

```javascript
db.students.createIndex( {
   name: 1, 
   gpa: -1
} )
```

In this example:

- The index on `name` is ascending (`1`).
- The index on `gpa` is descending (`-1`).
## Results

The created index supports queries that select on:

- Both `name` and `gpa` fields.
- Only the `name` field, because `name` is a :ref:`prefix
<compound-index-prefix>` of the compound index.

For example, the index supports these queries:

```javascript
db.students.find( { name: "Alice", gpa: 3.6 } )

db.students.find( { name: "Bob" } )
```

The index **does not** support queries on only the `gpa` field, because `gpa` is not part of the index prefix. For example, the index does not support this query:

```javascript
db.students.find( { gpa: { $gt: 3.5 } } )
```

## Learn More

- To learn how to create efficient compound indexes, see
`esr-indexing-guideline`.

- To learn how sort order (ascending or descending) impacts performance
of compound indexes, see `sorting-with-indexes`.

- To learn about other index types, see `index-types`.
- To learn what properties you can specify for indexes, see
`index-properties`.
