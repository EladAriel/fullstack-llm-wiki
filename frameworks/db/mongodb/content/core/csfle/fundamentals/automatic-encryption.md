---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/fundamentals/automatic-encryption.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Automatic Encryption

MongoDB supports automatically encrypting fields in read and write operations when using {+csfle+}. You can perform automatic encryption using :binary:`~bin.mongosh` and official MongoDB drivers. For a complete list of official compatible drivers with support for {+csfle-abbrev+}, see Driver Compatibility `csfle-driver-compatibility`.

## How Encrypted Writes and Reads Work

The following diagrams show how the client application and driver write and read field-level encrypted data.

### Encrypted Writes

For write operations, the driver encrypts field values prior to writing to the MongoDB database.

The following diagram shows the steps taken by the client application and driver to perform a write of field-level encrypted data:

.. image:: /images/CSFLE_Write_Encrypted_Data.png

### Encrypted Reads

For read operations, the driver encrypts field values in the query prior to issuing the read operation.

For read operations that return encrypted fields, the driver automatically decrypts the encrypted values only if the driver was configured with access to the Customer Master Key (CMK) and Data Encryption Keys (DEK) used to encrypt those values.

The following diagram shows the steps taken by the client application and driver to query and decrypt field-level encrypted data:

.. image:: /images/CSFLE_Read_Encrypted_Data.png

## Enabling Automatic {+csfle+}

To enable automatic encryption, specify automatic encryption settings in your client's `MongoClient` instance.

The following code snippets show how to create a client with automatic encryption enabled in `mongosh` and MongoDB drivers:

.. include:: /includes/automatic-enc-options/tabs.rst

For more information on CSFLE-specific `MongoClient` settings, see `csfle-reference-mongo-client`.

## Server-Side Field Level Encryption Enforcement

MongoDB supports using `schema validation <schema-validation-overview>` to enforce encryption of specific fields in a collection. Clients performing automatic {+csfle+} have specific behavior depending on the database connection configuration:

- If the connection
`{+auto-encrypt-options+} <csfle-enc-options-example>` `schemaMap` object contains a key for the specified collection, the client uses that object to perform automatic field level encryption and ignores the remote schema. At minimum, the local rules **must** encrypt those fields that the remote schema marks as requiring encryption.

- If the connection
`{+auto-encrypt-options+} <csfle-enc-options-example>` `schemaMap` object does not contain a key for the specified collection, the client downloads the server-side remote schema for the collection and uses it to perform automatic field level encryption.

> **Important:**   .. include:: /includes/queryable-encryption/qe-csfle-schema-validation-warning.rst

To learn how to set up server-side {+csfle-abbrev+} enforcement, see `csfle-reference-server-side-schema`.
