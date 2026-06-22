---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/scala-project-fields.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page provides examples of |query_operations| using the :scala-api:`collection.find()<find[C](filter:org.mongodb.scala.bson.conversions.Bson)(implicite:org.mongodb.scala.bson.DefaultHelper.DefaultsTo[C,TResult],implicitct:scala.reflect.ClassTag[C]):org.mongodb.scala.FindObservable[C]>` method in the [MongoDB Scala Driver](http://mongodb.github.io/mongo-scala-driver/).

.. include:: /includes/driver-examples/examples-intro.rst

## Return All Fields in Matching Documents

If you do not specify a `projection` document, the :method:`db.collection.find()` method returns all fields in the matching documents.

The following example returns all fields from all documents in the `inventory` collection where the `status` equals `"A"`:

The operation corresponds to the following SQL statement:

```sql
SELECT * from inventory WHERE status = "A"
```

## Return the Specified Fields and the `_id` Field Only

A projection can explicitly include several fields by setting the `<field>` to `1` in the projection document. The following operation returns all documents that match the query. In the result set, only the `item`, `status and, by default, the id` fields return in the matching documents.

The operation corresponds to the following SQL statement:

```sql
SELECT _id, item, status from inventory WHERE status = "A"
```

## Suppress `_id` Field

You can remove the `_id` field from the results by setting it to `0` in the projection, as in the following example:

The operation corresponds to the following SQL statement:

```sql
SELECT item, status from inventory WHERE status = "A"
```

> **Note:** With the exception of the `_id` field, you cannot combine inclusion
and exclusion statements in projection documents.

## Return All But the Excluded Fields

Instead of listing the fields to return in the matching document, you can use a projection to exclude specific fields. The following example which returns all fields except for the `status` and the `instock` fields in the matching documents:

> **Note:** With the exception of the `_id` field, you cannot combine inclusion
and exclusion statements in projection documents.

## Return Specific Fields in Embedded Documents

You can return specific fields in an embedded document. Use the `dot notation <document-dot-notation>` to refer to the embedded field and set to `1` in the projection document.

The following example returns:

- The `_id` field (returned by default),
- The `item` field,
- The `status` field,
- The `uom` field in the `size` document.
The `uom` field remains embedded in the `size` document.

You can also specify embedded fields using the nested form. For example, `{ item: 1, status: 1, size: { uom: 1 } }`.

## Suppress Specific Fields in Embedded Documents

You can suppress specific fields in an embedded document. Use the `dot notation <document-dot-notation>` to refer to the embedded field in the projection document and set to `0`.

The following example specifies a projection to exclude the `uom` field inside the `size` document. All other fields are returned in the matching documents:

You can also specify embedded fields using the nested form. For example, `{ size: { uom: 0 } }`.

## Projection on Embedded Documents in an Array

Use `dot notation <document-dot-notation>` to project specific fields inside documents embedded in an array.

The following example specifies a projection to return:

- The `_id` field (returned by default),
- The `item` field,
- The `status` field,
- The `qty` field in the documents embedded in the `instock` array.
## Project Specific Array Elements in the Returned Array

.. include:: /includes/fact-projection-ops.rst

.. include:: /includes/fact-projection-slice-example.rst

:projection:`$elemMatch`, :projection:`$slice`, and :projection:`$` are the only operators that you can use to project specific elements to include in the returned array. For instance, you cannot project specific array elements using the array index; e.g. `include("instock.0")` projection does not project the array with the first element.

## Project Fields with Aggregation Expressions

You can specify `aggregation expressions <aggregation-expressions>` in a query projection. Aggregation expressions let you project new fields and modify the values of existing fields.

For example, the following operation uses aggregation expressions to override the value of the `status` field, and project new fields `area` and `reportNumber`.

> **Note:** The following example uses MongoDB Shell syntax. For driver examples
of projection with aggregation, see your :driver:`driver
documentation </>`.
