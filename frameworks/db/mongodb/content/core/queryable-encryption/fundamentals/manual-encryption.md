---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/fundamentals/manual-encryption.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# {+qe+} with {+manual-enc-title+}

## Overview

.. include:: /includes/queryable-encryption/qe-csfle-manual-enc-overview.rst

{+manual-enc-first+} is available in the following MongoDB products:

- MongoDB Community Server
- MongoDB Enterprise Advanced
- MongoDB Atlas
## Use {+manual-enc-title+}

### Create a ClientEncryption Instance

`ClientEncryption` is an abstraction used across drivers and :binary:`~bin.mongosh` that encapsulates the {+key-vault-long+} and {+kms-abbr+} operations involved in {+manual-enc+}.

To create a `ClientEncryption` instance, specify:

- A `kmsProviders` object configured with access to the
{+kms-abbr+} provider hosting your {+cmk-long+}

- The namespace of your {+key-vault-long+}
- If you use MongoDB Community Server, set the `bypassQueryAnalysis`
option to `True`

- A `MongoClient` instance with access to your {+key-vault-long+}
For more `ClientEncryption` options, see `qe-reference-mongo-client`.

### Encrypt Fields in Read and Write Operations

You must update read and write operations throughout your application such that your application encrypts fields before performing read and write operations.

To encrypt fields, use the `encrypt` method of your `ClientEncryption` instance. Specify the following:

- The value to be encrypted
- The algorithm used: `Indexed`, `Unindexed`, or `Range`
- The ID of the {+dek-long+}
- The `contention factor <qe-contention>` (if you are using the
`Indexed` or `Range` algorithm)

- If you are performing a read operation using the `Indexed` or
`Range` algorithm, set the query type defined for your field.

- The `range` options `min, max<qe-field-min-max>` (if you
are using the `Range` algorithm)

> **Note:** The query type only applies to read operations.
To learn more about query types, see `qe-query-types`.

Algorithm Choice ````````````````

Use the `Indexed` or `Range` algorithm if you specify a `queryType` on the field.

`Indexed` supports equality queries. `Range` supports range queries. `Indexed` and `Range` fields require an index on the server. The index is created by specifying the `encryptedFields` option in :method:`db.createCollection()`.

> **Note:** .. include:: /includes/rangePreview-deprecated.rst

### Automatic Decryption

To decrypt fields automatically, configure your `MongoClient` instance as follows:

- Specify a `kmsProviders` object
- Specify your {+key-vault-long+}
- If you use MongoDB Community Server, set the `bypassQueryAnalysis`
option to `True`

> **Note:** Automatic decryption is available in MongoDB Community Server.
Automatic encryption requires MongoDB Enterprise or MongoDB
Atlas.

## Server-Side Field Level Encryption Enforcement

`qe-specify-fields-for-encryption` to enforce encryption of specific fields in a collection.

`Indexed` and `Range` fields require an index on the server. The index is created by specifying the `encryptedFields` option in :method:`db.createCollection()`.

If your MongoDB instance enforces the encryption of specific fields, any client performing {+qe+} with {+manual-enc+} must encrypt those fields as specified. To learn how to set up server-side {+qe+} enforcement, see `qe-fundamentals-encrypt-query`.

## Learn More

To learn more about {+key-vault-long+}s, {+dek-long+}s, and {+cmk-long+}s, see `qe-reference-keys-key-vaults`.

To learn more about {+kms-abbr+} providers and `kmsProviders` objects, see `qe-fundamentals-kms-providers`.
