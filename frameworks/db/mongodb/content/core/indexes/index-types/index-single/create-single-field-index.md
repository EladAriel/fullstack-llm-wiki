---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-single/create-single-field-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# Create an Index on a Single Field

You can create an index on a single field to improve performance for queries on that field.

To create a single-field index, use the :method:`db.collection.createIndex()` method:

.. include:: /includes/indexes/code-examples/create-single-field-index.rst

## Before You Begin

Create a `students` collection that contains the following documents:

```javascript
db.students.insertMany( [
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
] )
```

## Procedures

The following examples show you how to:

- `index-create-ascending-single-field`
- `index-embedded-fields`
### Create an Index on a Single Field

Consider a school administrator who frequently looks up students by their :abbr:`GPA (Grade Point Average)`. You can create an index on the `gpa` field to improve performance for those queries:

```javascript
db.students.createIndex( { gpa: 1 } )
```

Results ```````

The index supports queries that select on the field `gpa`, such as the following:

```javascript
db.students.find( { gpa: 3.6 } )

db.students.find( { gpa: { $lt: 3.4 } } )
```

### Create an Index on an Embedded Field

You can create indexes on fields within embedded documents. Indexes on embedded fields can fulfill queries that use `dot notation`.

The `location` field is an embedded document that contains the embedded fields `city` and `state`. Create an index on the `location.state` field:

```javascript
db.students.createIndex( { "location.state": 1 } )
```

Results ```````

The index supports queries on the field `location.state`, such as the following:

```javascript
db.students.find( { "location.state": "California" } )

db.students.find( { "location.city": "Albany", "location.state": "New York" } )
```

## Learn More

- `index-embedded-documents`
- `index-create-multikey-embedded`
- `Check if a query uses an index <index-measure-index-use>`
- `Learn about other types of index types <index-types>`
