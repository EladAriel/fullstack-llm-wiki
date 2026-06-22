---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/reference/decryption.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# How CSFLE Decrypts Documents

This page describes how {+csfle-abbrev+} uses metadata from your {+dek-long+} and {+cmk-long+} to decrypt data.

## Metadata Used for Decryption

When you encrypt data using {+csfle-abbrev+}, the data you encrypt is stored as a :bsontype:`BinData <Binary>` subtype 6 object that includes the following metadata:

- The `_id` of the {+dek-long+} used to encrypt the data
- The encryption algorithm used to encrypt the data
{+dek-long+}s contain metadata that describes what {+cmk-long+} was used to encrypt them.

Drivers and :binary:`~bin.mongosh` use this metadata to attempt to automatically decrypt your data.

## Automatic Decryption Process

To automatically decrypt your data, your {+csfle-abbrev+}-enabled client performs the following procedure:

#. Check the `BinData` blob metadata of the field you intend to decrypt for the {+dek-long+} and encryption algorithm used to encrypt the value.

#. Check the {+key-vault-long+} configured in the current database connection for the specified {+dek-long+}. If the {+key-vault-long+} does not contain the specified key, automatic decryption fails and the driver returns an error.

#. Check the {+dek-long+} metadata for the {+cmk-long+} (CMK) used to encrypt the key material.

#. Decrypt the {+dek-long+}. This process varies by KMS provider:

#. Decrypt the `BinData` value using the decrypted {+dek-long+} and appropriate algorithm.

Applications with access to the MongoDB server that do not also have access to the required CMK and {+dek-long+}s cannot decrypt the `BinData` values.

## Automatically Encrypted Read Behavior

For read operations, the driver encrypts field values in the query document using your encryption schema prior to issuing the read operation.

Your client application then uses the `BinData` metadata to automatically decrypt the document you receive from MongoDB.

To learn more about encryption schemas, see `csfle-fundamentals-create-schema`.

## Learn More

To learn how to configure the database connection for {+csfle+}, see `csfle-reference-mongo-client`.

To learn more about the relationship between {+dek-long+}s and {+cmk-long+}s, see `qe-reference-keys-key-vaults`.
