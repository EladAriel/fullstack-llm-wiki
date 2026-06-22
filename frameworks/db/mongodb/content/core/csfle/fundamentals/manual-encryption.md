---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/fundamentals/manual-encryption.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

# ========================= {+csfle-abbrev+} {+manual-enc-title+}

## Overview

.. include:: /includes/queryable-encryption/qe-csfle-manual-enc-overview.rst

{+manual-enc-first+} is available in the following MongoDB products:

- MongoDB Community Server
- MongoDB Enterprise Advanced
- MongoDB Atlas
## Use {+manual-enc-title+}

To use {+manual-enc+} you must perform the following actions in your {+csfle-abbrev+}-enabled application:

- `csfle-fundamentals-manual-encryption-client-enc`
- `csfle-fundamentals-manual-encryption-update-operations`
- `Manually <csfle-fundamentals-manual-encryption-manual-decryption>`
or `Automatically <csfle-fundamentals-manual-encryption-automatic-decryption>` Decrypt Fields in Your Documents

### Create a ClientEncryption Instance

To use {+manual-enc+}, you must create a `ClientEncryption` instance. `ClientEncryption` is an abstraction used across drivers and :binary:`~bin.mongosh` that encapsulates the {+key-vault-long+} and {+kms-abbr+} operations involved in {+manual-enc+}.

To create a `ClientEncryption` instance, you must specify the following information:

- A `MongoClient` instance with access to your {+key-vault-long+}
- The namespace of your {+key-vault-long+}
- A `kmsProviders` object configured with access to the
{+kms-abbr+} provider hosting your {+cmk-long+}

For more `ClientEncryption` options, see `csfle-reference-mongo-client`.

To view code snippets that show how to create a `ClientEncryption` instance, see the `csfle-fundamentals-manual-encryption-example` section of this guide.

### Encrypt Fields in Read and Write Operations

You must update read and write operations throughout your application such that your application encrypts fields before performing read and write operations.

To encrypt fields, use the `encrypt` method of your `ClientEncryption` instance.

To view code snippets that show how to use the `encrypt` method, see the `csfle-fundamentals-manual-encryption-example` section of this guide.

### Manual Decryption

You can decrypt your encrypted fields manually or automatically when using {+manual-enc+}.

To decrypt your fields manually, use the `decrypt` method of your `ClientEncryption` instance.

To view code snippets that show how to use the `decrypt` method, see the `csfle-fundamentals-manual-encryption-example` section of this guide.

### Automatic Decryption

To decrypt your fields automatically, configure your `MongoClient` instance as follows:

- Specify your {+key-vault-long+}
- Specify a `kmsProviders` object
- If you use MongoDB Community Server, set the `bypassAutoEncryption`
option to `True`

> **Note:** Although automatic encryption requires MongoDB Enterprise or MongoDB
Atlas, automatic decryption is available in the following MongoDB
products:
- MongoDB Community Server
- MongoDB Enterprise Advanced
- MongoDB Atlas

To view a code snippet demonstrating how to enable automatic decryption, select the tab corresponding to your preferred language:

## Example

Assume you want to insert documents with the following structure into your MongoDB instance:

## Server-Side Field Level Encryption Enforcement

MongoDB supports using `schema validation <schema-validation-overview>` to enforce encryption of specific fields in a collection.

A client performing {+csfle+} with the {+manual-enc+} mechanism on a MongoDB instance configured to enforce encryption of certain fields must encrypt those fields as specified on the MongoDB instance.

To learn how to set up server-side {+csfle-abbrev+} enforcement, see `csfle-reference-server-side-schema`.

## Learn More

To learn more about {+key-vault-long+}s, {+dek-long+}s, and {+cmk-long+}s, see `qe-reference-keys-key-vaults`.

To learn more about {+kms-abbr+} providers and `kmsProviders` objects, see `qe-fundamentals-kms-providers`.

To view and download full runnable code examples for the topics covered above, select a programming language:

- [C#](https://github.com/mongodb/mongo-csharp-driver/blob/main/tests/MongoDB.Driver.Examples/ExplicitEncryptionExamples.cs)_
- [Go](https://github.com/mongodb/mongo-go-driver/blob/master/internal/integration/client_side_encryption_test.go)_
- [Java](https://github.com/mongodb/mongo-java-driver/blob/main/driver-sync/src/test/functional/com/mongodb/client/ClientSideEncryptionSessionTest.java)_
- [Node.js](https://github.com/mongodb/node-mongodb-native/blob/main/test/integration/client-side-encryption/client_side_encryption.prose.22.range_explicit_encryption.test.ts)_
- [Python](https://github.com/mongodb/mongo-python-driver/blob/master/test/test_encryption.py)_
