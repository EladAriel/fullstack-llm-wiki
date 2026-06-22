---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# db.getCollection() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

The :method:`db.getCollection()` object can access any `collection methods <collection-method>`.

The collection specified may or may not exist on the server.  If the collection does not exist, MongoDB creates it implicitly as part of `write operations <crud>` like :method:`db.collection.insertOne()`.

## Example

The following example uses :method:`db.getCollection()` to access the `auth` collection and insert a document into it.

```javascript
var authColl = db.getCollection("auth")

authColl.insertOne(
   {
       usrName : "John Doe",
       usrDept : "Sales",
       usrTitle : "Executive Account Manager",
       authLevel : 4,
       authDept : [ "Sales", "Customers"]
   }
)
```

This returns:

```javascript
{
   "acknowledged" : true,
   "insertedId" : ObjectId("569525e144fe66d60b772763")
}
```

The previous example requires the use of :method:`db.getCollection("auth")<db.getCollection()>` because of a name conflict with the database method :method:`db.auth()`.  Calling `db.auth` directly to perform an insert operation would reference the :method:`db.auth()` method and would error.

The following example attempts the same operation, but without using the :method:`db.getCollection()` method:

```javascript
db.auth.insertOne(
   {
       usrName : "John Doe",
       usrDept : "Sales",
       usrTitle : "Executive Account Manager",
       authLevel : 4,
       authDept : [ "Sales", "Customers"]
   }
)
```

The operation errors as `db.auth()` method has no `insertOne` method.

> **Seealso:** `collection-method`
