---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/wildcard-query-restrictions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Field does **not** exist Wildcard indexes cannot support document queries when an indexed field does **not** exist.

For example, consider a collection `inventory` with a wildcard index on `product_attributes`. The wildcard index **cannot** support the following queries:

```javascript
  db.inventory.find( {"product_attributes" : { $exists : false } } )

  db.inventory.aggregate([
    { $match : { "product_attributes" : { $exists : false } } }
  ])
```

Field is equal to a document or an array Wildcard indexes generate entries for the **contents** of a document or array, and not the document or array itself. Therefore, wildcard indexes don't support exact document or array equality matches. Wildcard indexes can support querying where the field equals an empty document `{}`.

For example, consider a collection `inventory` with a wildcard index on `product_attributes`. The wildcard index **cannot** support the following queries:

```javascript
  db.inventory.find({ "product_attributes" : { "price" : 29.99 } } )
  db.inventory.find({ "product_attributes.tags" : [ "waterproof", "fireproof" ] } )

  db.inventory.aggregate([{ 
    $match : { "product_attributes" : { "price" : 29.99 } }
  }])

  db.inventory.aggregate([{ 
    $match : { "product_attributes.tags" : ["waterproof", "fireproof" ] } }
  }])
```

Field is not equal to a document or array Wildcard indexes generate entries for the **contents** of a document or array, and not the document/array itself. Therefore, wildcard indexes don't support exact document or array inequality matches.

For example, consider a collection `inventory` with a wildcard index on `product_attributes`. The wildcard index **cannot** support the following queries:

```javascript
  db.inventory.find( { $ne : [ "product_attributes", { "price" : 29.99 } ] } )
  db.inventory.find( { $ne : [ "product_attributes.tags",  [ "waterproof", "fireproof" ] ] } )

  db.inventory.aggregate([{ 
    $match : { $ne : [ "product_attributes", { "price" : 29.99 } ] }
  }])

  db.inventory.aggregate([{ 
    $match : { $ne : [ "product_attributes.tags", [ "waterproof", "fireproof" ] ] }
  }])
```

Array Field is equal or not equal to null If a given field is an array in any document in the collection, wildcard indexes cannot support queries for documents where that field is equal or not equal to null.

For example, consider a collection `inventory` with a wildcard index on `product_attributes`. The wildcard index **cannot** support the following queries if `product_attributes.tags` is an array in any document in the collection:

```javascript
  db.inventory.find( { "product_attributes.tags": { $ne: null } } )

  db.inventory.find( { "product_attributes.tags": null } )

  db.inventory.aggregate([{ 
    $match : { "product_attributes.tags": { $ne: null } }
  }])

  db.inventory.aggregate([{ 
    $match : { "product_attributes.tags": null }
  }])
```

Field is equal to null Wildcard indexes cannot support queries for documents where a field is equal to null.

The query `{ $eq: null }` matches all documents where the field is null or missing, but wildcard indexes don't index null or empty fields. that.

For example, consider a collection `inventory` with a wildcard index on `product_attributes`. The wildcard index **cannot** support the following queries:

```javascript
  db.inventory.find( { "product_attributes.price": { $eq: null } } )

  db.inventory.aggregate([{
     $match : { "product_attributes.price": { $eq: null } }
  }])
```
