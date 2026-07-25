---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.collation.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================

# cursor.collation() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Examples

Consider a collection `foo` with the following documents:

```javascript
{ "_id" : 1, "x" : "a" }
{ "_id" : 2, "x" : "A" }
{ "_id" : 3, "x" : "á" }
```

The following operation specifies a query filter of `x: "a"`. The operation also includes a collation option with `locale: "en_US"` (US English locale) and `strength: 1` (compare base characters only; i.e. ignore case and diacritics):

```javascript
db.foo.find( { x: "a" } ).collation( { locale: "en_US", strength: 1 } )
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "x" : "a" }
{ "_id" : 2, "x" : "A" }
{ "_id" : 3, "x" : "á" }
```

If you do not specify the collation, i.e. `db.collection.find( { x: "a" } )`, the query would only match the following document:

```javascript
db.foo.find( { x: "a" } )
```

You can chain other cursor methods, such as :method:`cursor.sort()` and :method:`cursor.count()`, to :method:`cursor.collation()`:

```javascript
db.collection.find({...}).collation({...}).sort({...});
db.collection.find({...}).collation({...}).count();
```

> **Note:** .. include:: /includes/extracts/collation-single-per-operation.rst
