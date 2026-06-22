---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/java-sync-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following Java Synchronous Driver methods:

- com.mongodb.client.MongoCollection.deleteMany_
- com.mongodb.client.MongoCollection.deleteOne_
.. include:: /includes/driver-examples/examples-intro.rst

## Delete All Documents

To delete all documents from a collection, pass an empty org.bson.Document_ object as the `filter<document-query-filter>` to the com.mongodb.client.MongoCollection.deleteMany_ method.

.. include:: /includes/fact-delete-all-inventory.rst

The com.mongodb.client.MongoCollection.deleteMany_ method returns an instance of com.mongodb.client.result.DeleteResult_ with the status of the operation.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use the `com.mongodb.client.model.Filters.eq_` method to create the `query filter document <document-query-filter>`:

```java
and(eq(<field1>, <value1>), eq(<field2>, <value2>) ...)
```

In addition to the equality condition, MongoDB provides various `query operators <query-selectors>` to specify filter conditions. Use the com.mongodb.client.model.Filters_ helper methods to facilitate the creation of filter documents. For example:

```java
and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
```

To delete all documents that match a deletion criteria, pass a `filter <document-query-filter>` parameter to the com.mongodb.client.MongoCollection.deleteMany_ method.

.. include:: /includes/fact-remove-condition-inv-example.rst

The com.mongodb.client.MongoCollection.deleteMany_ method returns an instance of com.mongodb.client.result.DeleteResult_ with the status of the operation.

## Delete Only One Document that Matches a Condition

To delete at most a single document that matches a specified filter (even though multiple documents may match the specified filter) use the com.mongodb.client.MongoCollection.deleteOne_ method.

.. include:: /includes/fact-remove-one-condition-inv-example.rst

> **Seealso:** - com.mongodb.client.MongoCollection.deleteMany_
- com.mongodb.client.MongoCollection.deleteOne_
- Additional Java Synchronous Driver Write Examples
