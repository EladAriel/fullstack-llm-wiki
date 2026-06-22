---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.createIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# db.collection.createIndexes() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-createIndexes.rst

## Definition

### Parameters

:method:`db.collection.createIndexes()` takes the following parameters:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

### Stable API

.. include:: /includes/create-indexes-stable-api-compatibility.rst

## Options

The `options` document contains a set of options that control the creation of the indexes. Different index types can have additional options specific for that type.

Multiple index options can be specified in the same document. However, if you specify multiple option documents the :method:`db.collection.createIndexes()` operation will fail.

Consider the following :method:`db.collection.createIndexes()` operation:

```javascript
db.collection.createIndexes(
   [
     {
       "a": 1
     },
     {
       "b": 1
     }
   ],
   {
     unique: true,
     sparse: true,
     expireAfterSeconds: 3600
   }
 )
```

If the options specification had been split into multiple documents like this: `{ unique: true }, { sparse: true, expireAfterSeconds: 3600 }` the index creation operation would have failed.

> **Important:** When you specify options to
:method:`db.collection.createIndexes()`, the options apply to
all of the specified indexes. For example, if you specify a
collation option, all of the created indexes will include that
collation.
:method:`db.collection.createIndexes()` will return an error if you
attempt to create indexes with incompatible options or too many
arguments. Refer to the option descriptions for more information.

### Options for All Index Types

The following options are available for all index types unless otherwise specified:

### Option for Collation

.. include:: /includes/extracts/collation-index-type-restrictions.rst

.. include:: /includes/extracts/collation-index-type-restrictions-addendum.rst

Collation and Index Use ```````````````````````

.. include:: /includes/extracts/collation-index.rst

### Options for `text` Indexes

The following options are available for `text <index-type-text>` indexes only:

### Options for `2dsphere` Indexes

The following option is available for `2dsphere <2dsphere-index>` indexes only:

### Options for `2d` Indexes

The following options are available for `2d` indexes only:

### Options for `wildcard` indexes

The following option is available for `wildcard <wildcard-index-core>` indexes only:

## Behaviors

### Recreating an Existing Index

If you call :method:`db.collection.createIndexes()` for an index or indexes that already exist, MongoDB does not recreate the existing index or indexes.

### Index Options

Non-Collation and Non-Hidden Options ````````````````````````````````````

With the exception of the `collation option <method-createIndexes-collation-option>`, if you create an index with one set of index options and then try to recreate the same index but with different index options, MongoDB will not change the options nor recreate the index.

The `hidden <createIndexes-hidden-option>` option can be changed without dropping and recreating the index. See `method-createIndexes-hidden-option`.

To change the other index options, drop the existing index with :method:`db.collection.dropIndex()` before running :method:`db.collection.createIndexes()` with the new options.

Collation Option ````````````````

.. include:: /includes/extracts/collation-index-options.rst

Hidden Option ``````````````

To hide or unhide existing indexes, you can use the following :binary:`~bin.mongosh` methods:

- :method:`db.collection.hideIndex()`
- :method:`db.collection.unhideIndex()`
For example,

- To change the `hidden` option for an index to `true`, use the
:method:`db.collection.hideIndex()` method:

```javascript
  db.restaurants.hideIndex( { borough: 1, ratings: 1 } );
```

- To change the `hidden` option for an index to `false`, use the
:method:`db.collection.unhideIndex()` method:

```javascript
  db.restaurants.unhideIndex( { borough: 1, city: 1 } );
```

> **Seealso:** `index-type-hidden`

### Wildcard Indexes

- .. include:: /includes/extracts/wildcard-index-id.rst
- .. include:: /includes/indexes/wildcard-restrictions.rst
To learn more, see:

- `Concepts <wildcard-index-core>`
- `Examples <createIndexes-command-wildcard-examples>`
- `Restrictions <wildcard-index-restrictions>`
### Transactions

.. include:: /includes/extracts/transactions-explicit-ddl.rst

### Index Builds

.. versionchanged:: 7.1

.. include:: /includes/index-build-improvements.rst

## Example

> **Seealso:** :method:`db.collection.createIndex()` for examples of various index
specifications.

### Create Indexes Without Options

Consider a `restaurants` collection containing documents that resemble the following:

```javascript
db.restaurants.insertOne ( 
   {
      location: {
         type: "Point",
         coordinates: [-73.856077, 40.848447]
      },
      name: "Morris Park Bake Shop",
      cuisine: "Cafe",
      borough: "Bronx",
   }
)
```

The following example creates two indexes on the `restaurants` collection: an ascending index on the `borough` field and a `2dsphere <2dsphere-index>` index on the `location` field.

```bash
db.restaurants.createIndexes([{"borough": 1}, {"location": "2dsphere"}])
```

### Create Indexes with Collation Specified

The following example creates two indexes on the `products` collection: an ascending index on the `manufacturer` field and an ascending index on the `category` field. Both indexes use a `collation <create-index-collation>` that specifies the locale `fr` and comparison strength `2`:

```javascript
db.products.createIndexes( [ { "manufacturer": 1}, { "category": 1 } ],
   { collation: { locale: "fr", strength: 2 } })
```

For queries or sort operations on the indexed keys that uses the same collation rules, MongoDB can use the index. For details, see `createIndex-collation-index-use`.

### Create a Wildcard Index

For complete documentation on Wildcard Indexes, see `wildcard-index-core`.

The following lists examples of wildcard index creation:

- `createIndexes-method-onepath`
- `createIndexes-method-allpaths`
- `createIndexes-method-inclusion`
- `createIndexes-method-exclusion`
Create a Wildcard Index on a Single Field Path ``````````````````````````````````````````````

The following operation creates a wildcard index on the `product_attributes` field:

```bash
use inventory
db.products_catalog.createIndexes( 
  [ { "product_attributes.$**" : 1 } ] 
)
```

With this wildcard index, MongoDB indexes all scalar values of `product_attributes`. If the field is a nested document or array, the wildcard index recurses into the document/array and indexes all scalar fields in the document/array.

The wildcard index can support arbitrary single-field queries on `product_attributes` or one of its nested fields:

> **Note:** The path-specific wildcard index syntax is incompatible with the
`wildcardProjection` option. See the |projection-ref| for more
information.

Create a Wildcard Index on All Field Paths ``````````````````````````````````````````

The following operation creates a wildcard index on all scalar fields (excluding the `_id` field):

```bash
use inventory
db.products_catalog.createIndexes( [ { "$**" : 1 } ] )
```

With this wildcard index, MongoDB indexes all scalar fields for each document in the collection. If a given field is a nested document or array, the wildcard index recurses into the document/array and indexes all scalar fields in the document/array.

The created index can support queries on any arbitrary field within documents in the collection:

```bash
db.products_catalog.find( { "product_price" : { $lt : 25 } } )
db.products_catalog.find( { "product_attributes.colors" : { $eq: "blue" } } )
```

> **Note:** Wildcard indexes omit the `_id` field by default. To include the
`_id` field in the wildcard index, you must explicitly include it
in the `wildcardProjection` document. See |projection-ref| for
more information.

Create a Wildcard Index on Multiple Specific Field Paths ````````````````````````````````````````````````````````

The following operation creates a wildcard index and uses the `wildcardProjection` option to include only scalar values of the `product_attributes.colors` and `product_attributes.material` fields in the index.

```bash
use inventory
db.products_catalog.createIndexes(
  [ { "$**" : 1 } ],
  {
    "wildcardProjection" : {
      "product_attributes.colors" : 1,
      "product_attributes.material" : 1
    }
  }
)
```

The pattern `"$**"` includes all fields in the document. Use the `wildcardProjection` field to limit the index to the specified fields.

For complete documentation on `wildcardProjection`, see `createIndex-method-wildcard-option`.

If a field is a nested document or array, the wildcard index recurses into the document/array and indexes all scalar fields in the document/array.

The wildcard index supports queries on any scalar field included in the `wildcardProjection`:

> **Note:** .. include:: /includes/extracts/wildcard-index-inclusion-exclusion.rst

Omit Specific Fields from Wildcard Index Coverage `````````````````````````````````````````````````

This example uses a wildcard index and a `wildcardProjection` document to index the scalar fields for each document in the collection. The wildcard index excludes the `product_attributes.colors` and `product_attributes.material` fields:

```bash
use inventory
db.products_catalog.createIndexes(
  [ { "$**" : 1 } ],
  {
    "wildcardProjection" : {
      "product_attributes.colors" : 0,
      "product_attributes.material" : 0
    }
  }
)
```

The wildcard pattern `"$**"` includes all of the fields in the document. However, the `wildcardProjection` field excludes the specified fields from the index.

For complete documentation on `wildcardProjection`, see `createIndex-method-wildcard-option`.

If a field is a nested document or array, the wildcard index recurses into the document/array and indexes all scalar fields in the document/array.

The index can support queries on any scalar field **except** fields that are excluded by `wildcardProjection`:

```bash
db.products_catalog.find( { "product_attributes.maxSize" : { $gt: 25 } } )
db.products_catalog.find( { "product_attributes.washable" : true } )
```

> **Note:** .. include:: /includes/extracts/wildcard-index-inclusion-exclusion.rst

### Create Indexes With Commit Quorum

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous-fcv.rst

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous.rst

.. include:: /includes/indexes/template-commit-quorum-intro.rst

The following operation creates an index with a `commit quorum <createIndexes-method-commitQuorum>` of `"majority"`:

```javascript
db.getSiblingDB("examples").invoices.createIndexes(
  { "invoices" : 1 },
  { },
  "majority"
)
```

The `primary` marks index build as ready only after a simple majority of data-bearing voting members "vote" to commit the index build. For more information on index builds and the voting process, see `index-operations-replicated-build`.

### Create Multiple Indexes

.. include:: /includes/cakeSales-example-collection.rst

The following example creates multiple indexes on the `cakeSales` collection:

```javascript
db.cakeSales.createIndexes( [
   { "type": 1 },
   { "orderDate": 1 },
   { "state": 1 },
   { "orderDate": 1, "state": -1 }
] )
```

The first three indexes are on single fields and in ascending order (`1`).

The last index is on `orderDate` in ascending order (`1`) and `state` in descending order (`-1`).

## Additional Information

For additional information about indexes, refer to:

- The `indexes` section of this manual for full
documentation of indexes and indexing in MongoDB.

- :method:`db.collection.getIndexes()` to view the specifications of
existing indexes for a collection.

- `index-feature-text` for details on creating `text`
indexes.

- `index-feature-geospatial` for geospatial queries.
- `index-feature-ttl` for expiration of data.
