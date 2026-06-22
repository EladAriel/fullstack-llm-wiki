---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-wildcard/create-wildcard-index-single-field.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# Create a Wildcard Index on a Single Field

Wildcard indexes on a single field support queries on any subfield of the indexed field. Use wildcard indexes to support queries on field names that you don't know in advance or vary between documents.

To create a wildcard index on a single field, use the :method:`db.collection.createIndex()` method and include the wildcard specifier (`$**`) in the index key:

```javascript
db.collection.createIndex( { "<field>.$**": <sortOrder> } )
```

## About this Task

.. include:: /includes/indexes/wildcard-use-case-warning.rst

## Before You Begin

Create a `products` collection that contains the following documents:

```javascript
db.products.insertMany( [
   {
      "product_name" : "Spy Coat",
      "attributes" : {
         "material" : [ "Tweed", "Wool", "Leather" ],
         "size" : {
            "length" : 72,
            "units" : "inches"
         }
      }
   },
   {
      "product_name" : "Spy Pen",
      "attributes" : {
         "colors" : [ "Blue", "Black" ],
         "secret_feature" : {
            "name" : "laser",
            "power" : "1000",
            "units" : "watts",
         }
      }
   }
] )
```

## Procedure

The following operation creates a wildcard index on the `attributes` field:

```javascript
db.products.createIndex( { "attributes.$**" : 1 } )
```

## Results

The wildcard index supports single-field queries on `attributes` or its embedded fields. For example, the index supports the following queries:

- Query:
```javascript
  db.products.find( { "attributes.size.length" : { $gt : 60 } } )

Output:

.. code-block:: javascript
  :copyable: false

  [
    {
      _id: ObjectId("63472196b1fac2ee2e957ef6"),
      product_name: 'Spy Coat',
      attributes: {
        material: [ 'Tweed', 'Wool', 'Leather' ],
        size: { length: 72, units: 'inches' }
      }
    }
  ]
```

- Query:
```javascript
  db.products.find( { "attributes.material" : "Leather" } )

Output:

.. code-block:: javascript
  :copyable: false

  [
    {
      _id: ObjectId("63472196b1fac2ee2e957ef6"),
      product_name: 'Spy Coat',
      attributes: {
        material: [ 'Tweed', 'Wool', 'Leather' ],
        size: { length: 72, units: 'inches' }
      }
    }
  ]
```

- Query:
```javascript
  db.products.find(
     { "attributes.secret_feature.name" : "laser" },
     { "_id": 0, "product_name": 1, "attributes.colors": 1 }
  )

Output:

.. code-block:: javascript
  :copyable: false

  [
    {
      product_name: 'Spy Pen',
      attributes: { colors: [ 'Blue', 'Black' ] }
    }
  ]
```

Wildcard indexes have specific behavior when the indexed field contains an embedded object (for example, `attributes.secret_feature`). For more information, see `wildcard-index-embedded-object-behavior`.

## Learn More

To learn more about behaviors and use cases for wildcard indexes, see:

- `create-wildcard-index-all-fields`
- `create-wildcard-index-multiple-fields`
- `wildcard-index-compound`
- `wildcard-index-restrictions`
