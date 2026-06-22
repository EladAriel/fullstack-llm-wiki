---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/go-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following :driver:`MongoDB Go Driver </go/>` functions:

- :go-api:`Collection.DeleteMany<mongo#Collection.DeleteMany>`
- :go-api:`Collection.DeleteOne<mongo#Collection.DeleteOne>`
.. include:: /includes/driver-examples/examples-intro.rst

## Delete All Documents

To delete all documents from a collection, pass an empty `filter<document-query-filter>` document to the :go-api:`Collection.DeleteMany<mongo#Collection.DeleteMany>` function.

.. include:: /includes/fact-delete-all-inventory.rst

Upon successful execution, the :go-api:`Collection.DeleteMany <mongo#Collection.DeleteMany>` function returns an instance of :go-api:`DeleteResult <mongo#DeleteResult>` whose `DeletedCount` property contains the number of documents that matched the filter.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use the `bson.D` type to create a filter document:

```go
filter := bson.D{{"<field>", <value>}}
```

In addition to the equality filter, MongoDB provides various `query operators <query-selectors>` to specify filter conditions. Use the bson package to create query operators for filter documents. For example:

```go
filter := bson.D{
    {"$and", bson.A{
        bson.D{{"field1", bson.D{{"$eq", value1}}}},
        bson.D{{"field2", bson.D{{"$lt", value2}}}},
    }},
}
```

To delete all documents that match a deletion criteria, pass a `filter <document-query-filter>` parameter to the :go-api:`Collection.DeleteMany<mongo#Collection.DeleteMany>` function.

.. include:: /includes/fact-remove-condition-inv-example.rst

Upon successful execution, the :go-api:`Collection.DeleteMany <mongo#Collection.DeleteMany>` function returns an instance of :go-api:`DeleteResult <mongo#DeleteResult>` whose `DeletedCount` property contains the number of documents that matched the filter.

## Delete Only One Document that Matches a Condition

To delete at most a single document that matches a specified filter (even though multiple documents may match the specified filter) use the :go-api:`Collection.DeleteOne<mongo#Collection.DeleteOne>` function.

.. include:: /includes/fact-remove-one-condition-inv-example.rst

> **Seealso:** - :go-api:`Collection.DeleteMany<mongo#Collection.DeleteMany>`
- :go-api:`Collection.DeleteOne<mongo#Collection.DeleteOne>`
- `additional-deletes`
