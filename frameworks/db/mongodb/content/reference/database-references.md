---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/database-references.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================

# Database References

For most MongoDB use cases, the denormalized data model stores related data in a single `document <document>`. In some cases, you need to store related information in separate documents, typically in different collections or databases.

> **Important:** You can use the :pipeline:`$lookup` pipeline stage to perform
a left outer join to an unsharded collection in the same database.
You can also use the :pipeline:`$graphLookup` pipeline stage to join an
unsharded collection to perform recursive search.

This page outlines alternative procedures that predate the :pipeline:`$lookup` and :pipeline:`$graphLookup` pipeline stages.

MongoDB applications use one of two methods to relate documents:

- `Manual references <document-references>` save the
`_id` field of one document in another document as a reference. Your application runs a second query to return the related data. These references are simple and sufficient for most use cases.

- `DBRefs <dbref-explanation>` are references from one document
to another using the value of the first document's `_id` field, collection name, and, optionally, its database name, as well as any other fields. DBRefs let you reference documents stored in multiple collections or databases.

To resolve DBRefs, your application must perform additional queries to return the referenced documents. Some :driver:`MongoDB drivers </>` provide helper methods that resolve DBRefs into documents, but resolution is not automatic.

DBRefs provide a common format and type to represent relationships among documents. The format also provides common semantics for representing links between documents when your database interacts with multiple frameworks and tools.

Unless you have a compelling reason to use DBRefs, use manual references instead.

## Manual References

### Background

A manual reference includes the `_id` field of one `document <document>` in another document. The application can then run a second query to resolve the referenced fields as needed.

### Create a Manual Reference in the {+atlas+} UI

To create a manual reference in the {+atlas+} UI, follow these steps:

### Create a Manual Reference in the Terminal

Consider the following operation to insert two documents, using the `_id` field of the first document as a reference in the second document:

```javascript
original_id = ObjectId()

db.places.insertOne({
    "_id": original_id,
    "name": "Broadway Center",
    "url": "bc.example.net"
})

db.people.insertOne({
    "name": "Erin",
    "places_id": original_id,
    "url":  "bc.example.net/Erin"
})
```

Then, when a query returns the document from the `people` collection you can, if needed, make a second query for the document referenced by the `places_id` field in the `places` collection.

### Use

For almost every case where you want to store a relationship between two documents, use `manual references <document-references>`. They are simple to create and your application can resolve them as needed.

Manual references do not convey the database and collection names. If documents in a single collection relate to documents in more than one collection, consider using DBRefs.

## DBRefs

### Background

DBRefs are a convention for representing a `document, rather than a specific reference type. They include the name of the collection, and in some cases the database name, in addition to the value from the id` field.

Optionally, DBRefs can include any number of other fields. Extra field names must follow the `rules for field names <limit-restrictions-on-field-names>` imposed by the server version.

### Format

DBRefs have the following fields:

> **Note:** The order of fields in the DBRef matters, and you must use the above
sequence when using a DBRef.

### Driver Support for DBRefs

### Use

In most cases, use `manual references <document-references>` to connect two or more related documents. If you need to reference documents from multiple collections, consider using DBRefs.
