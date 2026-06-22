---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/fundamentals/encrypt-and-query.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Encrypted Fields and Enabled Queries

When you use {+qe+}, you define encrypted fields at the collection level using an {+enc-schema+}. Encrypting a field and enabling queries increases storage requirements and impacts query performance. You can configure an encrypted field for either equality or range queries, but not both. Configure fields for the expected query type.

For instructions on creating an {+enc-schema+} and configuring querying, see `qe-create-encryption-schema`.

## Supported Query Types and Behavior

For a list of supported query operators and behavior with encrypted fields, see `qe-supported-query-operators`.

## Schema Validation

{+qe+} requires a server-side {+enc-schema+} to enforce encryption of specific fields in a collection. Clients using automatic {+qe+} behave differently depending on the database connection configuration:

- At minimum, local rules must encrypt the same fields as the remote schema on
the server.

- If the connection `encryptedFieldsMap` object contains a key for the
specified collection, the client uses that object to perform automatic {+qe+}, rather than using the remote schema.

- If the connection `encryptedFieldsMap` object doesn't contain a
key for the specified collection, the client downloads the remote schema for the collection and uses it instead.

> **Important:**   When using a remote schema:
  - The client trusts that the server has a valid schema
  - The client uses the remote schema to perform automatic {+qe+}
    only. The client does not enforce any other validation rules
    specified in the schema.

## Considerations when Enabling Querying

Decide which fields should be encrypted and/or queryable prior to creating your collection. Changing which fields are encrypted or queryable requires rebuilding the collection's {+enc-schema+} and re-creating the collection.

If you don't need to query an encrypted field, you may not need to enable querying on that field. You can still retrieve the document by querying other fields that are queryable or unencrypted.

For every encrypted collection, MongoDB creates `two metadata collections <qe-metadata-collections>`, increasing storage space. MongoDB creates an index for each encrypted field, which increases the duration of write operations on that field. When a write operation updates an indexed field, MongoDB updates the related index.

## Configure Encrypted Fields for Optimal Search and Storage

MongoDB provides the following parameters to facilitate debugging and performance tuning:

### Substring Parameters

.. include:: includes/queryable-encryption/qe-warning-public-preview.rst

### Advanced Query Parameters

> **Warning:** These parameters are intended for advanced users only. The
default values are suitable for the majority
of use cases, and should only be modified if your use case
requires it.
