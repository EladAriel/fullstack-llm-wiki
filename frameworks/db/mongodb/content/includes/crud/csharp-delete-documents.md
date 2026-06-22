---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/csharp-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following :driver:`MongoDB C# Driver </csharp/>` methods:

- :csharp-api:`IMongoCollection.DeleteMany()
<M_MongoDB_Driver_IMongoCollection_1_DeleteMany>`

- :csharp-api:`IMongoCollection.DeleteOne()
<M_MongoDB_Driver_IMongoCollection_1_DeleteOne>`

.. include:: /includes/driver-examples/examples-intro.rst

## Delete All Documents

To delete all documents from a collection, pass an empty `filter<document-query-filter>` `Builders<BsonDocument>.Filter.Empty` to the :csharp-api:`IMongoCollection.DeleteMany() <M_MongoDB_Driver_IMongoCollection_1_DeleteMany>` method.

.. include:: /includes/fact-delete-all-inventory.rst

Upon successful execution, the :csharp-api:`IMongoCollection.DeleteMany() <M_MongoDB_Driver_IMongoCollection_1_DeleteMany>` method returns an instance of :csharp-api:`DeleteResult <T_MongoDB_Driver_DeleteResult>` whose `DeletedCount` property contains the number of documents that matched the filter.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, construct a filter using the :csharp-api:`Eq <Overload_MongoDB_Driver_FilterDefinitionBuilder_1_Eq>` method:

```csharp
Builders<BsonDocument>.Filter.Eq(<field>, <value>);
```

In addition to the equality filter, MongoDB provides various `query operators <query-selectors>` to specify filter conditions. Use the :csharp-api:`FilterDefinitionBuilder <T_MongoDB_Driver_FilterDefinitionBuilder_1>` methods to create a filter document. For example:

```csharp
var builder = Builders<BsonDocument>.Filter;
builder.And(builder.Eq(<field1>, <value1>), builder.Lt(<field2>, <value2>));
```

To delete all documents that match a deletion criteria, pass a `filter <document-query-filter>` parameter to the :csharp-api:`IMongoCollection.DeleteMany() <M_MongoDB_Driver_IMongoCollection_1_DeleteMany>` method.

.. include:: /includes/fact-remove-condition-inv-example.rst

Upon successful execution, the :csharp-api:`IMongoCollection.DeleteMany() <M_MongoDB_Driver_IMongoCollection_1_DeleteMany>` method returns an instance of :csharp-api:`DeleteResult <T_MongoDB_Driver_DeleteResult>` whose `DeletedCount` property contains the number of documents that matched the filter.

## Delete Only One Document that Matches a Condition

To delete at most a single document that matches a specified filter (even though multiple documents may match the specified filter) use the :csharp-api:`IMongoCollection.DeleteOne() <M_MongoDB_Driver_IMongoCollection_1_DeleteOne>` method.

.. include:: /includes/fact-remove-one-condition-inv-example.rst

> **Seealso:** - :csharp-api:`IMongoCollection.DeleteMany()
  <M_MongoDB_Driver_IMongoCollection_1_DeleteMany>`
- :csharp-api:`IMongoCollection.DeleteOne()
  <M_MongoDB_Driver_IMongoCollection_1_DeleteOne>`
- `additional-deletes`
