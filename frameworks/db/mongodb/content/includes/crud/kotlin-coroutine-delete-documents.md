---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/kotlin-coroutine-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following :driver:`Kotlin Coroutine Driver </kotlin/coroutine/current/>` methods:

- `MongoCollection.deleteOne()
<{+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-one.html>`__

- `MongoCollection.deleteMany()
<{+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html>`__

.. include:: /includes/driver-examples/examples-intro.rst

## Delete All Documents

To delete all documents from a collection, pass an empty `Bson` object as the `filter <document-query-filter>` to the [MongoCollection.deleteMany()]({+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html)_ method.

.. include:: /includes/fact-delete-all-inventory.rst

The [MongoCollection.deleteMany()]({+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html)_ method returns an instance of [com.mongodb.client.result.DeleteResult]({+java-api-docs+}/driver-core/com/mongodb/client/result/DeleteResult.html)_ that describes the status of the operation and count of deleted documents.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use the [Filters.eq()]({+java-api-docs+}/driver-core/com/mongodb/client/model/Filters.html#eq(java.lang.String,TItem))_ method to create the `query filter document <document-query-filter>`:

```kotlin
and(eq(<field1>, <value1>), eq(<field2>, <value2>) ...)
```

In addition to the equality condition, MongoDB provides various `query operators <query-selectors>` to specify filter conditions. Use the [com.mongodb.client.model.Filters]({+java-api-docs+}/driver-core/com/mongodb/client/model/Filters.html)_ helper methods to facilitate the creation of filter documents. For example:

```kotlin
and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
```

To delete all documents that match a deletion criteria, pass a `filter <document-query-filter>` parameter to the [MongoCollection.deleteMany()]({+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html)_ method.

.. include:: /includes/fact-remove-condition-inv-example.rst

The [MongoCollection.deleteMany()]({+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html)_ method returns an instance of [com.mongodb.client.result.DeleteResult]({+java-api-docs+}/driver-core/com/mongodb/client/result/DeleteResult.html)_ that describes the status of the operation and count of deleted documents.

## Delete Only One Document that Matches a Condition

To delete at most a single document that matches a specified filter, even if multiple documents match the specified filter, use the [MongoCollection.deleteOne()]({+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-one.html)_ method.

.. include:: /includes/fact-remove-one-condition-inv-example.rst

> **Seealso:** - `MongoCollection.deleteOne()
  <{+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-one.html>`__
- `MongoCollection.deleteMany()
  <{+java-api-docs+}/driver-kotlin-coroutine/mongodb-driver-kotlin-coroutine/com.mongodb.kotlin.client.coroutine/-mongo-collection/delete-many.html>`__
- :driver:`Kotlin Coroutine Driver Delete Documents Guide
  </kotlin/coroutine/current/fundamentals/crud/write-operations/delete/>`
