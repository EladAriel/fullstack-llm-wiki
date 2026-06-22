---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/createIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# createIndexes (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :dbcommand:`createIndexes` command takes the following form:

```javascript
db.runCommand(
   {
     createIndexes: <collection>,
     indexes: [
         {
             key: {
                 <key-value_pair>,
                 <key-value_pair>,
                 ...
             },
             name: <index_name>,
             <option1>,
             <option2>,
             ...
         },
         { ... },
         { ... }
     ],
     writeConcern: { <write concern> },
     commitQuorum: <int|string>,
     comment: <any>
   }
 )
```

### Command Fields

The :dbcommand:`createIndexes` command takes the following fields:

Each document in the `indexes` array can take the following fields:

:binary:`~bin.mongosh` provides the methods :method:`db.collection.createIndex()` and :method:`db.collection.createIndexes()` as wrappers for the :dbcommand:`createIndexes` command.

## Considerations

MongoDB disallows the creation of version 0 indexes.

### Index Names

The :dbcommand:`createIndexes` command and :binary:`~bin.mongosh` helpers :method:`db.collection.createIndex()` and :method:`db.collection.createIndexes()` report an error if you create an index with one name, and then try to create the same index again but with another name.

```javascript
{
  "ok" : 0,
  "errmsg" : "Index with name: x_1 already exists with a different name",
  "code" : 85,
  "codeName" : "IndexOptionsConflict"
}
```

In previous versions, MongoDB did not create the index again, but would return a response object with `ok` value of `1` and a note that implied that the index was not recreated. For example:

```javascript
{
  "numIndexesBefore" : 2,
  "numIndexesAfter" : 2,
  "note" : "all indexes already exist",
  "ok" : 1
}
```

### Replica Sets and Sharded Clusters

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous-fcv.rst

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous.rst

To start an index build with a non-default commit quorum, specify the `commitQuorum <createIndexes-cmd-commitQuorum>`.

Use the :dbcommand:`setIndexCommitQuorum` command to modify the commit quorum of an in-progress index build.

### Collation and Index Types

.. include:: /includes/extracts/collation-index-type-restrictions.rst

.. include:: /includes/extracts/collation-index-type-restrictions-addendum.rst

### Stable API

.. include:: /includes/create-indexes-stable-api-compatibility.rst

## Behavior

### Concurrency

.. include:: /includes/extracts/createIndexes-resource-lock.rst

.. include:: /includes/unreachable-node-default-quorum-index-builds.rst

### Memory Usage Limit

.. include:: /includes/fact-index-build-default-memory-limit.rst

### Index Options

Non-Hidden Option `````````````````

The `hidden <createIndexes-hidden-option>` option can be changed without dropping and recreating the index. See `createIndexes-hidden-option`.

Changing Index Options ``````````````````````

Collation options on an existing index can be updated. To change other index options, drop the existing index with :method:`db.collection.dropIndex()` then run :dbcommand:`createIndexes` with the new options.

Collation Option ````````````````

.. include:: /includes/extracts/collation-index-options.rst

.. include:: /includes/extracts/collation-index-collection.rst

.. include:: /includes/extracts/collation-index-tip.rst

.. include:: /includes/extracts/collation-index-use.rst

Hidden Option ``````````````

To change the `hidden` option for existing indexes, you can use the following :binary:`~bin.mongosh` methods:

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

> **Seealso:** `/core/index-hidden`

### Wildcard Indexes

- .. include:: /includes/extracts/wildcard-index-id.rst
- .. include:: /includes/indexes/wildcard-restrictions.rst
To learn more, see:

- `About Wildcard Indexes <wildcard-index-core>`
- `Wildcard Index Examples <createIndexes-command-wildcard-examples>`
- `Wildcard Index Restrictions <wildcard-index-restrictions>`
### Transactions

.. include:: /includes/extracts/transactions-explicit-ddl.rst

### Commit Quorum Contrasted with Write Concern

.. include:: /includes/indexes/commit-quorum-vs-write-concern.rst

## Example

The following command builds two indexes on the `inventory` collection of the `products` database:

```javascript
db.getSiblingDB("products").runCommand(
  {
    createIndexes: "inventory",
    indexes: [
        {
            key: {
                item: 1,
                manufacturer: 1,
                model: 1
            },
            name: "item_manufacturer_model",
            unique: true
        },
        {
            key: {
                item: 1,
                supplier: 1,
                model: 1
            },
            name: "item_supplier_model",
            unique: true
        }
    ],
    writeConcern: { w: "majority" }
  }
)
```

When the indexes successfully finish building, MongoDB returns a results document that includes a status of `"ok" : 1`.

### Create a Wildcard Index

> **Note:** For complete documentation on Wildcard Indexes, see
`wildcard-index-core`.

The following lists examples of wildcard index creation:

- `createIndexes-command-wildcard-onepath`
- `createIndexes-command-wildcard-allpaths`
- `createIndexes-command-wildcard-inclusion`
- `createIndexes-command-wildcard-exclusion`
Create a Wildcard Index on a Single Field Path ``````````````````````````````````````````````

.. include:: /includes/extracts/wildcard-index-example-pre.rst

The following operation creates a wildcard index on the `product_attributes` field:

```bash
use inventory
db.runCommand(
  {
    createIndexes: "products_catalog",
    indexes: [
      {
        key: { "product_attributes.$**" : 1 },
        name: "wildcardIndex"
      }
    ]
  }
)
```

With this wildcard index, MongoDB indexes all scalar values of `product_attributes`. If the field is a nested document or array, the wildcard index recurses into the document/array and indexes all scalar fields in the document/array.

The wildcard index can support arbitrary single-field queries on `product_attributes` or one of its nested fields:

```bash
db.products_catalog.find( { "product_attributes.superFlight" : true } )
db.products_catalog.find( { "product_attributes.maxSpeed" : { $gt : 20 } } )
db.products_catalog.find( { "product_attributes.elements" : { $eq: "water" } } )
```

> **Note:** The path-specific wildcard index syntax is incompatible with the
`wildcardProjection` option. See the |projection-ref| for more
information.

Create a Wildcard Index on All Field Paths ``````````````````````````````````````````

.. include:: /includes/extracts/wildcard-index-example-pre.rst

The following operation creates a wildcard index on all scalar fields (excluding the `_id` field):

```bash
use inventory
db.runCommand(
  {
    createIndexes: "products_catalog",
    indexes: [
      {
        key: { "$**" : 1 },
        name: "wildcardIndex"
      }
    ]
  }
)
```

With this wildcard index, MongoDB indexes all scalar fields for each document in the collection. If a given field is a nested document or array, the wildcard index recurses into the document/array and indexes all scalar fields in the document/array.

The created index can support queries on any arbitrary field within documents in the collection:

```bash
db.products_catalog.find( { "product_price" : { $lt : 25 } } )
db.products_catalog.find( { "product_attributes.elements" : { $eq: "water" } } )
```

> **Note:** Wildcard indexes omit the `_id` field by default. To include the
`_id` field in the wildcard index, you must explicitly include it
in the `wildcardProjection` document. See |projection-ref| for
more information.

Create a Wildcard Index on Multiple Specific Field Paths ````````````````````````````````````````````````````````

.. include:: /includes/extracts/wildcard-index-example-pre.rst

The following operation creates a wildcard index and uses the `wildcardProjection` option to include only scalar values of the `product_attributes.elements` and `product_attributes.resistance` fields in the index.

```bash
use inventory
db.runCommand(
  {
    createIndexes: "products_catalog",
    indexes: [
      {
        key: { "$**" : 1 },
        "wildcardProjection" : {
          "product_attributes.elements" : 1,
          "product_attributes.resistance" : 1
        },
        name: "wildcardIndex"
      }
    ]
  }
)
```

While the key pattern `"$**"` covers all fields in the document, the `wildcardProjection` field limits the index to only the included fields and their nested fields.

If a field is a nested document or array, the wildcard index recurses into the document/array and indexes all scalar fields in the document/array.

The created index can support queries on any scalar field included in the `wildcardProjection`:

```bash
db.products_catalog.find( { "product_attributes.elements" : { $eq: "Water" } } )
db.products_catalog.find( { "product_attributes.resistance" : "Bludgeoning" } )
```

> **Note:** .. include:: /includes/extracts/wildcard-index-inclusion-exclusion.rst

Create a Wildcard Index that Excludes Multiple Specific Field Paths ```````````````````````````````````````````````````````````````````

.. include:: /includes/extracts/wildcard-index-example-pre.rst

The following operation creates a wildcard index and uses the `wildcardProjection` document to index all scalar fields for each document in the collection, excluding the `product_attributes.elements` and `product_attributes.resistance` fields:

```bash
use inventory
db.runCommand(
  {
    createIndexes: "products_catalog",
    indexes: [
      {
        key: { "$**" : 1 },
        "wildcardProjection" : {
           "product_attributes.elements" : 0,
           "product_attributes.resistance" : 0
        },
        name: "wildcardIndex"
      }
    ]
  }
)
```

While the key pattern `"$**"` covers all fields in the document, the `wildcardProjection` field excludes the specified fields from the index.

If a field is a nested document or array, the wildcard index recurses into the document/array and indexes all scalar fields in the document/array.

The created index can support queries on any scalar field **except** those excluded by `wildcardProjection`:

```bash
db.products_catalog.find( { "product_attributes.maxSpeed" : { $gt: 25 } } )
db.products_catalog.find( { "product_attributes.superStrength" : true } )
```

> **Note:** .. include:: /includes/extracts/wildcard-index-inclusion-exclusion.rst

### Create Index With Commit Quorum

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous-fcv.rst

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous.rst

.. include:: /includes/indexes/template-commit-quorum-intro.rst

The following operation creates an index with a `commit quorum <createIndexes-cmd-commitQuorum>` of `"majority"`, or a simple majority of data-bearing members:

```javascript
db.getSiblingDB("examples").runCommand(
  { 
    createIndexes: "invoices",
    indexes: [
      { 
        key: { "invoices" : 1 },
        "name" : "invoiceIndex"
      }
    ],
    "commitQuorum" : "majority"
  }
)
```

The `primary` marks index build as ready only after a simple majority of data-bearing voting members "vote" to commit the index build. For more information on index builds and the voting process, see `index-operations-replicated-build`.

## Output

The :dbcommand:`createIndexes` command returns a document that indicates the success of the operation. The document contains some but not all of the following fields, depending on outcome:

### Output Example

The following code block illustrates an example of the `createIndexes` output on a sharded cluster. On a sharded cluster, `createIndexes` outputs a `raw` embedded document which contains a document for each shard the index is built on. The keys of the `raw` embedded document are concantenations of shard id and the hostname and port of the individual nodes that make up the shard.

```javascript
{
  raw: {
    'atlas-2m11gv-shard-1/atlas-2m11gv-shard-01-00.cpfgx.mongodb.net:27017,atlas-2m11gv-shard-01-01.cpfgx.mongodb.net:27017,atlas-2m11gv-shard-01-02.cpfgx.mongodb.net:27017': {
      numIndexesBefore: 3,
      numIndexesAfter: 5,
      createdCollectionAutomatically: false,
      commitQuorum: 'votingMembers',
      ok: 1
    },
    'atlas-2m11gv-shard-0/atlas-2m11gv-shard-00-00.cpfgx.mongodb.net:27017,atlas-2m11gv-shard-00-01.cpfgx.mongodb.net:27017,atlas-2m11gv-shard-00-02.cpfgx.mongodb.net:27017': {
      numIndexesBefore: 3,
      numIndexesAfter: 5,
      createdCollectionAutomatically: false,
      commitQuorum: 'votingMembers',
      ok: 1
    }
  },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1743624296, i: 7 }),
    signature: {
      hash: Binary.createFromBase64('22j0GK8SIK806T+0OdCY6qYHocM=', 0),
      keyId: Long('7438621020069560323')
    }
  },
  operationTime: Timestamp({ t: 1743624296, i: 7 })
}  
```
