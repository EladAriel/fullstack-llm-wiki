---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.hideIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# db.collection.hideIndex() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method-alt

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
db.collection.hideIndex(<index>)
```

### Parameters

The :method:`db.collection.hideIndex()` method takes the following parameter:

The :method:`db.collection.hideIndex()` is a :binary:`mongosh` shell wrapper for the :dbcommand:`collMod` command.

## Behavior

### Feature Compatibility Version

To hide an index, you must have `featureCompatibilityVersion <view-fcv>` set to `{+minimum-lts-version+}` or greater.

### Restrictions

You cannot hide the `_id` index.

### Index Modifications Reset Statistics

Hiding an unhidden index resets its :pipeline:`$indexStats`.

### No-op

Hiding an already hidden index has no effect on the index. However, the operation will still generate an empty oplog entry.

## Access Control

If the deployment enforces authentication/authorization, you must have the :authaction:`collMod` privilege in the collection's database.

The built-in role :authrole:`dbAdmin` provides the required privileges.

## Example

The following example hides an existing index.

First, use :method:`db.collection.createIndex()` to create an index without hiding:

```javascript
db.restaurants.createIndex( { borough: 1, ratings: 1 } );
```

To hide the index, you can specify either the index key specification document or the index name to the :method:`db.collection.hideIndex()` method. The following specifies the index name:

```javascript
db.restaurants.hideIndex( "borough_1_ratings_1" ); 
```

To verify, run :method:`db.collection.getIndexes()` on the `restaurants` collection:

```javascript
db.restaurants.getIndexes();
```

The operation returns the following information:

```javascript
[
   {
      "v" : 2,
      "key" : {
         "_id" : 1
      },
      "name" : "_id_"
   },
   {
      "v" : 2,
      "key" : {
         "borough" : 1,
         "ratings" : 1
      },
      "name" : "borough_1_ratings_1",
      "hidden" : true
   }
]
```

The `hidden` index option is only returned if the value is `true`.

> **Seealso:** - :method:`db.collection.unhideIndex()`
- `db.collection.createIndex() <method-createIndex-hidden>`
