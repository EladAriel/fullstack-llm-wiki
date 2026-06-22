---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.createIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# db.collection.createIndex() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-createIndex.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`~db.collection.createIndex()` method has the following form:

### Parameters

The :method:`~db.collection.createIndex()` method takes the following parameters:

## Options

The `options` document contains a set of options that controls the creation of the index. Different index types can have additional options specific for that type.

Multiple index options can be specified in the same document. However, if you specify multiple option documents the :method:`db.collection.createIndex()` operation will fail.

Consider the following :method:`db.collection.createIndex()` operation:

If the options specification had been split into multiple documents like this: `{ unique: true }, { sparse: true, expireAfterSeconds: 3600 }` the index creation operation would have failed.

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

The following options are available for `2d <2d-index>` indexes only:

### Options for `wildcard` indexes

`Wildcard indexes <wildcard-index-core>` can use the `wildcardProjection` option.

## Behaviors

### Recreating an Existing Index

If you call :method:`db.collection.createIndex()` for an index that already exists, MongoDB does not recreate the index.

### Index Options

Non-Collation and Non-Hidden Options ````````````````````````````````````

With the exception of the `collation option <method-createIndex-collation-option>`, if you create an index with one set of index options and then try to recreate the same index but with different index options, MongoDB will not change the options nor recreate the index.

The `hidden <createIndexes-hidden-option>` option can be changed without dropping and recreating the index. See `method-createIndex-hidden-option`.

To change the other index options, drop the existing index with :method:`db.collection.dropIndex()` before running :method:`db.collection.createIndex()` with the new options.

Collation Option ````````````````

.. include:: /includes/extracts/collation-index-options.rst

Hidden Option ``````````````

To hide or unhide existing indexes, you can use the following :binary:`~bin.mongosh` methods:

- :method:`db.collection.hideIndex()`
- :method:`db.collection.unhideIndex()`
For example,

- To change the `hidden` option for an index to `true`, use the
:method:`db.collection.hideIndex()` method:

- To change the `hidden` option for an index to `false`, use the
:method:`db.collection.unhideIndex()` method:

> **Seealso:** `/core/index-hidden`

### Transactions

.. include:: /includes/extracts/transactions-explicit-ddl.rst

### Index Builds

.. versionchanged:: 7.1

.. include:: /includes/index-build-improvements.rst

## Examples

.. include:: /includes/sample-data-usage.rst

.. include:: /includes/sample-data-additional-fields-note.rst

### Create an Ascending Index on a Single Field

The following example creates an ascending index on the field `title`.

If the `keys` document specifies more than one field, then :method:`~db.collection.createIndex()` creates a `compound index`.

### Create an Index on Multiple Fields

The following example creates a compound index on the `year`, `runtime`, and `title` fields:

Compound indexes can include a single `hashed <index-type-hashed>` field. Compound hashed indexes require `featureCompatibilityVersion <view-fcv>` set to at least `5.0`.

The following example creates a compound index on the `title` field (in ascending order) and the `runtime` field (hashed):

The order of fields in a compound index is important for supporting :method:`~cursor.sort()` operations using the index.

> **Seealso:** - `sort-on-multiple-fields`
- `sort-index-prefix`

### Create Indexes with Collation Specified

The following example creates an index on the `movies` collection named `title_fr`. The example creates the index with the `collation <create-index-collation>` that specifies the locale `fr` and comparison strength `2`:

The following example creates a compound index named `title_category_fr` with a `collation <create-index-collation>`. The collation applies only to the index keys with string values.

The collation applies to the indexed keys whose values are string.

For queries or sort operations on the indexed keys that uses the same collation rules, MongoDB can use the index. The indexes use collation of `strength: 2`, which results in case-insensitive queries when the index is used. For details, see `createIndex-collation-index-use`.

### Create a Wildcard Index

- .. include:: /includes/extracts/wildcard-index-id.rst
- .. include:: /includes/indexes/wildcard-restrictions.rst
To learn more, see:

- `About Wildcard Indexes <wildcard-index-core>`
- `Wildcard Index Restrictions <wildcard-index-restrictions>`
For examples, see:

- `createIndex-method-wildcard-onepath`
- `createIndex-method-wildcard-allpaths`
- `createIndex-method-wildcard-inclusion`
- `createIndex-method-wildcard-exclusion`
Create a Wildcard Index on a Single Field Path ``````````````````````````````````````````````

The following operation creates a wildcard index on the `awards` field:

With this wildcard index, MongoDB indexes all scalar values of `awards`. If the field is a nested document or array, the wildcard index recurses into the document or array and indexes all scalar fields in the document or array.

The wildcard index can support arbitrary single-field queries on `awards` or one of its nested fields:

> **Note:** The path-specific wildcard index syntax is incompatible with the
`wildcardProjection` option. See the |projection-ref| for more
information.

Create a Wildcard Index on All Field Paths ``````````````````````````````````````````

The following operation creates a wildcard index on all scalar fields (excluding the `_id` field):

With this wildcard index, MongoDB indexes all scalar fields for each document in the collection. If a given field is a nested document or array, the wildcard index recurses into the document or array and indexes all scalar fields in the document or array.

The created index can support queries on any arbitrary field within documents in the collection:

> **Note:** Wildcard indexes omit the `_id` field by default. To include the
`_id` field in the wildcard index, you must explicitly include it
in the `wildcardProjection` document. See |projection-ref| for
more information.

Include Specific Fields in Wildcard Index Coverage ``````````````````````````````````````````````````

The following operation creates a wildcard index and uses the `wildcardProjection` option to include only scalar values of the `tomatoes.viewer` and `tomatoes.critic` fields in the index.

The pattern `"$**"` includes all fields in the document. Use the `wildcardProjection` field to limit the index to fields you specify. For complete documentation on `wildcardProjection`, see `createIndex-method-wildcard-option`.

If a field is a nested document or array, the wildcard index recurses into it and indexes all scalar fields in the document or array.

The wildcard index supports queries on any scalar field included in the `wildcardProjection`:

> **Note:** .. include:: /includes/extracts/wildcard-index-inclusion-exclusion.rst

Omit Specific Fields from Wildcard Index Coverage `````````````````````````````````````````````````

This example uses a wildcard index and a `wildcardProjection` document to index the scalar fields for each document in the collection.

The wildcard index excludes the `tomatoes.viewer` and `tomatoes.critic` fields:

The wildcard pattern `"$**"` includes all of the fields in the document. However, the `wildcardProjection` field excludes the specified fields from the index.

For complete documentation on `wildcardProjection`, see `createIndex-method-wildcard-option`.

If a field is a nested document or array, the wildcard index recurses into the document or array and indexes all scalar fields in the document or array.

The index can support queries on any scalar field **except** those excluded by `wildcardProjection`:

> **Note:** .. include:: /includes/extracts/wildcard-index-inclusion-exclusion.rst

### Create Index With Commit Quorum

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous-fcv.rst

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous.rst

.. include:: /includes/indexes/template-commit-quorum-intro.rst

The following operation creates an index with a `commit quorum <createIndex-method-commitQuorum>` of `"majority"`, or a simple majority of data-bearing voting members:

The `primary` marks index build as ready only after a simple majority of data-bearing voting members "vote" to commit the index build. For more information on index builds and the voting process, see `index-operations-replicated-build`.

## Additional Information

- The `/indexes` section of this manual for full
documentation of indexes and indexing in MongoDB.

- :method:`db.collection.getIndexes()` to view the specifications of
existing indexes for a collection.

- `<index-type-text>` for details on creating `text`
indexes.

- `index-feature-geospatial` for geospatial queries.
- `index-feature-ttl` for expiration of data.
