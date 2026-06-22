---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/embedding.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Embedded Data in Your MongoDB Schema

Embedded documents store related data in a single document structure. A document can contain arrays and sub-documents with related data. These **denormalized** data models allow applications to retrieve related data in a single database operation.

In the following example, the `contact` and `access` fields are embedded documents:

.. include:: /images/data-model-denormalized.rst

Embedded data models are often considered **denormalized** because frequently-accessed data is duplicated in multiple collections.

Embedded data models let applications query related pieces of information in the same database record. As a result, embedding provides the following benefits:

- Better performance for read operations
- The ability to retrieve related data in a single database operation
- The ability to update related data in a single atomic write
operation

Embedded documents store related data in a single document structure. A document can contain arrays and sub-documents with related data. These **denormalized** data models allow applications to retrieve related data in a single database operation.

> **Note:** Documents in MongoDB must be smaller than 16 mebibytes.
For large binary data, consider `GridFS <gridfs>`.

## Use Cases

Use embedded data models in the following scenarios:

- You have "contains" relationships between entities. For example, a
`contacts` document that contains an `address`. See `data-modeling-example-one-to-one`.

- You have one-to-many relationships between entities. In these
relationships, the "many" or child documents are viewed in the context of the "one" or parent documents. See `data-modeling-example-one-to-many`.

### Collections with a Large Number of Small Documents

If you have a collection with a large number of small documents, consider embedding to improve performance. If you can group these small documents by some logical relationship and you frequently retrieve the documents by this grouping, you might consider "rolling-up" the small documents into larger documents that contain an array of embedded documents.

"Rolling up" these small documents into logical groupings means that queries to retrieve a group of documents involve sequential reads and fewer random disk accesses. Additionally, "rolling up" documents and moving common fields to the larger document benefit the index on these fields. There would be fewer copies of the common fields and there would be fewer associated key entries in the corresponding index. See `indexes` for more information on indexes.

However, if you often only need to retrieve a subset of the documents within the group, then "rolling-up" the documents may not provide better performance. Furthermore, if small, separate documents represent the natural model for the data, you should maintain that model.

## Query Embedded Data

To query data within embedded documents, use `dot notation`. For examples of querying data in arrays and embedded documents, see:

- `read-operations-arrays`
- `read-operations-embedded-documents`
