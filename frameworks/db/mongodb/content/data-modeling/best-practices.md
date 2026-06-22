---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/best-practices.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# Best Practices for Data Modeling in MongoDB

MongoDB's flexible data model allows you to strategically balance performance and adaptability while ensuring data consistency and integrity. In addition to the general guidance on `planning your schema <data-modeling-schema-design>`, consider the following best practices to optimize your data model and determine which `schema design pattern <schema-design-patterns>` may be best suited for your application use case.

## Plan Your Schema Early and Iterate

.. include:: /includes/fact-plan-schema-early.rst

### Modify Your Data Model

Consider the following example:

You're tasked with building the backend of an online user learning platform that stores information on courses and their lessons. Initially, the platform only needs to store the following basic information for each course:

- Course title
- Instructor
- Description
- Lessons, embedded as an array of sub-documents inside each course document.
At this time, each lesson sub-document only contains a title, description, and presentation slides.

As the platform evolves, each course needs additional learning and testing formats, such as videos, quizzes, assignments, and external resource links. Embedding all of this new data in each course document would make the data model too complex.

Instead, consider creating a separate `lessons` collection. This way, you can link the `course` and `lessons` collections by using `reference <data-modeling-referencing>` IDs. By using references, each lesson can include different content types and be more flexible for future format changes.

## Link Related Data

When you design your data model in MongoDB, consider the structure of your documents and the ways your application uses data from related entities.

To link related data, you can either:

- Embed related data within a single document.
- Reference related data stored in a separate collection.
For examples of when to use embedding or referencing, refer to the following table:

.. include:: /includes/data-modeling/table-data-linking.rst

To learn more about use cases, performance considerations, and benefits for each data-linking method, see:

- `data-modeling-embedding`
- `data-modeling-referencing`
## Duplicate Data

.. include:: /includes/data-modeling/data-duplication-overview.rst

.. include:: /includes/data-modeling/duplicate-data-considerations.rst

The following table lists the different types of duplicate data that might exist in your schema:

If you don't need to update the duplicated data often, minimal additional work would be required to keep the two collections consistent. However, if the duplicated data is updated often, using a `reference <data-modeling-referencing>` to link related data may be a better approach.

For examples on how duplicating related data can help optimize your data model, see `data-modeling-duplicate-data`.

### Enforce Data Consistency

If you duplicate data in your schema, you need to decide how to keep your data consistent across multiple collections. For example, an e-commerce platform likely requires continuously up-to-date data to provide the real-time status of its product stock. On the other hand, applications that handle data for longer-term strategic decisions, such as social media analytics, can tolerate reading slightly stale data.

You can enforce data consistency in your application with any of the following methods:

- `Embedding related data <enforce-consistency-embedding>`
- `Transactions <enforce-consistency-embedding>`
- `Atlas Database Triggers <atlas-database-trigger>`
To learn more about each data consistency enforcement method, their use cases, and their performance tradeoffs, see `data-modeling-data-consistency`.

## Enforce Schema with Validation Rules

.. include:: /includes/data-modeling/schema-validation-use-case.rst

To learn more, see `schema-validation-overview`.

## Index Commonly Queried Fields

When designing your data model, think about how you access and store your data. If you frequently query, filter, sort, or join specific fields, consider creating `indexes <indexes>` on those fields. With indexes, MongoDB can:

- Return query results faster
- Sort results more efficiently
- Optimize `$lookup` and `$group` operations
- Reduce CPU and I/O usage
As your application grows, `monitor your deployment's index use <indexes-measuring-use>` to ensure that your indexes still support relevant queries.

When you create indexes, consider the following index behaviors:

- Each index requires at least 8 kB of data space.
- Adding an index has some negative performance impact for write
operations. For collections with high write-to-read ratio, indexes are expensive since each insert must also update any indexes.

- Collections with high read-to-write ratio often benefit from
additional indexes. Indexes do not affect un-indexed read operations.

- When active, each index consumes disk space and memory. This usage
can be significant and should be tracked for capacity planning, especially for concerns over working set size.

For more information on indexes, see `indexing-strategies`.

## Additional Considerations

When developing a data model, analyze all of your application's `read and write operations <crud>` in conjunction with the following considerations.

### Atomicity

In MongoDB, a write operation is `atomic <atomic operation>` on the level of a single document. This means that even if an update operation affects several sub-documents, either all of those sub-documents are updated, or the operation fails entirely and no updates occur.

A denormalized data model that uses embedded documents and arrays combines all related data in a single document instead of normalizing across multiple documents and collections. This data model allows atomic operations, in contrast to a normalized model where operations affect multiple documents and collections. For an example data model that provides atomic updates for a single document, see `data-modeling-atomic-operation`.

For data models that store references between related pieces of data, the application must issue separate read and write operations to retrieve and modify these related pieces of data.

.. include:: /includes/extracts/transactions-intro.rst

### Data Lifecycle Management

Data lifecycle management refers to the process of managing data from creation and storage to archiving and deletion. To ensure schema cost-efficiency, performance, and security, consider data life cycle management when making data modeling decisions.

If your application requires some data to persist in the database for a limited period of time, consider using the `Time to Live or TTL feature <ttl-collections>`. For example, TTL collections could be useful for managing user login sessions on a web application, where sessions are set to automatically expire after 30 minutes of inactivity. This means that MongoDB automatically deletes the session documents after the specified time period.

Additionally, if your application only uses recently inserted documents, consider `manual-capped-collection`. Capped collections provide first-in-first-out (FIFO) management of inserted documents and efficiently support operations that insert and read documents based on insertion order.

### Hardware Constraints

When you design your schema, consider your deployment's hardware, especially the amount of available RAM. Larger documents use more RAM, which may cause your application to read from disk and degrade performance. When possible, design your schema so only relevant fields are returned by queries, ensuring that your application's `working set` does not grow unnecessarily large.

### Small Documents

Each MongoDB document contains a certain amount of overhead. This overhead is normally insignificant but becomes significant if all documents are just a few bytes, as might be the case if the documents in your collection only have one or two fields.

Consider the following suggestions and strategies for optimizing storage utilization for these collections:

- Use the `_id` field explicitly.
MongoDB clients automatically add an `_id` field to each document and generate a unique 12-byte `ObjectId for the id field. Furthermore, MongoDB always indexes the id` field. For smaller documents, this may use a significant amount of space.

To optimize storage use, you can explicitly specify a value for the `_id field when inserting documents into the collection. This allows applications to store a value in the id field that would have occupied space in another portion of the document. This value must be unique, as the id` field uniquely identifies documents in a collection.

- Use shorter field names.
> **Note:**   While shortening field names can reduce BSON size in MongoDB, it's often
  more effective to modify the overall document model to reduce BSON size.
  Shortening field names might reduce expressiveness, and does not affect the
  size of indexes, as indexes have a predefined structure that does not
  incorporate field names.
MongoDB stores all field names in every document. For most
documents, this represents a small fraction of the space used by a
document; however, for small documents the field names may represent
a proportionally large amount of space. Consider a collection of
small documents that resemble the following:
.. code-block:: javascript
  { last_name : "Smith", best_score: 3.9 }
If you shorten the field named `last_name` to `lname` and the
field named `best_score` to `score`, as follows, you could save 9
bytes per document.
.. code-block:: javascript
  { lname : "Smith", score : 3.9 }

- Embed documents.
In some cases you may want to embed documents in other documents and save on the per-document overhead. See `faq-developers-embed-documents`.

## Learn More

To learn more about how to structure your documents and define your schema, see MongoDB University's [Data Modeling](https://learn.mongodb.com/learning-paths/data-modeling-for-mongodb)_ course.

## Contents

- Embedded Data </data-modeling/embedding>
- Reference Data </data-modeling/referencing>
- Duplicate Data </data-modeling/handle-duplicate-data>
- Data Consistency </data-modeling/data-consistency>
- Schema Validation </core/schema-validation>
