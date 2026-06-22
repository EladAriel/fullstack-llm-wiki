---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/java-async-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following [Java Reactive Streams Driver](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/) methods:

- `com.mongodb.reactivestreams.client.MongoCollection.deleteMany
<http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson)>`_

- `com.mongodb.reactivestreams.client.MongoCollection.deleteOne
<http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteOne(org.bson.conversions.Bson)>`_

.. include:: /includes/driver-examples/examples-intro.rst

## Delete All Documents

To delete all documents from a collection, pass an empty org.bson.Document_ object as the `filter<document-query-filter>` to the [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson)) method.

.. include:: /includes/fact-delete-all-inventory.rst

[com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson)) returns a [Publisher](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher.html) object of type com.mongodb.client.result.DeleteResult_ if successful. Returns an instance of `com.mongodb.MongoException` if unsuccessful.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use the com.mongodb.client.model.Filters.eq_ method to create the `query filter document <document-query-filter>`:

```java
and(eq(<field1>, <value1>), eq(<field2>, <value2>) ...)
```

In addition to the equality condition, MongoDB provides various `query operators <query-selectors>` to specify filter conditions. Use the com.mongodb.client.model.Filters_ helper methods to facilitate the creation of filter documents. For example:

```java
and(gte(<field1>, <value1>), lt(<field2>, <value2>), eq(<field3>, <value3>))
```

To delete all documents that match a deletion criteria, pass a `filter <document-query-filter>` parameter to the [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson)) method.

.. include:: /includes/fact-remove-condition-inv-example.rst

[com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson)) returns a [Publisher](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher.html) object of type com.mongodb.client.result.DeleteResult_ if successful. Returns an instance of `com.mongodb.MongoException` if unsuccessful.

## Delete Only One Document that Matches a Condition

To delete at most a single document that matches a specified filter (even though multiple documents may match the specified filter) use the [com.mongodb.reactivestreams.client.MongoCollection.deleteMany](http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson)) method.

.. include:: /includes/fact-remove-one-condition-inv-example.rst

> **Seealso:** - `com.mongodb.reactivestreams.client.MongoCollection.deleteMany
  <http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteMany(org.bson.conversions.Bson)>`_
- `com.mongodb.reactivestreams.client.MongoCollection.deleteOne
  <http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/javadoc/com/mongodb/reactivestreams/client/MongoCollection.html#deleteOne(org.bson.conversions.Bson)>`_
- `Java Reactive Streams Driver Quick Tour
  <http://mongodb.github.io/mongo-java-driver-reactivestreams/1.6/getting-started/quick-tour/>`_
