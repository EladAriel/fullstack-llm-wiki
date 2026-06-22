---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/scala-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/) methods:

- :scala-api:`collection.deleteMany()
<deleteMany(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>`

- :scala-api:`collection.deleteOne()
<deleteOne(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>`

.. include:: /includes/driver-examples/examples-intro.rst

## Delete All Documents

To delete all documents from a collection, pass an empty `filter<document-query-filter>` `Document()` to the :scala-api:`collection.deleteMany() <deleteMany(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>` method.

.. include:: /includes/fact-delete-all-inventory.rst

Upon successful execution, the :scala-api:`collection.deleteMany() <deleteMany(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>` method returns an [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/) with a single element with a `DeleteResult` type parameter or with an `com.mongodb.MongoException`.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use the `com.mongodb.client.model.Filters.eq_` method to create the `query filter document <document-query-filter>`:

```scala
and(equal(<field1>, <value1>), equal(<field2>, <value2>) ...)
```

In addition to the equality condition, MongoDB provides various `query operators <query-selectors>` to specify filter conditions. Use the `com.mongodb.client.model.Filters_` helper methods to facilitate the creation of filter documents. For example:

```scala
and(gte(<field1>, <value1>), lt(<field2>, <value2>), equal(<field3>, <value3>))
```

To delete all documents that match a deletion criteria, pass a `filter <document-query-filter>` parameter to the :scala-api:`deleteMany() <deleteMany(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>` method.

.. include:: /includes/fact-remove-condition-inv-example.rst

Upon successful execution, the :scala-api:`collection.deleteMany() <deleteMany(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>` method returns an [Observable](http://mongodb.github.io/mongo-scala-driver/2.1/reference/observables/) with a single element with a `DeleteResult` type parameter or with an `com.mongodb.MongoException`.

## Delete Only One Document that Matches a Condition

To delete at most a single document that matches a specified filter (even though multiple documents may match the specified filter) use the :scala-api:`collection.deleteOne() <deleteOne(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>` method.

.. include:: /includes/fact-remove-one-condition-inv-example.rst

> **Seealso:** - :scala-api:`collection.deleteMany()
  <deleteMany(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>`
- :scala-api:`collection.deleteOne()
  <deleteOne(filter:org.mongodb.scala.bson.conversions.Bson,options:org.mongodb.scala.model.DeleteOptions):org.mongodb.scala.SingleObservable[org.mongodb.scala.result.DeleteResult]>`
- `additional-deletes`
