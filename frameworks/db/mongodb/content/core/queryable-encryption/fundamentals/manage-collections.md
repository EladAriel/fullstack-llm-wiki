---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/fundamentals/manage-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================

# Encrypted Collections

Field level encryption comes with performance and storage costs. Every field you choose to encrypt:

- Adds writes to insert and update operations.
- Requires additional storage, because MongoDB maintains an index of
encrypted fields to improve query performance.

This section summarizes the storage and write impact of encrypting collections, and explains how to compact encrypted collection indexes to minimize these costs. If you want to encrypt fields and configure them for querying, see `<qe-fundamentals-encrypt-query>`.

## Overview

{+qe+} introduces the ability to encrypt sensitive fields in your documents using randomized encryption, while still being able to query the encrypted fields.

With {+qe+}, a given plaintext value always encrypts to a different ciphertext, while still remaining queryable. To enable this functionality, {+qe+} uses three data structures:

- Two metadata collections
- A field in every document in the encrypted collection called `__safeContent__`
> **Warning:** It is critical that these data structures are not modified or
deleted, or query results will be incorrect.

## Metadata Collections

When you create an encrypted collection, MongoDB creates two metadata collections:

- `enxcol_.<collectionName>.esc`, referred to as `ESC`
- `enxcol_.<collectionName>.ecoc`, referred to as `ECOC`
When you insert documents with a queryable encrypted field, MongoDB updates the metadata collections to maintain an index that enables querying. The field becomes an "indexed field". This comes at a cost in storage and write speed for every such field.

> **Important:** When you drop an encrypted collection, drop the associated metadata
collections immediately afterwards:
- `enxcol_.<collectionName>.esc`
- `enxcol_.<collectionName>.ecoc`
Otherwise, re-creating the collection with the same name puts the metadata
collections in a conflicted state that consumes excess storage space and
degrades CRUD performance.

## Equality and Range Query Impact

Equality queries carry fixed additional costs for storage and write operations. Range query costs depend on the queryable field's `parameters <qe-field-configuration>`. Tightly bounding these queries greatly decreases their performance impact.

## Write Costs for Equality Queryable Fields

### Insert Operations

When inserting a document, each indexed field requires two additional writes to metadata collections.

- One write to `ESC`
- One write to `ECOC`
### Update Operations

When updating a document, each indexed field requires two additional writes to metadata collections.

- One write to `ESC`
- One write to `ECOC`
### Delete Operations

When deleting a document, indexed fields do not require any additional writes.

## Storage Costs for Equality Queryable Fields

Before any metadata compaction, the `ESC` and `ECOC` contain one metadata document for every field/value pair of every indexed field. Indexing one encrypted field/value pair across 1000 documents requires 1000 documents in the `ESC` and 1000 documents in the `ECOC`.

> **Note:** A {+qe+} collection that encrypts every field can take up to 2-3 times the
storage space, to account for metadata collections. For example, a 1 GB
collection may have a storage requirement of 2-3 GB.

### Best Practices

- Don't encrypt fields that don't need it. Most data only requires a small
subset of fields to be encrypted, such as those that contain Personally Identifiable Information.

- Don't enable range queries on a field if equality queries are sufficient for
your users.

- For encrypted fields with range queries enabled, review the field
configuration, especially the `min, max, <qe-field-min-max>` and `precision <qe-field-precision>` parameters. Setting tight bounds for range queries greatly decreases the performance impact of those fields.

- `Model your data <manual-data-modeling-intro>` and prototype it to
determine the actual storage and write increases for your deployment.

## Metadata Collection Compaction

As you insert or update documents, the metadata collections change and grow. Metadata collection compaction empties the `ECOC` and reduces the size of the `ESC`.

### Scheduling Metadata Compaction

> **Important:** In the worst case, running metadata compaction reveals the number of unique
field/value pairs inserted across all documents since the previous
compaction.
For details on the exact information revealed by metadata compaction,
see "Section 6: Theoretical Analysis" and "Section 9: Guidelines" in
MongoDB's [Queryable Encryption Technical Paper](https://www.mongodb.com/collateral/queryable-encryption-technical-paper).

As a best practice, keep track of the following information:

- `encfields`: the number of encrypted fields per document.
- `docinserts`: the number of documents inserted since the last compaction.
- `valinserts`: the number of unique field/value pairs inserted since the
last compaction.

To reduce the size of the `ESC` metadata collection by at least `t` documents, run metadata compaction when the following formula is satisfied:

(`encfields` · `docinserts`) - `valinserts` ≥ `t`

The number of encrypted fields per document multiplied by the number of insertions since last compaction, minus the number of unique field/value pairs inserted across all documents since the last compaction, should be greater than or equal to the number of documents to remove from the `ESC`.

Example ```````

For example, in a collection with six encrypted fields, you can reduce the size of the `ESC` by at least 1000 documents when total documents inserted and unique field/value pairs inserted since the last compaction meet the following conditions:

(6 · `docinserts`) - `valinserts` ≥ `1000`

The formula would be satisfied, for example, if 200 documents were inserted since the last compaction with a total of 200 unique field/value pairs across all documents, or if 400 documents were inserted since the last compaction with 700 unique field/value pairs.

### Running Metadata Compaction

You must run metadata compaction manually. Use :binary:`~bin.mongosh` and run the `db.collection.compactStructuredEncryptionData()` command:

You can check the size of a metadata collection using :binary:`~bin.mongosh` and running the :method:`db.collection.totalSize()` command.
